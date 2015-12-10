if(${PROJECT_NAME}_BUILD_TESTS)
    file(GLOB test_sources *.cpp)

    add_executable(test_runner
        ${test_sources}
    )
    target_link_libraries(test_runner ${${PROJECT_NAME}_EXTERNAL_LIBRARIES})
endif()

