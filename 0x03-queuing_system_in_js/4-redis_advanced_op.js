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

// Step 2: Storing Hash Values
// Store values using the hset method
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Step 3: Display Hash Values
// Retrieve all values of the hash using hgetall
client.hgetall('HolbertonSchools', (err, result) => {
  if (err) {
    console.error('Error retrieving hash values:', err);
  } else {
    console.log(result); // Display the retrieved hash values
  }
});
