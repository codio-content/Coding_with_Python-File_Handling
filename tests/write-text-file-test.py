import test
import sys
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

script = 'challenges/write-text-file.py'

# shortcut version of the assignment that uses python's internals
# to solve the problem
def getOutput(inputList):
  f= open(inputList[0], 'r')
  t= f.read()
  result= t.replace(inputList[2], inputList[3])
  result= result
  return result


# Our validate function does not look at stdout, so it 
# need to be different
def validate(inputs, myOutput, studentOutput):
  studentAnswer= open(inputs[1], 'r').read()
  return studentAnswer == myOutput

# path to my content text files
CPATH= 'content/textfiles'
  
# copy the input files to tmp files
# so the users won't mangle them up
tmp1= '/tmp/w1'
tmp2= '/tmp/w2'
tmp3= '/tmp/w3'
open(tmp1,'w').write(open(CPATH + '/parrot.txt', 'r').read())
open(tmp2,'w').write(open(CPATH + '/empty.txt', 'r').read())
open(tmp3,'w').write(open(CPATH + '/parrot.txt', 'r').read())

# set up the output files in tmp so they are wrong
# in case nothing is done to them at all
out1= '/tmp/o1'
out2= '/tmp/o2'
out3= '/tmp/o3'
open(out1,'w').write("NO")
open(out2,'w').write("NO")
open(out3,'w').write("NO")

# run the tests
test.test(script, [tmp1, out1, 'parrot', 'chicken'], getOutput, _validate=validate)
test.test(script, [tmp2, out2, 'parrot', 'chicken'], getOutput, _validate=validate)
test.test(script, [tmp3, out3, 'fungi', 'Pateng'], getOutput, _validate=validate)

print('Well done')
