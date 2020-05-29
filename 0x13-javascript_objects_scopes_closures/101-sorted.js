#!/usr/bin/node
const data = require('./101-data.js').dict;
const ndict = {};
for (const k in data) {
  ndict[data[k]] = [];
}
for (const key in ndict) {
  for (const k in data) {
    if (String(data[k]) === String(key)) {
      ndict[key].push(k);
    }
  }
}
console.log(ndict);
