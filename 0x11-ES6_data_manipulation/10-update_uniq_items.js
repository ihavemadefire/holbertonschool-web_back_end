export default function updateUniqueItems(snaxx) {
  if (!(snaxx instanceof Map)) throw TypeError('Cannot process');

  for (const i of snaxx) {
    if (i[1] === 1) {
      snaxx.set(i[0], 100);
    }
  }
}
