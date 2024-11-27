#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id
const request = require('request');
// 
const url = process.argv[2];
// The first argument is the API URL:
// https://jsonplaceholder.typicode.com/todos
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  try {
    const tasks = JSON.parse(body).results;
    const completedTasks = {};

    tasks.forEach((task) => {
      if (task.completed) {
        if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
        } else {
        completedTasks[task.userId] = 1;
        }
      }
    });
    console.log(completedTasks);
  } catch (e) {
    console.error(e);
  }
});
