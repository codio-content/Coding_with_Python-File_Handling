
import sys

inputs = []
outputs = []

def input0(v):
  global inputs
  return inputs[0]

def input1(v):
  global inputs
  return inputs[1]

def input2(v):
  global inputs
  return inputs[2]

def output(v):
  global outputs
  outputs.append(v)
  # print(v)

def printException():
    exc_type, exc_obj, tb = sys.exc_info()
    print(exc_obj)  

def test(_file, _inputs, _outputs, _message = 'Not quite right please try again'):
  global outputs
  outputs = []
  
  global inputs
  inputs = _inputs
  
  try:
    exec(open(_file).read())

    if len(outputs) != len(_outputs):
      print('Your program is not outputting the expected number of outputs')
      exit(1)

    # print(outputs)
    # print(_outputs)
      
    for i in range(len(outputs)):
      if outputs[i] != _outputs[i]:
        print(_message)
        exit(1)
    
  except (IOError, SyntaxError, NameError) as e:
    printException()
    exit(1)
    