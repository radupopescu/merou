import os
import shutil

def new_project_tree(params):
    try:
        # Copy the template files into the new project directory
        project_template_dir = 'project_template'
        project_name_lower = params['project_name'].lower()
        new_project_path = os.path.join(params['output_path'], project_name_lower)
        if not os.path.isdir(new_project_path):
            shutil.copytree(project_template_dir, new_project_path)

            # Some files need to be renamed to match the new project name
            template_project_config = os.path.join(new_project_path, 'new_project_config.h.in')
            shutil.copy2(template_project_config,
                         os.path.join(new_project_path, project_name_lower + "_config.h.in"))
            os.remove(template_project_config)

        else:
            raise IOError('Project directory exists, aborting.')

    except shutil.Error as e:
        print e

