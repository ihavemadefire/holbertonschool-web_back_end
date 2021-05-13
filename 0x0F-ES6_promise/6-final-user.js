import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then(
      (res) => {
        const ret = [];
        for (const i of res) {
          if (i.status === 'fulfilled') {
            ret.push({
              status: i.status,
              value: i.value,
            });
          } else {
            ret.push({
              status: i.status,
              value: `Error: ${i.reason.message}`,
            });
          }
        }

        return ret;
      },
    );
}
