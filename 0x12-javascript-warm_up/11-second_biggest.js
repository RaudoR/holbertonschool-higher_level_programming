#!/usr/bin/node
function secondhighest () {
  if (process.argv.length <= 2) {
    return 0;
  } else if (process.argv.length === 3) {
    return 0;
  }
  const args = [];
  for (let cnt = 2; cnt < process.argv.length; cnt++) {
    args.push(parseInt(process.argv[cnt]));
  }
  return args.sort()[process.argv.length - 4];
}

console.log(secondhighest());
