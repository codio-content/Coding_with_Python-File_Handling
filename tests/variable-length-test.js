var fs= require('fs');
var test = require('./test-fw.js');

function buildTest(pathi, patho, firstname, lastname, bday){
  var safeOutputPath= '/tmp/' + patho.replace(/\W/g, '')
  
  var startingData= fs.readFileSync(pathi, 'utf8')
  fs.writeFileSync(safeOutputPath, startingData, 'utf8')
  
  var regx= firstname+"[|]"+lastname+"[|]"+"\\d{8}";
  var re= new RegExp(regx);
	var correctOutput= startingData.replace(re, firstname+'|'+lastname+'|'+bday).replace(/\s\s*$/, '')
	return {
		inputs: [safeOutputPath, firstname, lastname, bday],
		outputs: [],
    validate: function(i){
      var actualOutput= fs.readFileSync(i.inputs[0], "utf8").replace(/\s\s*$/, '');
      var resultAsExpected= correctOutput == actualOutput;
      if(!resultAsExpected){
        console.info("ACTUAL\n" + actualOutput)
        console.info("CORRECT\n" + correctOutput)
        console.info("LOCAL: " + actualOutput.localeCompare(correctOutput))
      }
      return resultAsExpected;
		}
	}
}

var script = 'challenges/variable-length.js';

var cpath= 'content/textfiles';

test.tests(script, [
	buildTest(cpath+'/pipe.txt', 'vlength1', 'Adam', 'Smith', '02022222'),
	buildTest(cpath+'/pipe.txt', 'vlength2', 'Adam K', 'Smith', '11111111')
]);
