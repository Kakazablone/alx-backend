const kue = require('kue');
const queue = kue.createQueue();

// Create job data
const jobData = {
  phoneNumber: '123-456-7890',
  message: 'Hello, this is a test message!',
};

// Create a job in the queue
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Listen for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Listen for job failure
job.on('failed', (errorMessage) => {
  console.log('Notification job failed:', errorMessage);
});
