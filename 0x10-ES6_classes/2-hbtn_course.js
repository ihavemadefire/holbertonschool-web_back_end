export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof length !== 'number') throw TypeError('Length must be a number');
    if (!Array.isArray(students)) throw TypeError('Students must be an array');
    this._name = name;
    this._length = length;
    this._student = students;
  }

  get name() {
    return this._name;
  }

  set name(anotherName) {
    if (typeof anotherName !== 'string') throw TypeError('Name must be a string');
    this._name = anotherName;
  }

  get length() {
    return this._length;
  }
  
  set length(anotherLength) {
    if (typeof anotherLength !== 'number') throw TypeError('Length must be a number');
    this._length = anotherLength;
  }

  get students() {
    return this._students;
  }

  set students(moreStudents) {
    if (!Array.isArray(moreStudents)) throw TypeError('Students must be an array');
    this._students = moreStudents;
  }
}
