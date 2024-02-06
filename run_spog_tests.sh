#! /usr/bin/env bash
set -e

#----------------- GLOBAL VARIABLES -----------------
TEST_RESULTS_DIR="results"
TEST_DIR="tests"
#--------------------- FUNCTIONS --------------------

arg_handle(){
    CLI_ARGS=$@
    ARGS_LIST="a:u:p:hr:t:"
    while getopts $ARGS_LIST opt; do
        case "$opt" in
            a)
                export TRUST_APP_URL="$OPTARG"
                ;;
            u)
                export TRUST_USER_NAME="$OPTARG"
                ;;
            p)
                export TRUST_USER_PASSWORD="$OPTARG"
                ;;
            r)
                TEST_RESULTS_DIR="$OPTARG"
                ;;
            t)
                TEST_DIR="$OPTARG"
                ;;
            h)
                help $OPTARG
                exit 0
                ;;
            :)
                echo "Option $OPTARG requires an option" >&2
                exit 1
                ;;
            \?)
                echo "Invalid option: $OPTARG" >&2
                help $OPTARG
                exit 1
                ;;
            
        esac
    done
}

set_env(){
    VENV_DIR="${PWD}/venv"
    cmd="${VENV_DIR}/bin/playwright --version"
    if ! $cmd &> /dev/null; then
        echo "Creating virual environment....."
        python3 -m venv ${VENV_DIR}
        source ${VENV_DIR}/bin/activate
        ${VENV_DIR}/bin/python3 -m pip install .
        playwright install
    fi
}

results_dir(){
    RESULTS="${PWD}/${TEST_RESULTS_DIR}/testrun-$(date +%Y-%m-%d-%H-%M-%S)"
    mkdir -p $RESULTS
}

help(){
    echo ""
    echo "Execute SPoG UI tests"
    echo ""
    echo "      To begin with, the user might need to configure and install the dependencies."
    echo "The information required to login to the application can be provided through flags."
    echo ""
    echo "Usage:"
    echo "      sh run_spog_tests.sh [options]"
    echo ""
    echo "Examples:"
    echo "sh run_spog_tests.sh -a https://staging.trustification.dev/ -u test -p user@123"
    echo ""
    echo "Options:"
    echo "       -a: Application URL"
    echo "       -u: Username"
    echo "       -p: Password"
    echo "       -t: Directory contains tests, defaults to /tests directory"
    echo "       -r: Directory for results, defaults to /results directory"
    echo ""
}

if [ "$#" -eq 0 ]; then
    help
    exit 1
fi

arg_handle "$@"
set_env
results_dir
pytest $TEST_DIR --html $RESULTS/report.html --application $TRUST_APP_URL --username $TRUST_USER_NAME --password $TRUST_USER_PASSWORD
set +e
