// Load the fs library.
var fs = require('fs')

// Load our command line arguments
var P= process.argv[2]

// Read in the data from our file
var data = fs.readFileSync(P, 'utf8')

