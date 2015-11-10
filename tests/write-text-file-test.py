import test
import sys
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

script = 'challenges/write-text-file.py'

def getOutput(inputList):
  f= open(inputList[0], 'r')
  t= f.read()
  result= t.replace(inputList[2], inputList[3])
  result= result
  return result
  
def validate(inputs, myOutput, studentOutput):
  logging.debug("MY VALIDATE")
  studentAnswer= open(inputs[1], 'r').read()
  return studentAnswer == myOutput


# copy the input files to tmp
cpath= 'content/textfiles'

tmp1= '/tmp/w1'
tmp2= '/tmp/w2'
tmp3= '/tmp/w3'

open(tmp1,'w').write(open(cpath + '/parrot.txt', 'r').read())
open(tmp2,'w').write(open(cpath + '/empty.txt', 'r').read())
open(tmp3,'w').write(open(cpath + '/parrot.txt', 'r').read())

# set up the output files in tmp
out1= '/tmp/o1'
out2= '/tmp/o2'
out3= '/tmp/o3'
open(out1,'w').write("NO")
open(out2,'w').write("NO")
open(out3,'w').write("NO")

test.test(script, [tmp1, out1, 'parrot', 'chicken'], getOutput, _validate=validate)
test.test(script, [tmp2, out2, 'parrot', 'chicken'], getOutput, _validate=validate)
test.test(script, [tmp3, out3, 'fungi', 'Pateng'], getOutput, _validate=validate)

print('Well done')
