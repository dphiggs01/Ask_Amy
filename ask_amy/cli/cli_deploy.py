import json
import pip
from subprocess import Popen, PIPE
import os
import shutil
import sys
from time import sleep


class DeployCLI(object):
    def deploy(self, config_file_name):
        deploy_dict = self.load_config(config_file_name)
        skill_home_dir = deploy_dict['skill_home_dir']
        distribution_dir = skill_home_dir + '/dist'
        ask_amy_impl = None
        if 'ask_amy_dev' in deploy_dict:
            if deploy_dict['ask_amy_dev']:
                ask_amy_home_dir = deploy_dict['ask_amy_home_dir']
                ask_amy_impl = ask_amy_home_dir + '/ask_amy'

        self.install_ask_amy(distribution_dir, ask_amy_impl)
        self.copy_skill_to_dist(skill_home_dir, distribution_dir)
        self.make_zipfile(deploy_dict['lambda_zip'], distribution_dir)
        out = self.run(self.lamabda_update_function(deploy_dict))
        deploy_response = out[1]
        return json.dumps(deploy_response, indent=4)

    def create(self, config_file_name):
        deploy_dict = self.load_config(config_file_name)
        out = self.run(self.lambda_create_function(deploy_dict))
        out = self.run(self.lambda_add_trigger(deploy_dict))
        return out

    def log(self, log_group_name, log_stream_name=None, next_forward_token=None):
        if log_stream_name is None:
            log_stream_name = self.latest_log_stream_for_log_group(log_group_name)
        log_events_tuple = self.run(self.cloudwatch_get_log_events(log_group_name, log_stream_name, next_forward_token))
        log_events_dict = log_events_tuple[1]
        next_forward_token = log_events_dict['nextForwardToken']
        log_events_lst = log_events_dict['events']
        for event_dict in log_events_lst:
            message = event_dict['message']
            sys.stdout.write(message)
        return next_forward_token, log_stream_name

    def latest_log_stream_for_log_group(self, log_group_name):
        log_streams_tuple = self.run(self.cloudwatch_latest_log_stream(log_group_name))
        log_streams_dict = log_streams_tuple[1]
        log_streams = log_streams_dict['logStreams']
        latest_stream = log_streams[-1]
        log_stream_name = latest_stream['logStreamName']
        return log_stream_name

    def log_tail(self, log_group_name):
        next_forward_token, log_stream_name = self.log(log_group_name)
        not_done = True
        try:
            while not_done:
                sleep(1)
                next_forward_token, log_stream_name = self.log(log_group_name, log_stream_name, next_forward_token)
        except KeyboardInterrupt:
            pass
        return

    def install_ask_amy(self, destination_dir, source_dir=None):
        ask_amy_dist = destination_dir + '/ask_amy'
        shutil.rmtree(ask_amy_dist, ignore_errors=True)
        if source_dir is not None:
            shutil.copytree(source_dir, ask_amy_dist)
        else:
            pip.main(['install', '--upgrade', 'ask_amy', '-t', destination_dir])

    def copy_skill_to_dist(self, source_dir, destination_dir):
        print(source_dir)
        files = os.listdir(source_dir)
        try:
            for file in files:
                full_path = source_dir+os.sep+file
                if file.endswith(".py"):
                    shutil.copy(full_path, destination_dir)
                if file.endswith(".json"):
                    shutil.copy(full_path, destination_dir)
        except FileNotFoundError:
            sys.stderr.write("ERROR: filename not found {}\n".format(full_path))
            sys.exit(-1)


    def make_zipfile(self, output_filename, source_dir):
        output_filename = output_filename[:-4]
        shutil.make_archive(output_filename, 'zip', source_dir)

    def lamabda_update_function(self, config_dict):
        aws_region = config_dict['aws_region']
        skill_name = config_dict['skill_name']
        lambda_zip = 'fileb://' + config_dict['skill_home_dir'] + '/' + config_dict['lambda_zip']
        aws_profile = config_dict['aws_profile']
        cmd_args = ['aws', 'lambda', 'update-function-code',
                    '--region', aws_region,
                    '--function-name', skill_name,
                    '--zip-file', lambda_zip,
                    '--profile', aws_profile
                    ]
        return cmd_args

    def lambda_create_function(self, config_dict):
        skill_name = config_dict['skill_name']
        lambda_runtime = config_dict['lambda_runtime']
        aws_role = config_dict['aws_role']
        lambda_handler = config_dict['lambda_handler']
        lambda_timeout = config_dict['lambda_timeout']
        lambda_memory = config_dict['lambda_memory']
        lambda_zip = 'fileb://' + config_dict['skill_home_dir'] + '/' + config_dict['lambda_zip']
        cmd_args = ['aws', 'lambda', 'create-function',
                    '--function-name', skill_name,
                    '--runtime', lambda_runtime,
                    '--role', aws_role,
                    '--handler', lambda_handler,
                    '--description', skill_name,
                    '--timeout', lambda_timeout,
                    '--memory-size', lambda_memory,
                    '--zip-file', lambda_zip
                    ]
        return cmd_args

    def lambda_add_trigger(self, config_dict):
        skill_name = config_dict['skill_name']
        cmd_args = ['aws', 'lambda', 'add-permission',
                    '--function-name', skill_name,
                    '--statement-id', 'alexa_trigger',
                    '--action', 'lambda:InvokeFunction',
                    '--principal', 'alexa-appkit.amazon.com'
                    ]
        return cmd_args

    def cloudwatch_latest_log_stream(self, log_group):
        cmd_args = ['aws', '--output', 'json', 'logs', 'describe-log-streams',
                    '--log-group-name', log_group,
                    '--order-by', 'LastEventTime'
                    ]
        return cmd_args

    def cloudwatch_latest_log_stream(self, log_group):
        cmd_args = ['aws', '--output', 'json', 'logs', 'describe-log-streams',
                    '--log-group-name', log_group,
                    '--order-by', 'LastEventTime'
                    ]
        return cmd_args

    def cloudwatch_get_log_events(self, log_group, log_stream_name, next_forward_token=None):
        cmd_args = ['aws', '--output', 'json', 'logs', 'get-log-events',
                    '--log-group-name', log_group,
                    '--log-stream-name', log_stream_name
                    ]
        if next_forward_token is not None:
            cmd_args.append('--next-token')
            cmd_args.append(next_forward_token)
        return cmd_args

    def load_config(self, config_file_name):
        deploy_dict = None
        try:
            file_ptr_r = open(config_file_name, 'r')
            deploy_dict = json.load(file_ptr_r)
            file_ptr_r.close()
        except FileNotFoundError:
            sys.stderr.write("ERROR: filename not found {}\n".format(config_file_name))
            sys.exit(-1)
        return deploy_dict

    def run(self, args):
        try:
            process = Popen(args, stdout=PIPE)
            out, err = process.communicate()
            out = str(out, 'utf-8')
            if not out:
                out = '{}'

            return process.returncode, json.loads(out), err
        except Exception as e:
            sys.stderr.write("ERROR: command line error %s\n" % args)
            sys.stderr.write("ERROR: %s\n" % e)

        return None
