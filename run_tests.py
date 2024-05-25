import pytest

def run_login_tests():
    pytest.main(["-v", "--html=report.html", "-m", "login", "tests/"])

def run_register_tests():
    pytest.main(["-v", "--html=report.html", "-m", "register", "tests/"])

def run_change_password_tests():
    pytest.main(["-v", "--html=report.html", "-m", "change_password", "tests/"])

def run_all_tests():
    pytest.main(["-v", "--html=report.html", "tests/"])

if __name__ == "__main__":
    run_login_tests()

    # run_register_tests()

    # run_change_password_tests()

    # run_all_tests()
