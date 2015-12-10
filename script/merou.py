import argparse
import json
import sys

def read_arguments():
    parser = argparse.ArgumentParser(description='Read the template file and generate a new project')

    parser.add_argument('template_file', help='JSON file that contains the parameters of the new project')

    return parser.parse_args()


def get_project_parameters(template_file):
    """
    Arguments:
    template_file -- name of the JSON file containing the new project parameters

    Returns a dictionary with the default values for the following keys:
    project_name        - the name of the new project; must be a single word (default: "MyNewProject")
    developer_name      - the name of the project developer (default: "Kameloso")
    project_path        - output path where the project will be created (default: "../<git_repo>")
    git_repo            - name of the associated GitHub repository (default: "")
    description         - text describing the project; will be placed in the Overview section
                          of the README.md file (default: "")
    """

    with open(template_file) as tf:
        project_json = json.load(tf)

        params = {'project_name' : 'MyNewProject',
                  'developer_name' : 'Kameloso',
                  'git_repo' : '',
                  'description' : ''}
        params.update(project_json)
        params.setdefault('project_path', '../' + params.get('git_repo'))

    return params

def main():
    arguments = read_arguments()

    template_file = arguments.template_file

    project_parameters = get_project_parameters(template_file)

if __name__ == '__main__':
    main()
