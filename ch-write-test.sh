cd /home/codio/workspace/challenge2
rm -f data.csv
touch data.csv
python3 ../write-escaped-test.py
CODE=$?
exit $CODE