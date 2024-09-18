import http from 'k6/http';
import {check} from 'k6';
import {Counter} from 'k6/metrics';
import {randomString} from 'https://jslib.k6.io/k6-utils/1.1.0/index.js';

export let errorRate = new Counter("errors");

export let options = {
    vus: 50, // Virtual users
    duration: '30s', // Test duration
};

export default function () {
    // Test POST a message
    const messageCount = __ENV.MESSAGE_COUNT || 10;

    for (let i = 0; i < messageCount; i++) {
        const payload = {
            message: randomString(10), // Generate a random 10-character message
        };
        const res = http.post('http://localhost:8000/api/messages', payload, {
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        });
        check(res, {
            'status was 200': (r) => r.status === 200,
        } || errorRate.add(1));
    }
}

// Tear down stage: Delete all messages
export function teardown() {
    http.del('http://localhost:8000/api/messages');
}