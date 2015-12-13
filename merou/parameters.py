import argparse
import json
import sys
import unittest

def read():
    parser = build_argument_parser()

    params = build_parameters_with_parser(parser)

    return params

def build_parameters_with_parser(parser, arg_list = None):
    arguments = parser.parse_args(arg_list)

    template_file = arguments.template_file
    if template_file != None:
        parameters = get_parameters_from_file(template_file)
    else:
        parameters = get_parameters_from_arguments(arguments)

    # Default parameter values, where needed. We do it here s.t. we don't don't have to do it twice,
    # once for the parser.add_argument call and one more time in get_parameters_from_file
    if parameters['project_name'] == None:
        parameters['project_name'] = 'NewProject'
    if parameters['output_path'] == None:
        parameters['output_path'] = './'

    return parameters

def build_argument_parser():
    parser = argparse.ArgumentParser(description='Generate a new C++ project')

    parser.add_argument('-p', '--project_name',
                        help='the name of the new project; must be a single word (default: "NewProject")')
    parser.add_argument('-d', '--description', nargs="*",
                        help='brief description of the project')
    parser.add_argument('-n', '--developer_name', nargs="*",
                        help='the name of the project developer')
    parser.add_argument('-u', '--github_user_name',
                        help='GitHub user name')
    parser.add_argument('-g', '--github_repo',
                        help='name of the associated GitHub repository')
    parser.add_argument('-o', '--output_path',
                        help='output path where the project will be created (default: "./")')
    parser.add_argument('-t', '--template_file',
                        help='JSON file that contains the parameters of the new project. '
                        + 'If this argument is provided, the others are not considered.')

    return parser

def get_parameters_from_file(template_file):
    with open(template_file) as tf:
        parameters = json.load(tf)

        return parameters

def get_parameters_from_arguments(arguments):
    params = {'project_name'     : arguments.project_name,
              'github_user_name' : arguments.github_user_name,
              'github_repo'      : arguments.github_repo,
              'output_path'      : arguments.output_path}

    if arguments.description != None:
        params['description'] = ' '.join(arguments.description)
    if arguments.developer_name != None:
        params['developer_name'] = ' '.join(arguments.developer_name)

    return params

# Tests
class ArgumentParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = build_argument_parser()

    def testParserIsConstructed(self):
        self.assertIsInstance(self.parser, argparse.ArgumentParser)

    def testParseAllArguments(self):
        params = build_parameters_with_parser(self.parser,
                                              '-p TestProject -d Description of the project -n Anon Ymous -u anonymous -g project -o ../'.split())
        self.assertEqual(params['project_name'], 'TestProject')
        self.assertEqual(params['description'], 'Description of the project')
        self.assertEqual(params['developer_name'], 'Anon Ymous')
        self.assertEqual(params['github_user_name'], 'anonymous')
        self.assertEqual(params['github_repo'], 'project')
        self.assertEqual(params['output_path'], '../')

    def testParseWithoutArguments(self):
        params = build_parameters_with_parser(self.parser, [])
        self.assertEqual(params['output_path'], './')
        self.assertEqual(params['project_name'], 'NewProject')
