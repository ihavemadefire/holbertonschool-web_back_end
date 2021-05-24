const fs = require('fs');

async function countStudents(path) {
  let payload;
  try {
    payload = await fs.promises.readFile(path, 'utf8');
  } catch (error) {
    throw Error('Cannot load the database');
  }
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
  return {
    allCount, csCount, sweCount, csList, sweList,
  };
}

module.exports = countStudents;
