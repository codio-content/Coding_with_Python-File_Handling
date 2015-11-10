
import sys
import re
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

inputs = []
outputs = []


def printException():
    exc_type, exc_obj, tb = sys.exc_info()
    print(exc_obj)  

def test(_file, _inputs, _outputs, _message = 'Not quite right please try again'):
  global outputs
  outputs = []
  
  global inputs
  inputs = _inputs
  
  try:
    # redirect stdout to a string (fake_stdout)                                      
    # compile into byte code and then execute the byte code                          
    # then process the printed output from the code we ran                           
    code= compile(open(_file).read(), '<string>', 'exec')                      
    orig_stdout= sys.stdout
    fake_stdout= StringIO()
    sys.stdout= fake_stdout

    # replace sys.argv while we exec the code
    orig_argv= sys.argv
    sys.argv= ['python', _file] 
    for i in range(0, len(inputs)):
      sys.argv.append(inputs[i])
    exec(code)

    # put everything back like it was before
    sys.stdout= orig_stdout
    sys.argv= orig_argv
    sys.stderr.flush()

    # set up the outputs
    outputs= fake_stdout.getvalue().split("\n")		
    last_line= outputs.pop()
    if len(last_line.strip()) > 0:
      outputs.append(last_line)

    #print(outputs)

    if(callable(_outputs)):
      _outputs= _outputs(_inputs)
    
    if len(outputs) != len(_outputs):
      print('Your program is not outputting the expected number of outputs')
      exit(1)

    # print(outputs)
    # print(_outputs)
      
    for i in range(len(outputs)):
      #if(callable(_outputs[i])):
      #  _outputs[i]= _outputs[i](_inputs)
        
      if str(outputs[i]) != str(_outputs[i]):
        #print(str(outputs[i]) + " != " + str(_outputs[i]))
        print(_message)
        exit(1)
    
  except (IOError, SyntaxError, NameError) as e:
    printException()
    exit(1)
    
