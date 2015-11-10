import sys
import logging


try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO



logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def printException():
    exc_type, exc_obj, tb = sys.exc_info()
    print(exc_obj)
  
try:
  # redirect stdout to a string (fake_stdout)
  # compile into byte code and then execute the byte code
  # then process the printed output from the code we ran
  orig_stdout= sys.stdout
  fake_stdout= StringIO()
  sys.stdout= fake_stdout
  code= compile(open(sys.argv[1]).read(), '<string>', 'exec')
  exec(code)
  sys.stderr.flush()
  sys.stdout.flush()
  sys.stdout= orig_stdout
  output= fake_stdout.getvalue()
  print(output)
  sys.stderr.flush()
  sys.stdout.flush()
  exit(0)
except (IOError, SyntaxError, NameError) as e:
  printException()
  
exit(1)
