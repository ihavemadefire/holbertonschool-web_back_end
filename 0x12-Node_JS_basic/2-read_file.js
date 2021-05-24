const fs = require('fs');

function countStudents(path) {
  if (!fs.existsSync(path)) {
    throw Error('Cannot load the database');
  }
  const payload = fs.readFileSync(path, 'utf8');
  const students = payload.split('\n')
    .map((student) => student.split(','))
    .filter((student) => student[0] !== 'firstname' && student.length === 4);
  const allCount = students.length;
  const csCount = students.filter((student) => student[3] === 'CS').length;
  const sweCount = students.filter((student) => student[3] === 'SWE').length;
  const csList = students.filter((student) => student[3] === 'CS')
    .map((student) => student[0]).join(', ');
  const sweList = students.filter((student) => student[3] === 'SWE')
    .map((student) => student[0]).join(', ');
  console.log(`Number of students: ${allCount}`);
  console.log(`Number of students in CS: ${csCount}. List: ${csList}`);
  console.log(`Number of students in SWE: ${sweCount}. List: ${sweList}`);
}

module.exports = countStudents;
