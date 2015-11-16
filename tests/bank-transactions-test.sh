#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh
start_python_test 'bank-transactions.py'

TEXTFILEPATH='/home/codio/workspace/content/textfiles'

function writeaccounts () {
  OUTPATH="${1}"
  echo -n "" > "${OUTPATH}"
  for a in "${ACCOUNT_INFO[@]}"; do
    if [ "${a}" != "" ] ; then
      echo "${a}" >> "${OUTPATH}"
    fi
  done
}

function writetx () {
  OUTPATH="${1}"
  echo -n "" > "${OUTPATH}"
  for a in "${TX_LIST[@]}"; do
    if [ "${a}" != "" ] ; then
      echo "${a}" >> "${OUTPATH}"
    fi
  done
}

function txadd () {
  AMOUNT=${1}
  ACCOUNT_INDEX=${2}
  PIN=${3}
  ACCOUNT_NUMBER=`echo "${ACCOUNT_INFO[${ACCOUNT_INDEX}]}" | cut -d '|' -f 1`
  ACCOUNT_PIN=`echo "${ACCOUNT_INFO[${ACCOUNT_INDEX}]}" | cut -d '|' -f 2`
  ACCOUNT_BALANCE=`echo "${ACCOUNT_INFO[${ACCOUNT_INDEX}]}" | cut -d '|' -f 3`
  TX_LIST+=("add|${AMOUNT}|${ACCOUNT_NUMBER}|${PIN}")
  
  if [ "${PIN}" == "${ACCOUNT_PIN}" ] ; then
    NEW_BALANCE=$(expr ${ACCOUNT_BALANCE} + ${AMOUNT})
    ACCOUNT_INFO[${ACCOUNT_INDEX}]="${ACCOUNT_NUMBER}|${PIN}|${NEW_BALANCE}"
  fi
}

function txsub () {
  AMOUNT=${1}
  ACCOUNT_INDEX=${2}
  PIN=${3}
  ACCOUNT_NUMBER=`echo "${ACCOUNT_INFO[${ACCOUNT_INDEX}]}" | cut -d '|' -f 1`
  ACCOUNT_PIN=`echo "${ACCOUNT_INFO[${ACCOUNT_INDEX}]}" | cut -d '|' -f 2`
  ACCOUNT_BALANCE=`echo "${ACCOUNT_INFO[${ACCOUNT_INDEX}]}" | cut -d '|' -f 3`
  TX_LIST+=("sub|${AMOUNT}|${ACCOUNT_NUMBER}|${PIN}")
  
  if [ "${PIN}" == "${ACCOUNT_PIN}" ] ; then
    NEW_BALANCE=$(expr ${ACCOUNT_BALANCE} - ${AMOUNT})
    if [ "${NEW_BALANCE}" -ge "0" ] ; then
      ACCOUNT_INFO[${ACCOUNT_INDEX}]="${ACCOUNT_NUMBER}|${PIN}|${NEW_BALANCE}"  
    fi
  fi
}

function resetaccounts () {
  ACCOUNT_INFO=()
  TX_LIST=()
  TX_LIST[0]=""
  ACCOUNT_INFO[0]="1000|1234|10000"
  ACCOUNT_INFO[1]="1020|2222|0"
  ACCOUNT_INFO[2]="3000|3344|1000"
  ACCOUNT_INFO[3]="2020|1234|90000"
}

function runonetest () {
  ACCOUNTS="${1}"
  TXS="${2}"
  EXPECTED="${3}"
  
  run_python_test "${ACCOUNTS} ${TXS}" ""
  
  if [ "$(diff -B ${ACCOUNTS} ${EXPECTED})" != "" ]; then
    echo "Your program output did not match the expected output."
    echo "<br/><hr/><small><b>Your output:</b></small>"
    cat ${ACCOUNTS}
    echo "<br/><hr/><small><b>Expected output:</b></small><hr/>"
    cat ${EXPECTED}
    exit 1
  fi
}

resetaccounts
writeaccounts "/tmp/a1" 
txadd 1000 0 1234
txsub 1000 1 2222
txsub 1000 2 3344
writetx "/tmp/tx"
writeaccounts "/tmp/e1"
runonetest "/tmp/a1" "/tmp/tx" "/tmp/e1"

resetaccounts
writeaccounts "/tmp/a1" 
txadd 100000 0 1234
txsub 100000 1 2222
txadd 100 2 9876
writetx "/tmp/tx"
writeaccounts "/tmp/e1"
runonetest "/tmp/a1" "/tmp/tx" "/tmp/e1"

resetaccounts
writeaccounts "/tmp/a1" 
txadd 100000 3 1234
txadd 100000 2 3344
txadd 100 2 9765
writetx "/tmp/tx"
writeaccounts "/tmp/e1"
runonetest "/tmp/a1" "/tmp/tx" "/tmp/e1"


end_python_test

  
