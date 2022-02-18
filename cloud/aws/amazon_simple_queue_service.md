---
title: Amazon Simple Queue Service
---

## Amazon Simple Queue Service
FIFO cannot be used as a dead letter queue destination.


## Concept
- Visibility timeout
- Message retention period
- Delivery delay
- Maximum message size 
- Receive message wait time
- Content-based deduplication
- Enable high throughput FIFO
    - per queue
    - per message group ID


## Scaling and concurrencies
[Using Lambda with Amazon SQS \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-scaling)

## Message attribute and message system attributes
- https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html#sqs-message-attributes

Message attributes

- Each message can have up to 10 metadata attribute

Message system attributes

message attributes for other AWS services.

## Queue type
* [What Is Amazon Simple Queue Service? \- Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html#sqs-queue-types)

* Standard
    * [Amazon SQS Standard Queues \- Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html)
    * Unlimited throughput
    * at-least-once delivery
    * best-effort ordering
    * Criteria
        * Decouple live user requests from intensive background work: let users upload media while resizing or encoding it.
        * Allocate tasks to multiple worker nodes: process a high number of credit card validation requests.
        * Batch messages for future processing: schedule multiple entries to be added to a database.


* FIFO queue
    * [Amazon SQS FIFO \(First\-In\-First\-Out\) Queues \- Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html)
    * high throughput
        * support up to 3,000 messages per second with batching
        * To request a limit increase, file a support request
        * support up to 300 messages per second (300 send, receive, or delete operations per second) without batching
    * Exactly once delivery
    * FIFO delivery
    * Criteria
        * Ensure that user-entered commands are executed in the right order.
        * Display the correct product price by sending price modifications in the right order.
        * Prevent a student from enrolling in a course before registering for an account.

## Reference
* [What Is Amazon Simple Queue Service? \- Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
