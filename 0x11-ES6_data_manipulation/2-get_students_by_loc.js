export default function getStudentsByLocation(students, city) {
  if (!Array.isArray(students)) {
    return [];
  }
  let ret = [];
  ret = students.filter((x) => x.location === city);
  return ret;
}
