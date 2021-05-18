export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  let ret = [];
  ret = students.map((x) => x.id);
  return ret;
}
