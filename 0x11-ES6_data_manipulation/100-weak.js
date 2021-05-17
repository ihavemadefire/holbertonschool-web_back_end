export const weakMap = new WeakMap();
export function queryAPI(endpoint) {
  // if passed endpoint has not been called set its value to zero
  if (!weakMap.has(endpoint)) {
    weakMap.set(endpoint, 0);
  }
  // increment enpoint ping count
  weakMap.set(endpoint, weakMap.get(endpoint) + 1);
  // high traffic condition
  if (weakMap.get(endpoint) >= 5) throw Error('Endpoint load is high');
}
