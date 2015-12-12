/*
 * This file is part of the <PROJECT_NAME> project:
 *     https://github.com/<USER_NAME>/<REPO_NAME>
 */

#include "<PROJECT_NAME_LOWER>_config.h"

#include <iostream>

int main()
{
    std::cout << "<PROJECT_NAME> version: " << <PROJECT_NAME>_VERSION_STRING << std::endl;

    <PROJECT_NAME_LOWER>::Dummy d;
    int var = d.Var();

    return 0;
}
