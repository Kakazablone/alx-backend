import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    // Create a new queue instance
    queue = kue.createQueue();
    // Enter test mode
    queue.testMode.enter();
  });

  afterEach((done) => {
    // Clear the queue after each test
    queue.testMode.clear(done);
  });

  after(() => {
    // Exit test mode after all tests
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should create two new jobs in the queue', (done) => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Check the jobs in the queue
    const queuedJobs = queue.testMode.jobs;

    // Validate the number of jobs created
    expect(queuedJobs).to.have.lengthOf(2);
    expect(queuedJobs[0].data.phoneNumber).to.equal('4153518780');
    expect(queuedJobs[1].data.phoneNumber).to.equal('4153518781');

    done();
  });
});
