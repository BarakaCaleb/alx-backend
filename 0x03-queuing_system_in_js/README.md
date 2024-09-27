# 0x03. Queuing System in JS

## Introduction

In this project, I delved into the integration of Redis with a Node.js backend to build a queuing system. My primary focus was to learn how to effectively utilize Redis as a data store and queue management system while leveraging the power of modern JavaScript (ES6) and Node.js technologies like Express.js and Kue. I aimed to gain hands-on experience with Redis operations, both synchronous and asynchronous, and to explore the creation of a basic yet functional queuing system using Kue. This README provides a detailed walkthrough of how I approached and implemented the tasks outlined in the project.

## Project Structure

The project is organized into several key files, each handling different aspects of Redis operations and queue management:

- **package.json**: Manages project dependencies and scripts.
- **.babelrc**: Configures Babel for transpiling ES6 code.
- **dump.rdb**: Redis database dump file.
- **0-redis_client.js**: Handles Redis client connection.
- **1-redis_op.js**: Implements basic Redis operations using callbacks.
- **2-redis_op_async.js**: Enhances Redis operations using async/await with Promises.
- **4-redis_advanced_op.js**: Manages advanced Redis operations like storing and retrieving hash values.
- **5-subscriber.js**: Implements a Redis client that subscribes to a Redis channel.
- **5-publisher.js**: Publishes messages to a Redis channel.

## Setting Up Redis

### 1. Installing and Configuring Redis

I began by installing Redis on my local machine. The process involved downloading, extracting, and compiling the latest stable version of Redis (version 6.0.10). After compiling, I started the Redis server in the background and verified its functionality by running a few basic commands such as `PING`, `SET`, and `GET`.

```bash
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
$ src/redis-server &
```

### 2. Running Redis Operations

With the Redis server up and running, I tested basic Redis operations. For instance, I stored the value "School" under the key "Holberton" and retrieved it to confirm everything was working as expected.

```bash
127.0.0.1:6379> SET Holberton School
OK
127.0.0.1:6379> GET Holberton
"School"
```

## Node.js Integration with Redis

### 1. Connecting to Redis from Node.js

I implemented a simple Redis client using Node.js. The script (`0-redis_client.js`) connects to the Redis server and logs a message indicating whether the connection was successful or not. This was my first step toward integrating Redis with a Node.js backend.

```javascript
import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log('Redis client not connected to the server: ', err.message);
});
```

### 2. Basic Redis Operations

Next, I extended the Redis client to perform basic operations. In the `1-redis_op.js` file, I wrote functions to set a new key-value pair in Redis (`setNewSchool`) and retrieve the value associated with a key (`displaySchoolValue`). This allowed me to explore Redis' callback-based API.

```javascript
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        console.log(reply);
    });
}
```

### 3. Async Redis Operations

To modernize the Redis operations, I refactored the previous code to use async/await syntax by leveraging the `promisify` utility from the `util` module. This approach was implemented in the `2-redis_op_async.js` file, where the `displaySchoolValue` function was made asynchronous, allowing me to handle Redis operations more cleanly and effectively.

```javascript
import { promisify } from 'util';

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    const value = await getAsync(schoolName);
    console.log(value);
}
```

### 4. Advanced Redis Operations

In the `4-redis_advanced_op.js` file, I explored more advanced Redis operations by working with hashes. I used the `hset` and `hgetall` commands to store and retrieve structured data in Redis, specifically a hash containing different cities and their corresponding values.

```javascript
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

client.hgetall('HolbertonSchools', (err, object) => {
    console.log(object);
});
```

## Implementing a Queuing System

### 1. Setting Up Kue

Kue is a priority job queue backed by Redis that allows you to manage job queues in Node.js. Although it's deprecated, it's still widely used in the industry. I installed Kue and set up a basic queuing system where jobs could be created and processed.

```bash
$ npm install kue
```

### 2. Creating and Processing Jobs

In the Kue setup, I created jobs that were added to the queue and processed asynchronously. This was done by defining the job type, setting its data, and specifying how it should be processed when dequeued.

```javascript
import kue from 'kue';

const queue = kue.createQueue();

queue.process('email', (job, done) => {
    console.log('Processing job:', job.data);
    done();
});

const job = queue.create('email', {
    title: 'Welcome Email',
    to: 'user@example.com'
}).save((err) => {
    if (!err) console.log('Job saved:', job.id);
});
```

## Pub/Sub with Redis

### 1. Implementing a Subscriber

In the `5-subscriber.js` file, I set up a Redis client that subscribes to a specific channel (`holberton school channel`). The client listens for messages on this channel and logs them to the console. If the message is `KILL_SERVER`, the client unsubscribes and exits.

```javascript
client.on('message', (channel, message) => {
    console.log(`Received message: ${message} on channel: ${channel}`);
    if (message === 'KILL_SERVER') {
        client.unsubscribe(channel);
        client.quit();
    }
});
client.subscribe('holberton school channel');
```

### 2. Implementing a Publisher

The `5-publisher.js` file handles the publishing of messages to the Redis channel. It logs when it's connected to the Redis server and sends messages to the channel at regular intervals.

```javascript
function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        client.publish('holberton school channel', message);
    }, time);
}
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
```

## Conclusion

This project was a comprehensive exercise in integrating Redis with a Node.js backend. I gained valuable experience working with Redis for both basic and advanced operations, asynchronous programming in JavaScript, and implementing a simple queuing system using Kue. Additionally, I explored the pub/sub pattern with Redis, further solidifying my understanding of Redis as a versatile and powerful tool in backend development. The knowledge and skills acquired in this project will undoubtedly be beneficial in future projects involving real-time data processing and queue management.

---

Feel free to explore the code and experiment with different Redis operations. If you have any questions or need further clarification, don't hesitate to reach out.