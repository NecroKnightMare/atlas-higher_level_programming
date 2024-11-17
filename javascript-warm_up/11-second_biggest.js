#!/usr/bin/node
// find and print secong largest integer
function secondLargestElement () {
  let largest = Infinity;
  let second = Infinity;

  for (let i = 0; i < arguments.length; i++) {
    if (args[i] > largest) {
        second = largest;
        largest = args[i];
        console.log(second);
    } else if (args[i] > second && args[i] !== largest) {
        second = args[i];
        console.log(second);
    } else if (args[i] === 1) {
        console.log(0);
    } else {
        console.log(0);
    }
  }
}
