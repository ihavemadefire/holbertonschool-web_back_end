export default function appendToEachArrayValue(array, appendString) {
  const array_2 = []
  for (const i of array) {
    const value = array[idx];
    array_2.push(`${appendString}${i}`)
  }

  return array;
}
