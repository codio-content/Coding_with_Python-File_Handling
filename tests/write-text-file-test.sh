#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test 'write-text-file.py'

TEXTFILEPATH='/home/codio/workspace/content/textfiles'


function runonetext () {
  SRCFILE="${1}"
  OLDTEXT="${2}"
  NEWTEXT="${3}"
  cp "${SRCFILE}" /tmp/w1
  cat /tmp/w1 | sed -s "s/${OLDTEXT}/${NEWTEXT}/g" > /tmp/e1
  echo "RESET" > /tmp/o1
  run_python_test "/tmp/w1 /tmp/o1 ${OLDTEXT} ${NEWTEXT}" ""
  if [ "$(diff /tmp/o1 /tmp/e1)" != "" ]; then
    echo "Your program output did not match the expected output."
    echo "<br/><hr/><small><b>Your output:</b></small>"
    cat /tmp/o1
    echo "<br/><hr/><small><b>Expected output:</b></small><hr/>"
    cat /tmp/e1
    exit 1
  fi
}

runonetext "${TEXTFILEPATH}/parrot.txt" parrot Ni
runonetext "${TEXTFILEPATH}/empty.txt" parrot chicken
runonetext "$TEXTFILEPATH/parrot.txt" parrot 1
runonetext "$TEXTFILEPATH/parrot.txt" fungi Pateng
runonetext "$TEXTFILEPATH/parrot.txt" parrot chicken

end_python_test
