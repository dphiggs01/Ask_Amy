import sys
from ask_amy.cli.cli_deploy import DeployCLI



HELP_BLURB = (
    "To see help text, you can run:\n"
    "\n"
    "  ask-amy-cli help\n"
    "  ask-amy-cli <command> help\n"
)
USAGE = (
    "ask-amy-cli [options] <command> <subcommand> [parameters]\n"
    "%s" % HELP_BLURB
)

class AMYCLI(object):

    COMMANDS = ['help', 'deploy', 'create', 'log' ]
    def parse_command(self, args):

        if len(args) == 0:
            sys.stderr.write("usage: %s\n" % USAGE)
            return None

        if len(args) >= 1:
            #print('do cool stuff' + args[0])
            if args[0] in AMYCLI.COMMANDS:
                cmd = args.pop(0)
                return self.execute_command(cmd, args)


    def help_cmd(self, args):
        return HELP_BLURB

    #  ask-amy-cli deploy --deploy-json-file config.json
    def deploy_cmd(self, args):
        param = args.pop(0)
        expected_param = '--deploy-json-file'
        if expected_param == param:
            cli = DeployCLI()
            ret_val = cli.deploy(args[0])
        else:
            sys.stderr.write("ERROR: expected --deploy-json-file paramater \n")
            ret_val = None
        return ret_val

    #  ask-amy-cli create --deploy-json-file config.json
    def create_cmd(self, args):
        param = args.pop(0)
        expected_param = '--deploy-json-file'
        if expected_param == param:
            cli = DeployCLI()
            ret_val = cli.create(args[0])
        else:
            sys.stderr.write("ERROR: expected --deploy-json-file paramater \n")
            ret_val = None
        return ret_val


    def log_cmd(self, args):
        tail_log = '--tail-log'
        should_tail_log=False
        if tail_log in args:
            index = args.index(tail_log)
            args.pop(index)
            should_tail_log=True

        param = args.pop(0)
        expected_param = '--log-group-name'
        if expected_param == param:
            cli = DeployCLI()
            if should_tail_log:
                ret_val = cli.log_tail(args[0])
            else:
                ret_val = cli.log(args[0])
        else:
            sys.stderr.write("ERROR: expected --log-group-name paramater \n")
            ret_val = None
        return ret_val

    def execute_command(self, method_name, args):
        method = getattr(self, method_name+'_cmd')
        #print(method)
        return method(args)



def main():
    amy_cli = AMYCLI()
    args = sys.argv
    args.pop(0)
    sys.exit(amy_cli.parse_command(args))

if __name__ == '__main__':
    main()
