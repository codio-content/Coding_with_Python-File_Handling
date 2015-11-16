#!/bin/bash

cd /home/codio/workspace/challenges

DEFAULT_FAILURE_MESSAGE='Your output was incorrect. Try again.'

function start_python_test {
  echo "<h3>Program Output</h3>"

  PYTHON_TEST_SCRIPT="${1}"
  
  if [ "${2}" != "" ]; then
    DEFAULT_FAILURE_MESSAGE="${2}"
  fi

COMPILE=$(python3 -m py_compile "${PYTHON_TEST_SCRIPT}")
  if [ $? -ne 0 ]; then
    echo "<p>There is an error is your program.</p>"
    exit 1
  fi
}

LAST_SUCCESS=""

function run_python_test {
  ARGS="${1}"
  ACTUAL_OUTPUT=$(python3 "${PYTHON_TEST_SCRIPT}" ${ARGS})
  if [ $? -ne 0 ]; then
    # bad exit code
    exit 1
  fi
  
  EXPECTED_OUTPUT="${2}"
  
  MESSAGE_ON_ERROR=${DEFAULT_FAILURE_MESSAGE}
  if [ "${3}" != "" ]; then
    MESSAGE_ON_ERROR="${3}"
  fi
  
  if [ "$ACTUAL_OUTPUT" == "$EXPECTED_OUTPUT" ]; then
    LAST_SUCCESS="<small><b>Input:</b> ${ARGS}</small>"
    LAST_SUCCESS="${LAST_SUCCESS}<br/><small><b>Your Output: </b></small>${ACTUAL_OUTPUT}"
    return 0
  fi
  echo "<small><b>Program Failed for Input: </b></small>${ARGS}"
  echo "<small><b>Expected Output:</b> </small>${EXPECTED_OUTPUT}"
  echo "<small><b>Your Program Output:</b> </small>${ACTUAL_OUTPUT}"
  echo "<br/>${MESSAGE_ON_ERROR}"
  exit 1
}

function end_python_test {
  echo ${LAST_SUCCESS}
  echo "<hr/><h3>Challenge Feedback</h3>"
  echo "Well done!"
  exit 0
}


