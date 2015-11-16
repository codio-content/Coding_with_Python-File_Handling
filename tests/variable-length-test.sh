#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh
start_python_test 'variable-length.py'

TEXTFILEPATH='/home/codio/workspace/content/textfiles'

function runonetest () {
  SRCFILE="${1}"
  FNAME="${2}"
  LNAME="${3}"
  BDAY="${4}"
  cp "${SRCFILE}" /tmp/fixed1
  cat /tmp/fixed1 | sed -E "s/(${FNAME})[\|](${LNAME})[\|][0-9]{8}/\1|\2|${BDAY}/g" > /tmp/e1
  run_python_test "/tmp/fixed1 ${FNAME} ${LNAME} ${BDAY}" ""
  if [ "$(diff /tmp/fixed1 /tmp/e1)" != "" ]; then
    echo "Your program output did not match the expected output."
    echo "<br/><hr/><small><b>Your output:</b></small>"
    cat /tmp/fixed1
    echo "<br/><hr/><small><b>Expected output:</b></small><hr/>"
    cat /tmp/e1
    exit 1
  fi
}

runonetest "${TEXTFILEPATH}/pipe.txt" Adam Smithers 00000000
runonetest "$TEXTFILEPATH/poem.txt" Adam Smith 11111111
runonetest "${TEXTFILEPATH}/pipe.txt" Adam Smith 11111900

end_python_test

