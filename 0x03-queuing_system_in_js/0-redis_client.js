// Import the redis package using ES6 syntax
import redis from 'redis';

// Create a Redis client
const client = redis.createClient({
  host: '127.0.0.1', // Default Redis host
  port: 6379         // Default Redis port
});

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for error
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});
