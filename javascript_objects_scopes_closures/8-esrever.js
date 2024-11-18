#!/usr/bin/node
// returns list in reverse
exports.esrever = function (list) {
  const rev_list = [];
  for (let i = list.length - 1; i >= 0; i--) {
    rev_list.push(list[i]);
  }
  return rev_list;
};
