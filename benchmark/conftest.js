import {randomString} from 'https://jslib.k6.io/k6-utils/1.1.0/index.js';
import http from 'k6/http';
import {check} from 'k6';


// Prepare stage: Send 1000 random messages
export function send1000Messages() {
    // delete all messages
    http.del('http://localhost:8000/api/messages');

    // get from env
    const messageCount = __ENV.MESSAGE_COUNT || 1000;

    for (let i = 0; i < messageCount; i++) {
        let payload = {
            message: randomString(10), // Generate a random 10-character message
        };
        let res = http.post('http://localhost:8000/api/messages', payload, {
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        });
        check(res, {
            'status was 200': (r) => r.status === 200,
        });
    }
}
