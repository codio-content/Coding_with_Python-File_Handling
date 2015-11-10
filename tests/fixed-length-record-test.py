import test
import sys
import re

import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

script = 'challenges/fixed-length-record.py'
var cpath= 'content/textfiles';

def correctOutput(input):
  logging.debug("MY CORRECT OUTPUT FUNCTION CALLED")
  inputPath= input[0]
  fn= input[1]
  ln= input[2]
  newBday= input[3]
  
  p= re.compile("^"+fn+"\|"+ln+"\|\d+$")
  myOutput= p.sub(fn+"|"+ln+"|"+newBday, open(inputPath, 'r').read())
  return myOutput

  
def validate(input, o1, o2):
  studentOutput= open(input[0]).read()
  
  

# clear the output file to the default values
open('/tmp/fixed1','w').write(open(CPATH + '/fixed-length.txt', 'r').read())
open('/tmp/fixed2','w').write(open(CPATH + '/poem.txt', 'r').read())

test.test(script, ['/tmp/fixed1', 'Adam', 'Smith', '12121912'], correctOutput, _validate=validate),
test.test(script, ['/tmp/fixed2', 'Adam', 'Smith', '11111111'], correctOutput, _validate=validate);
