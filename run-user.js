
var vm = require('vm');
var fs = require('fs');

var data;

//
// Read in the code to execute in a seperate VM. This is passed from the text of the
// button in the content.
//
try {
  data = fs.readFileSync(process.argv[2], 'UTF-8');
}
catch(e) {
  console.log(e)
  process.exit(1)
}

//
// Create an artificial command line argument array
//
var mockargv= ['javascript'].concat(process.argv.slice(2));

//
// This is the sandbox "scoping" context we will use to run the seperate VM in which
// to process the test code.
//
var scope = {
  output: function(val) {
    console.log("**** STILL USING OUTPUT ****");
    console.log(val);
  },
  process: {
    argv: mockargv // process.argv
  },
  require:require,
  console: console
}

//
// Run the test code in a new context, but in this VM.
//
try {
  vm.runInNewContext(data, scope)
}
catch(e) {
  //
  // There was a problem, so lint out the issues and present them to the user.
  //
  var msg = '';

  var CLIEngine = require("eslint").CLIEngine;

  var cli = new CLIEngine({
    envs: ["node"],
    useEslintrc: false,
    rules: {
      // semi: 2
    }
  });

  var report = cli.executeOnFiles([process.argv[2]]);
  
  if(report.errorCount) {
    for (var i = 0; i < report.results.length; i++) {
      for (var j = 0; j < report.results[i].messages.length; j++) {
        var obj = report.results[i].messages[j];

        if(msg.length > 0) {
          msg += '\n';
        }

        msg += "error: '" + obj.message + "' at line " + obj.line + ", column " + obj.column 
      }
    };
  }
  else {
    msg = e.toString()    
  }

  console.log(msg);
  process.exit(1);
}
