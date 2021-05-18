export default function cleanSet(set, startString) {
  if (typeof startString === 'string' && startString !== '') {
    const ret = [];
    for (const i of set) {
      if (i.startsWith(startString)) {
        ret.push(i.slice(startString.length));
      }
    }
    return ret.join('-');
  }
  return '';
}