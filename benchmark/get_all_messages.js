import http from 'k6/http';
import {check} from 'k6';
import {Counter} from 'k6/metrics';
import {send1000Messages} from './conftest.js';

export let errorRate = new Counter("errors");

export let options = {
    vus: 50, // Virtual users
    duration: '30s', // Test duration
};

// Prepare stage: Send 1000 random messages
export function setup() {
    send1000Messages();
}

export default function () {
    // Test GET all messages
    let res = http.get('http://localhost:8000/api/messages');
    check(res, {
        'status was 200': (r) => r.status === 200,
    }) || errorRate.add(1);
}
