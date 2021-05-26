const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe('calculateNumber', function () {
    it('1 + 3 should round to 4', function () {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });
    it('1 + 3.9 round to 5', function () {
      assert.strictEqual(calculateNumber(1, 3.9), 5);
    });
    it('3.7 + 1.2 = 5', function () {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });
    it('1.5 + 3.7 = 5', function () {
      assert.strictEqual(calculateNumber(1.5, 3.7), 5);
    });
  });
  