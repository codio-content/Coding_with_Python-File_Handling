#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test 'read-text-file.py'
run_python_test '../content/textfiles/empty.txt parrot' '0'
run_python_test '../content/textfiles/parrot.txt parrot' '3'
end_python_test 


