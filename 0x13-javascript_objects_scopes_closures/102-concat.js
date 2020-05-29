#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');
const textA = fs.readFileSync('./' + args[0]);
const textB = fs.readFileSync('./' + args[1]);
fs.writeFileSync('./' + args[2], textA + textB);
