import redis from 'redis'
const client = redis.createClient();

client.on("error", function(error) {
    console.error(`Redis client not connected to the server: ${error}`);
});
  
client.on("connect", function() {
    console.log('Redis client connected to the server');
});
  
client.subscribe('holberton school channel');

client.on('message', function(channel, message) {
    console.log(message);

    if (message === 'KILL_SERVER') {
        client.unsubscribe(channel);
        client.quit();
    }
});
