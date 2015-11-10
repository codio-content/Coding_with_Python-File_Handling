import test
import sys
import re

import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

script = 'challenges/variable-length.py'
CPATH= 'content/textfiles';

def correctOutput(input):
  inputPath= input[0]
  fn= input[1]
  ln= input[2]
  newBday= input[3]
  filecontent= open(inputPath, 'r').read()
  myOutput= re.sub(r'(^|\s+|\W+)'+fn+'\|'+ln+'\|\d+', r"\1"+fn+"|"+ln+"|"+newBday, filecontent);
  return myOutput

  
def validate(input, internalTestOutput, studentTestOutput):
  studentOutput= open(input[0]).read()
  return studentOutput == internalTestOutput
  

# clear the output file to the default values
open('/tmp/v1','w').write(open(CPATH + '/pipe.txt', 'r').read())
open('/tmp/v2','w').write(open(CPATH + '/pipe.txt', 'r').read())
open('/tmp/v3','w').write(open(CPATH + '/poem.txt', 'r').read())

test.test(script, ['/tmp/v1', 'Adam', 'Smith', '11111900'], correctOutput, _validate=validate),
test.test(script, ['/tmp/v2', 'Adam', 'Smithers', '00000000'], correctOutput, _validate=validate),
test.test(script, ['/tmp/v3', 'Adam', 'Smith', '11111111'], correctOutput, _validate=validate);

print ("Well done!")