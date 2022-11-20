---
title: Cloud Pub/Sub
---

## Cloud Pub/Sub

## Subscriber
* [Subscriber Overview  |  Cloud Pub/Sub  |  Google Cloud](https://cloud.google.com/pubsub/docs/subscriber)


At-Least-Once Delivery

* at least onceでsubscriberに通知
* 7日のretention timeをこけたmessageは削除される


delivery type

* Pull
    * endpointやserverがpub/subにeventをpullしにいく
* Push
    * [Push Subscriber Guide  |  Cloud Pub/Sub  |  Google Cloud](https://cloud.google.com/pubsub/docs/push#configuring-http-endpoints)
    * Pub/Subがenpoint(http/https)にpushする
    * pushされたendpointは指定された時間までにackを返す
        * 200, 201, 202, 204, 102がsuccess
        * 最大7日retryする

Pull/Push

* Pull
* Large volume of messages (many more than 1/second).
* Efficiency and throughput of message processing is critical.
* Public HTTPs endpoint, with non-self-signed SSL certificate, is not feasible to set up.


## Permissions

* add the writer to your destination topic's permission list
* give the writer the `Pub/Sub Publisher` role

## Reference
