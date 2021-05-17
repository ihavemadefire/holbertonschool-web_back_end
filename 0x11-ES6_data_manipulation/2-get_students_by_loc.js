export default function getStudentsByLocation(students, city) {
  if (!Array.isArray(students)) {
    return [];
  }
  let arr = [];
  arr = students.filter((x) => x.location === city);
  return arr;
}
