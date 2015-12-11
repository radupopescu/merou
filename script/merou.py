import parameters

def main():
    project_params = parameters.read()

    print "Creating new project:"
    print "Project name        : ", project_params['project_name']
    print "Project description : ", project_params['description']
    print "Developer name      : ", project_params['developer_name']
    print "GitHub repo         : ", project_params['github']
    print "Output path         : ", project_params['output_path']

if __name__ == '__main__':
    main()
