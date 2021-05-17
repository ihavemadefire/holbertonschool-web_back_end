export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  let arr = [];
  arr = students.map((x) => x.id);
  return arr;
}
