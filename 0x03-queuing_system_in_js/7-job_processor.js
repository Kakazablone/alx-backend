const kue = require('kue');
const queue = kue.createQueue();

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
  // Track job progress
  job.progress(0, 100);

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job with an error
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // If not blacklisted, proceed with sending notification
  job.progress(50);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Simulate sending notification (asynchronous task)
  setTimeout(() => {
    // Mark job as complete
    done();
  }, 1000); // Simulate a delay of 1 second
}

// Process jobs in the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
