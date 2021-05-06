export default function appendToEachArrayValue(array, appendString) {
  const array2 = [];
  for (const i of array) {
    array2.push(`${appendString}${i}`);
  }

  return array2;
}
