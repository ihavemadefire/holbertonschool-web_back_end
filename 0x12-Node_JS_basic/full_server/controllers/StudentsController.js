import readDatabase from '../utils';

const databasePath = process.argv[2];

class StudentsController {
  static getAllStudents(request, response) {
    response.status(200);
    response.set('Content-Type', 'text/plain');
    readDatabase(databasePath)
      .then((x) => {
        response.write('This is the list of our students\n');
        response.write(`Number of students in CS: ${x.csCount}. List: ${x.csList}\n`);
        response.write(`Number of students in SWE: ${x.sweCount}. List: ${x.sweList}`);
        response.end();
      })
      .catch((err) => {
        response.status(500);
        response.send(err.message);
      });
  }

  static getAllStudentsByMajor(request, response) {
    response.status(200);
    response.set('Content-Type', 'text/plain');
    readDatabase(databasePath)
      .then((x) => {
        const { major } = request.params;
        if (major === 'CS') response.send(`List: ${x.csList}`);
        else if (major === 'SWE') response.send(`List: ${x.sweList}`);
        else {
          response.status(500);
          response.send('Major parameter must be CS or SWE');
        }
      })
      .catch((err) => {
        response.status(500);
        response.send(err.message);
      });
  }
}

module.exports = StudentsController;
