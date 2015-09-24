
var vm = require('vm');
var fs = require('fs');
var async = require('async');

var test = {
  test: function(file, argv, cb) {
    var data = fs.readFileSync(file);
    var input = [];
    var output = [];

    var scope = {
      output: function(val) {
        output.push(val);
      },
      require: require,
      console: {
        log: console.log.bind(console)
      }      
    }

    for (var i = 0; i < argv.length; i++) {
      input.push({ i: 0, val: argv[i]});
      
      (function(n) {
        Object.defineProperty(scope, 'input' + n, {
          get: function() {
            return input[n].val
          },
          set: function(val) {
            if(input[n].i++ > 0) {
              input[n].val = val
            }
          }
        });
      })(i);

    }

    try {
      vm.runInNewContext(data, scope)

      if(typeof cb == 'function') {
        cb(output, null);
      }
    }
    catch(e) {
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
      console.log(outputs)
      
      if(err) return cb(err);
      if(outputs.length != t.outputs.length) cb(t.message || 'Not quite right please try again.');
      
      for(var i = 0; i < outputs.length; i++) {
        
        if(Array.isArray(outputs[i]) && Array.isArray(t.outputs[i]) && outputs[i].length == t.outputs[i].length) {          
           for(var j = 0; j < outputs[i].length; j++) {
             if(outputs[i][j] != t.outputs[i][j]) {
               return cb(t.message || 'Not quite right please try again.');
             }
           }
        }
        else if(outputs[i] != t.outputs[i]) {
          return cb(t.message || 'Not quite right please try again.');
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
