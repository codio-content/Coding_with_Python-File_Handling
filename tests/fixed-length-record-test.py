import test
import sys
import re

import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

script = 'challenges/fixed-length-record.py'
CPATH= 'content/textfiles';

# get the correct output
def correctOutput(input):
  inputPath= input[0]
  fn= (input[1] + "                ")[0:16]
  ln= (input[2] + "                ")[0:16]
  newBday= (input[3] + '        ')[0:8]
  filecontent= open(inputPath, 'r').read()
  myOutput= re.sub(r''+fn+ln+'........', fn+ln+newBday, filecontent);
  return myOutput

# validation function that the test harness calls
def validate(input, internalTestOutput, studentTestOutput):
  studentOutput= open(input[0]).read()
  return studentOutput == internalTestOutput
  

# clear the output file to the default values
open('/tmp/fixed1','w').write(open(CPATH + '/fixed-length.txt', 'r').read())
open('/tmp/fixed2','w').write(open(CPATH + '/fixed-length.txt', 'r').read())
open('/tmp/fixed3','w').write(open(CPATH + '/poem.txt', 'r').read())

test.test(script, ['/tmp/fixed1', 'Adam', 'Smith', '11111900'], correctOutput, _validate=validate),
test.test(script, ['/tmp/fixed2', 'Adam', 'Smithers', '00000000'], correctOutput, _validate=validate),
test.test(script, ['/tmp/fixed3', 'Adam', 'Smith', '11111111'], correctOutput, _validate=validate);

print ("Well done!")