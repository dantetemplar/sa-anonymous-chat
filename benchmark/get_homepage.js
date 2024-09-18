import http from 'k6/http';
import {check} from 'k6';
import {Counter} from 'k6/metrics';

export let errorRate = new Counter("errors");

export let options = {
    vus: 50, // Virtual users
    duration: '30s', // Test duration
};

export default function () {
    // Test GET homepage
    let res = http.get('http://localhost:8000/');
    check(res, {
        'status was 200': (r) => r.status === 200,
    }) || errorRate.add(1);
}