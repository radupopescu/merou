# Mérou - A helper for quickly creating new C++ projects

[![Build Status](https://travis-ci.org/radupopescu/merou.svg?branch=master)](https://travis-ci.org/radupopescu/merou)

## Overview

Many programming languages come with full featured tools for creating and managing projects written in these languages.
Some examples are Mix for Elixir, Rebar(3) for Erlang, Cabal for Haskell, SBT for Scala.
With C++, setting up a new project is a bit more involved, when one doesn't use an IDE.

Mérou aims to simplify this: it provides a simple C++ project skeleton that can easily be configured and extended.
The base features provided by the skeleton are:

+ CMake based project configuration
+ Dummy files for application and library parts of the code
+ Unit tests already set up
+ Travis integration

This project is under development, feedback is really appreciated. Please report any bugs and issues you encounter.

I hope you find Mérou helpful and enjoy using it.

## Usage

First step is to clone or download this repo to your computer. Mérou can be run without installing:
```
$ git clone https://github.com/radupopescu/merou.git
$ cd merou
$ bin/merou -h
```

To create a new C++ project, you can provide the project parameters as command line arguments.
For example:
```
$ bin/merou --project_name MyNewProject \
            --description Description of the project \
            --developer_name Radu Popescu \
            --github_user_name radupopescu \
            --github_repo mynewproject \
            -o ./
```
will create a new project entitled "MyNewProject", with the given description, with Radu Popescu as the author.
The GitHub user name of the author and the name of the (future) GitHub repo are also provided.
There values are used to customize the `README.md` file of the new project, inserting links for the issue tracker and the Travis-CI status.
Keep in mind that the GitHub project is not created by the `merou` command, you still have to do it yourself. The same goes for activating Travis-CI integration. Mérou helps you with the repetitive tasks of inserting the relevant sections in the `README.md` file, creating `.travis.yml` etc.

After issuing the previous command, the program will print out some progress information and your new project should be ready. Here is a basic overview of the new project:

* `README.md` - title, description, licensing information (MPL v2 by default, may add options for other licenses), links to GitHub issue tracker and Travis-CI build status badge
* `LICENSE` - license file (MPL v2)
* `AUTHORS`
* `cmake`  - directory with CMake scripts used for configuration
* `external`  - external files needed by the project. One can add additional TPLs here. By default, it only includes `catch.hpp` and its license file, which are downloaded when the new project is created
* `travis_build.sh` and `.travis.yml` - files for configuring Travis-CI
* `.lvimrc` - if you use `vim-localvimrc` and `ctrlp`, this file defines some basic ignore patterns for `ctrlp`
* `.ycm_extra_conf.py` - default configuration for `YouCompleteMe`
* `src` - sources that are compiled as a static library for your project
* `apps` - sources that produce your project's executables; the executables are linked with the static library
* `tests` - skeletons for your unit tests. The [Catch](https://github.com/philsquared/Catch) unit testing framework is used.
* a global header for your project (with the extension `.h.in`)
* the project is configured and built with CMake

All this should help you get started working on your new projects and should serve as a good base for further configuration.

### JSON Configuration

As an alternative to providing the project parameter as command line arguments, you can also specify them in a JSON file. An example file is provided (`test_project.json`). The parameters are equivalent to the long-form command line arguments. The JSON file is passed to `merou` with the `-t` arguments:
```
$ bin/merou -t test_project.json
```

## License and authorship

The contributors are listed in AUTHORS. This project uses the MPL v2 license, see LICENSE.

## Issues

To report an issue, please use the [Merou issue tracker](https://github.com/radupopescu/merou/issues) at github.com.

