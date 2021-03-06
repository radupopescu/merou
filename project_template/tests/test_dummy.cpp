/*
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 *
 * This file is part of the <PROJECT_NAME> project:
 *     https://github.com/<GITHUB_USER_NAME>/<GITHUB_REPO_NAME>
 */

#include "catch.hpp"

#include "dummy.h"

TEST_CASE( "Dummy::Var() returns 0", "[dummy]" ) {
  <PROJECT_NAME_LOWER>::Dummy d;
  REQUIRE( d.Var() == 0);
}
