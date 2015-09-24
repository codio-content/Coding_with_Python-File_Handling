cd /home/codio/workspace/challenge1
cp ../data-read-escaped-test.csv data.csv
python3 ../read-escaped-test.py
CODE=$?
cp ../data-read-escaped-backup.csv data.csv
exit $CODE