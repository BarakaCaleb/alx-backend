// Import the required packages using ES6 syntax
import redis from 'redis';
import { promisify } from 'util'; // Import promisify from the util module

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

// Function to set a new value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print); // redis.print will log 'Reply: OK'
}

// Promisify the get method to use it with async/await
const getAsync = promisify(client.get).bind(client);

// Function to display the value of a given key using async/await
async function displaySchoolValue(schoolName) {
  try {
    const result = await getAsync(schoolName);
    console.log(result); // Log the value to the console
  } catch (error) {
    console.error(`Error retrieving value for ${schoolName}:`, error);
  }
}

// Call the functions as required
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
