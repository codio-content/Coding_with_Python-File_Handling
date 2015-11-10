import test
script = 'challenges/write-text-file.py';


#def replaceString(path, o, n):
#  f= open(path, 'r')
#	t= f.read()
#	re= new RegExp(o, "g")
#	return t.replace(re, n)

#function buildTest(pathi, patho, find, replace){
#  var safeOutputPath= '/tmp/' + patho.replace(/\W/g, '')
#  fs.unlink(safeOutputPath);
#  
##	var correctOutput= replaceString(pathi, find, replace);
#	return {
#		inputs: [pathi, safeOutputPath, find, replace],
#		outputs: [],
#    validate: function(i){
#      var actualOutput= fs.readFileSync(safeOutputPath, "utf8", "r");
#      var resultAsExpected= correctOutput == actualOutput;
#      return resultAsExpected;
#		}
#	}
#}

def getOutput(input):
  print("In the getOutput function")
  print(str(input))
  print("Not sure what is next honestly")
  
cpath= 'content/textfiles'
test.test(script, [cpath+'/parrot.txt', 'write1', 'parrot', 'chicken'], getOutput)
test.test(script, [cpath+'/empty.txt', 'write2', 'parrot', 'chicken'], getOutput)
test.test(script, [cpath+'/parrot.txt', 'write3', 'fungi', 'Pateng'], getOutput)

print('Well done')
