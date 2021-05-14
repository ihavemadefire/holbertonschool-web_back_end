export default class Currency {
  constructor(name, code) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof code !== 'string') throw TypeError('Code must be a string');
    this._name = name;
    this._code = code;
  }

  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }

  set name(anotherName) {
    if (typeof anotherName !== 'string') throw TypeError('Name must be a string');
    this._name = anotherName;
  }

  set code(anotherCode) {
    if (typeof anotherCode !== 'string') throw TypeError('Code must be a string');
    this._name = anotherCode;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
