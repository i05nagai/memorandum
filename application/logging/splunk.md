---
title: splunk
---

## splunk


## Rest API
- HTTP Event Collector
    - running on Forworder
    - [Set up and use HTTP Event Collector in Splunk Web \- Splunk Documentation](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector)


API Reference

[Input endpoint descriptions \- Splunk Documentation](https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTinput#services.2Fcollector)

Example

```
curl -k  https://hec.example.com:8088/services/collector/event -H "Authorization: Splunk B5A79AAD-D822-46CC-80D1-819F80D7BFB0" -d '{"event": "hello world"}'
{"text": "Success", "code": 0}
```


Format of event data

[Format events \| HTTP Event Collector](http://dev.splunk.com/view/event-collector/SP-CAAAE6P)

Available metadata

* `time`
    * The event time. The default time format is epoch time format, in the format <sec>.<ms>. For example, 1433188255.500 indicates 1433188255 seconds and 500 milliseconds after epoch, or Monday, June 1, 2015, at 7:50:55 PM GMT.
* `host`
    * The host value to assign to the event data. This is typically the hostname of the client from which you're sending data.
* `source`
    * The source value to assign to the event data. For example, if you're sending data from an app you're developing, you could set this key to the name of the app.
* `sourcetype`
    * The sourcetype value to assign to the event data.
* `index`
    * The name of the index by which the event data is to be indexed. The index you specify here must within the list of allowed indexes if the token has the indexes parameter set.
* `fields`
    * (Not applicable to raw data.) Specifies a JSON object that contains explicit custom fields to be defined at index time. Requests containing the "fields" property must be sent to the /collector/event endpoint, or they will not be indexed. For more information, see Indexed field extractions.

Examples

```
{
    "time": 1426279439, // epoch time
    "host": "localhost",
    "source": "datasource",
    "sourcetype": "txt",
    "index": "main",
    "event": { "Hello world!" }
}
```

## CLI

## Usage

## Configuration

- frozenTimePeriodInSecs
    - how long data is kept before being deleted, in seconds.

## Reference
