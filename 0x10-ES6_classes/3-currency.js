export default class Currency {
  constructor(code, name) {
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
    this._name = anotherName;
  }

  set code(anotherCode) {
    this._code = anotherCode;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`
  }
}
