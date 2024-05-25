# Web Automation Testing with Selenium & Docker

This project demonstrates how to use Selenium with Docker to perform automated testing on a web application. The project includes login, registration, and password change test cases, all written in Python using the Pytest framework.

## Project Structure
```
Selenium-in-Docker/
├── Dockerfile       # Docker configuration file
├── requirements.txt # Python dependencies
├── tests/           # Directory containing test cases
│ ├── test_web.py    # Test cases for login, registration, password change
├── run_tests.py     # Script to run the tests
└── README.md        # Project documentation
```

## Setup

### Prerequisites

- Docker
- Python 3.8
- Chrome WebDriver or Edge WebDriver

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Caryio/Selenium-in-Docker.git
    cd Selenium-in-Docker
    ```

2. **Build the Docker image:**

    ```bash
    docker build -t selenium-docker-test .
    ```

3. **Install Python dependencies:**

    If you prefer to run the tests outside of Docker, you can install the dependencies locally:

    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

### Using Docker

1. **Run all tests:**

    ```bash
    docker run --rm selenium-docker-test
    ```

2. **Run specific test groups:**

    Uncomment the relevant function call in `run_tests.py` to execute specific test groups (login, registration, or change password).

### Without Docker

1. **Run all tests:**

    ```bash
    python run_tests.py
    ```

2. **Run specific test groups:**

    Uncomment the relevant function call in `run_tests.py` to execute specific test groups (login, registration, or change password).

## Test Cases

The test cases are organized in the `tests/test_web.py` file. Each test case uses Selenium to interact with the web application and Pytest markers to organize the tests into different groups.

- **Login Test:**
    - Opens the login page
    - Enters username and password
    - Clicks the login button
    - Asserts successful login by checking the page title

- **Registration Test:**
    - Opens the registration page
    - Enters user details (username, email, password)
    - Clicks the register button
    - Asserts successful registration by checking the page content

- **Change Password Test:**
    - Opens the change password page
    - Enters current and new passwords
    - Clicks the change password button
    - Asserts successful password change by checking the page content

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.
