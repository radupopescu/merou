#include "catch.hpp"

#include "dummy.h"

TEST_CASE( "Dummy::Var() returns 0", "[dummy]" ) {
  <PROJECT_NAME_LOWER>::Dummy d;
  REQUIRE( d.Var() == 0);
}
