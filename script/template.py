import datetime
import os
import re

def build_substitution_table(params):
    table = { '<PROJECT_NAME>'       : params['project_name'],
              '<PROJECT_NAME_LOWER>' : params['project_name'].lower(),
              '<CURRENT_YEAR>'       : str(datetime.datetime.now().year),
              '<DEVELOPER_NAME>'     : params['developer_name'],
              '<GITHUB_REPO_NAME>'   : params['github_repo'],
              '<PROJECT_OVERVIEW>'   : params['description'] }

    return table

def substitute_in_line(line, substitutions):
    str_buf = line
    for (pattern, value) in substitutions.iteritems():
        str_buf = re.sub(pattern, value, str_buf)

    return str_buf

def substitute_in_file(file_name, substitutions):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    with open(file_name, 'w') as f:
        for line in lines:
            f.write(substitute_in_line(line, substitutions))

def build_file_list(dir_name):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(dir_name):
        for f in filenames:
            files.append(os.path.join(dirpath, f))

    return files


def configure_new_project(params):
    project_dir = os.path.join(params['output_path'], params['project_name'].lower())
    files = build_file_list(project_dir)
    substitutions = build_substitution_table(params)
    for f in files:
        substitute_in_file(f, substitutions)
