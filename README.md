# SPoG-test

SPoG-test is a [Playwright-python](https://playwright.dev/python/ "Playwright-python") based framework to test [trustification](https://github.com/trustification/trustification.git "trustification") UI. The purpose of this repo is to execute and test the trustification UI, where the backend REST API is tested with [RUST scripts](https://github.com/trustification/trustification/tree/main/integration-tests/tests).  Along the way there will be attempts to execute these tests automatically against the Trustification repo. 

## Quick Start
1. Clone the repository 

```
git clone https://github.com/trustification/spog-test.git
cd spog-test
```

2. The shell script [run_spog_tests.sh](run_spog_tests.sh) is capable of setting up the virtual environment and installing the required packages to execute the Automation scripts. At the end of the execution the HTML reports are stored into `results` directory. To run the script, the user should pass trustification application URL, registered Username and Password.

```
sh run_spog_tests.sh --base-url https://staging.trustification.dev/ -u test -p user@123
```

By default, the above step would execute the tests under [/tests](tests) directory.

The target tests directory and the results directory which can be changed with the command line arguments.

```
sh run_spog_tests.sh --base-url https://staging.trustification.dev/ -u test -p user@123 -r test_results_dir -t custom_tests_dir
```
 - [Playwright-python](https://playwright.dev/python/ "Playwright-python") is internally backed up with pytest. As an alternate to using the shell script run_spog_tests.sh, we can use python and pytest to directly install the requirements and execute the tests.
 - Playwright by default executes the scripts in headless mode, In order to execute the tests on browsers run the command `pytest --headed`

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md)