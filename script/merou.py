import parameters
import fileoperations

def main():
    # Collect the project parameters either from command-line arguments or from JSON file
    project_params = parameters.read()

    print
    print 'New project:'
    print 'Project name        : ', project_params['project_name']
    print 'Project description : ', project_params['description']
    print 'Developer name      : ', project_params['developer_name']
    print 'GitHub repo         : ', project_params['github']
    print 'Output path         : ', project_params['output_path']
    print

    # Creating new project files
    print 'Creating new project... ',
    fileoperations.new_project_tree(project_params)
    print 'done.'

    # Configure the new project replacing the template values
    print 'Configuring new project... ',


if __name__ == '__main__':
    main()
