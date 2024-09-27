import kue from 'kue';

const queue = kue.createQueue();
const jobData = {
  phoneNumber: '+210123',
  message: 'First queue',
};

const job = queue.create('push_notification_code', jobData);
job.save(err => {
  if (err) {
    console.log('Notification job failed');
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
})

job.on('complete', () => console.log('Notification job completed'));
