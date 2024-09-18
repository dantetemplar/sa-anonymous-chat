# Benchmarking

This directory contains scripts and configurations for benchmarking the application.


## How to run benchmarks

1. Run the application
2. Install [k6](https://grafana.com/docs/k6/latest/set-up/install-k6/)
3. Run the benchmark script
    ```bash
    k6 run <benchmark_script>.js
    ```
4. Check the results in the console output

## Supported benchmarks

[GET /messages](get_all_messages.js) - benchmark getting 1000 messages
  ```bash
  k6 run get_all_messages.js
  ```
[GET /messages/count](get_messages_count.js) - benchmark getting messages count for 1000 messages
  ```bash
  k6 run get_messages_count.js
  ```
[POST /messages](post_message.js) - benchmark posting 10 messages to the server
  ```bash
  k6 run post_message.js
  ```
[GET /](get_homepage.js) - benchmark getting the homepage
  ```bash
  k6 run get_homepage.js
  ```

## Speed up API

Run with granian and more workers:
```bash
granian --opt --workers 8 --interface asgi src.api.app:app
```