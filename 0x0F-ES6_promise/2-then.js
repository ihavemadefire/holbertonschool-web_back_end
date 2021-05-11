export default function getResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({
        status: 200,
        body: 'Success',
      });
    } else {
      reject(Error());
    }
  }).then(() => console.log('Got a response from the API'));
}
