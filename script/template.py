import datetime
import re

def build_substitution_table(params):
    table = { '<PROJECT_NAME>'       : params['project_name'],
              '<PROJECT_NAME_LOWER>' : params['project_name'].lower(),
              '<CURRENT_YEAR>'       : datetime.datetime.now.year,
              '<OWNER_NAME>'         : params['developer_name'],
              '<GITHUB_REPO_NAME>'   : params['github_repo'],
              '<PROJECT_OVERVIEW>'   : params['description'] }

    return table

def substitute_in_string(str, substitutions):
    str_buf = str
    for pattern, value in substitutions:
        str_buf = re.sub(pattern, value, str_buf)

    return str_buf

def substitute_in_file(file, substitutions):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    with open(file_name, 'w') as f:
        for line in lines:
            sources.write(substitute_in_string(line, substitutions))
