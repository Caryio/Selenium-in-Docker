import pytest

def run_all_tests():
    pytest.main(["-v", "--html=report.html", "tests/"])

def run_specific_test(test_name):
    pytest.main(["-v", "--html=report.html", f"tests/{test_name}.py"])

def run_tests_by_marker(marker):
    pytest.main(["-v", "--html=report.html", "-m", marker, "tests/"])

if __name__ == "__main__":
    run_all_tests()

    # run_specific_test("test_web")

    # run_tests_by_marker("login")
    # run_tests_by_marker("register")
    # run_tests_by_marker("change_password")
    # run_tests_by_marker("search")
    # run_tests_by_marker("navigation")
    # run_tests_by_marker("form_submission")
