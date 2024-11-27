#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id
const request = require('request');
const process = require('process');
// 
const url = process.argv[2];
// The first argument is the API URL:
// https://jsonplaceholder.typicode.com/todos
request(url, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  // const tasks = JSON.parse(body).results;
  const completedTasks = {};

  body.forEach((task) => {
    if (task.completed) {
      const userId = task.userId.toString();
      if (!completedTasks[userId]) {
      completedTasks[userId] = 1;
      } else {
      completedTasks[userId]++;
      }
    }
  });

  Object.keys(completedTasks).forEach(userId => {
    if(completedTasks[userId] === 0) {
      delete completedTasks[userId];
    }
  });

  const sortedKeys = Object.keys(completedTasks).sort((a, b) => parseInt(a) - parseInt(b));

  const output = sortedKeys.map(userId => `'${userId}': ${completedTasks[userId]}`).join(',\n');
  console.log(`{ ${output} }`);
});
