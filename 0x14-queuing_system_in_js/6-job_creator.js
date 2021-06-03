import kue from 'kue';

const queue = kue.createQueue();

const payload = {
    phoneNumber: '9189080733',
    message: 'Please dear Dod, I just want a job',
};

const job = queue.create('push_notification_code', payload).save(
    (err) => {
        if (!err) console.log(`Notification job created: ${job.id}`);
    });

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
