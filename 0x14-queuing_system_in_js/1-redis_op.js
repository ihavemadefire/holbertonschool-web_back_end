import redis from 'redis'
const client = redis.createClient();

client.on("error", function(error) {
  console.error(`Redis client not connected to the server: ${error}`);
});

client.on("connect", function() {
    console.log('Redis client connected to the server');
  });

const setNewSchool = (schoolName, value)  => client.set(schoolName, value, redis.print);
const displaySchoolValue = (schoolName) => client.get(schoolName, function(error, res) {
    console.log(res);
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
