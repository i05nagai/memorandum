---
title: awssdk
---

## awssdk


## Dynamodb
https://github.com/aws/aws-sdk-java-v2

PutItem

- If key is primary key, it cannot be null and empty string
- `s`
    - cannot be null
    - can be empty string
- `n`
    - cannot be null
    - cannot be empty string
    - the value must be convertible to numeric value

```
import java.util.HashMap;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.PutItemRequest;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;

import java.util.HashMap;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        DynamoDbClient client = DynamoDbClient
                .builder()
                .region(Region.of("eu-west-1"))
                .build();

        Map<String, AttributeValue> item = new HashMap<>();

        item.put("s", AttributeValue.builder().s("<string>").build());
        item.put("n", AttributeValue.builder().n("<numeric-value>").build());

        PutItemRequest d = PutItemRequest.builder().tableName("<table-name>").item(item).build();
        client.putItem(d);
    }
}
```


Error

Provide non-convertible string to `n`

```
Exception in thread "main" software.amazon.awssdk.services.dynamodb.model.DynamoDbException: The parameter cannot be converted to a numeric value: a (Service: DynamoDb, Status Code: 400, 
```

```
Exception in thread "main" software.amazon.awssdk.services.dynamodb.model.DynamoDbException: The parameter cannot be converted to a numeric value: a (Service: DynamoDb, Status Code: 400, 
```


## Reference
