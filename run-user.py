
import sys

def input0(v):
  return v

def input1(v):
  return v

def input2(v):
  return v

def output(v):
  print(v)

def printException():
    exc_type, exc_obj, tb = sys.exc_info()
    print(exc_obj)
  
try:
  exec(open(sys.argv[1]).read())
  
  exit(0)
except (IOError, SyntaxError, NameError) as e:
  printException()
  
exit(1)
