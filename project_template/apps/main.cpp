/*
 * This file is part of the <PROJECT_NAME> project:
 *     https://github.com/<GITHUB_USER_NAME>/<GITHUB_REPO_NAME>
 */

#include "<PROJECT_NAME_LOWER>_config.h"

#include <dummy.h>

#include <iostream>

int main()
{
    std::cout << "<PROJECT_NAME> version: " << <PROJECT_NAME>_VERSION_STRING << std::endl;

    <PROJECT_NAME_LOWER>::Dummy d;
    int var = d.Var();

    return 0;
}
