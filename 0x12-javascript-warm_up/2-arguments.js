#!/usr/bin/node
// count the arguments

if (process.argv[2] === undefined) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
