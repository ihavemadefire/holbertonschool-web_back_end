export default (employeesList) => {
  const allEmployees = employeesList;
  const getNumberOfDepartments = (obj) => Object.keys(obj).length;
  return { allEmployees, getNumberOfDepartments };
};
