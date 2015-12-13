import argparse
import json

def read():
    parser = argparse.ArgumentParser(description='Generate a new C++ project')

    parser.add_argument('project_name', nargs="?",
                        help='the name of the new project; must be a single word (default: "NewProject")')
    parser.add_argument('-d', '--description', help='brief description of the project')
    parser.add_argument('-n', '--developer_name', help='the name of the project developer')
    parser.add_argument('-u', '--github_user_name', help='GitHub user name')
    parser.add_argument('-g', '--github_repo', help='name of the associated GitHub repository')
    parser.add_argument('-o', '--output_path',
                        help='output path where the project will be created (default: "./")')
    parser.add_argument('-t', '--template_file',
                        help='JSON file that contains the parameters of the new project. '
                        + 'If this argument is provided, the others are not considered.')

    arguments = parser.parse_args()

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

def get_parameters_from_file(template_file):
    with open(template_file) as tf:
        parameters =json.load(tf)

        return parameters

def get_parameters_from_arguments(arguments):
    params = {'project_name'     : arguments.project_name,
              'description'      : arguments.description,
              'developer_name'   : arguments.developer_name,
              'github_user_name' : arguments.github_user_name,
              'github_repo'      : arguments.github,
              'output_path'      : arguments.output_path}

    return params

