export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  const ret = students.map((x) => x.id).reduce((total, amount) => total + amount);
  return ret;
}
