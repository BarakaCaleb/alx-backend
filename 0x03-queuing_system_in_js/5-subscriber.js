import redis from 'redis';

const client = redis.createClient();

client
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', err => console.log(`Redis client not connected to the server: ${err}`));

const subscriber = client.duplicate();

subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    process.exit();
  }
})

subscriber.subscribe('holberton school channel');
