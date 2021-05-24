const http = require('http');
const countStudents = require('./3-read_file_async');

const databasePath = process.argv[2];

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  if (req.method === 'GET') {
    if (req.url === '/') {
      res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
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
    }
  }
}).listen(1245);

module.exports = app;
