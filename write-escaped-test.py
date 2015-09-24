
import sys

_script = '/home/codio/workspace/challenge2/write-escaped.py';
_input0 = [['one','1'],['Two', '2'],['3','3'] ]
_expected = 'one,1\nTwo,2\n3,3'

def input0(v):
  global _input0
  return _input0



try:
  exec(open(_script).read())

  _result = open('/home/codio/workspace/challenge2/data.csv').read()

  if _result == _expected:
    print('Well done')
    exit(0)
  else:
    print('Not quite right please try again')
    exit(1)

except (IOError, SyntaxError, NameError) as e:
  exc_type, exc_obj, tb = sys.exc_info()
  print(exc_obj)  
  exit(1)
