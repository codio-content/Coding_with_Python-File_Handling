
var vm = require('vm');
var fs = require('fs');
var async = require('async');

var DEBUG= false;



var test = {
  test: function(file, argv, cb) {
    var data = fs.readFileSync(file);
    var input = [];
    var output = [];

    var scope = {
      output: function(val) {
        output.push(val);
      },
      process: {
        argv: ['javascript', file].concat(argv)
      },
      require: require,
      console: console
    }

    // 
    // We will replace the console.log function with one which stores the
    // console output so we can check the test. We hold a pointer to the 
    // original "normal" console.log function so we can put it back after
    // running the student code, without effecting any code that comes after.
    //
    var normalConsoleLogFunction= console.log;
    scope.console.log= function(val){
      output.push(val);
    }


    //
    // Execute the code the student has provided.
    //
    try {
      vm.runInNewContext(data, scope)

      // 
      // Put back the console.log function to the original
      //
      console.log= normalConsoleLogFunction;

      if(typeof cb == 'function') {
        cb(output, null);
      }
    }
    catch(e) {
      // 
      // Put back the console.log function to the original
      //
      console.log= normalConsoleLogFunction;

      if(typeof cb == 'function') {
        var msg = '';

        var CLIEngine = require("eslint").CLIEngine;

        var cli = new CLIEngine({
            envs: ["browser", "mocha"],
            useEslintrc: false,
            rules: {
                // semi: 2
            }
        });

        var report = cli.executeOnFiles([file]);        // console.log(report);

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
        cb(null, msg);      
      }      
    }

    return output;
  }
}

test.tests = function(script, tasks) {
  async.each(tasks, function(t, cb) {
    test.test(script, t.inputs, function(outputs, err) {
      if(err) return cb(err);

      // First, check for a validate function
      if(t['validate']){
        if(!t.validate(t)){
          cb(t.message || 'Not quite right. Please try again.');
        }
      } else {
        // No validate function, so assume we should just compare outputs

        if(outputs.length != t.outputs.length) {
          if(DEBUG)console.info("FAIL: output count wrong. Was ["+outputs.length+"] Expected ["+t.outputs.length+"]");
          cb(t.message || 'Not quite right please try again.');
        }

        for(var i = 0; i < outputs.length; i++) {
          if(outputs[i] != t.outputs[i]) {
            if(DEBUG)console.info("Fail ["+outputs[i]+"] != ["+t.outputs[i]+"]");
            return cb(t.message || 'Not quite right please try again.');
          } else {
            if(DEBUG)console.info("Good ["+outputs[i]+"] == ["+t.outputs[i]+"]");
          }
        }
      }

      cb(null);
    });
  }, function(err, results) {
    if(err) {
      console.log(err);
      process.exit(1)
    }
    else {
      console.log('Well done!');
      process.exit(0)
    }
  });
}


module.exports = test;
