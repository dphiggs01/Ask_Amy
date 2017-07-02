from ask_amy.tests.utility import TestCaseASKAmy
from ask_amy.cli.code_gen import dicttoxml
import json
import urllib
import urllib.request
from xml.dom.minidom import parseString

class TestDialog(TestCaseASKAmy):
    def setUp(self):
        pass

    def test_dialog_constr(self):
        print('hello world')
        #page = urllib.urlopen('http://quandyfactory.com/api/example')
        request_url = urllib.request.Request('http://quandyfactory.com/api/example')
        obj = self.load_json_file('../data/intent_schema.json')

        print(obj)

        xml = dicttoxml.dicttoxml(obj)

        dom = parseString(xml)
        print(dom.toprettyxml())


    def test_dialog_constr(self):
        iam_attach_role_policy = ['aws', '--output', 'json', 'iam', 'attach-role-policy',
                    '--role-name', 0,
                    '--policy-arn',1,
                    '---next',     2]
        print(self.process_args(iam_attach_role_policy,'one','two'))



    def process_args(self,arg_list,*args):
        # process the arg
        for index in range(0,len(arg_list)):
            if type(arg_list[index]) == int:
                # substitue for args passed in
                if arg_list[index] < len(args):
                    arg_list[index] = args[arg_list[index]]
                # if we more substitutions than args passed delete them
                else:
                    del arg_list[index-1:]
                    break
        return arg_list