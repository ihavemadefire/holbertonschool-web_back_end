const express = require('express');
const countStudents = require('./3-read_file_async');

const databasePath = process.argv[2];

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});
app.get('/students', async (req, res) => {
  await countStudents(databasePath)
    .then((x) => {
      res.write('This is the list of our students\n');
      res.write(`Number of students: ${x.allCount}\n`);
      res.write(`Number of students in CS: ${x.csCount}. List: ${x.csList}\n`);
      res.write(`Number of students in SWE: ${x.sweCount}. List: ${x.sweList}\n`);
      res.end();
    })
    .catch((err) => {
      res.write('This is the list of our students\n');
      res.end(err.message);
    });
});
app.listen(1245);
module.exports = app;
