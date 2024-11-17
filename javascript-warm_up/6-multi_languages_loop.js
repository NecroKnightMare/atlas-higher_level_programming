#!/usr/bin/node
// prints array of strings in order with while loop
// will increment to avoid infinite loop
const arg = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let index = 0;
while (index < arg.length) {
  console.log(arg[index]);
  index++;
}
