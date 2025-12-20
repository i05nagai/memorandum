---
title: Change Data Capture
---

## Change Data Capture

## RDB

### Timestamp/Version Column Polling

The idea is simple: each row in the table has a monotonically increasing timestamp (or version number).

```ddl
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT,
    amount DECIMAL(10, 2),
    status VARCHAR(50),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Trigger-based CDC

```ddl
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE customer_changes (
    change_id SERIAL PRIMARY KEY,
    customer_id INT,
    change_type CHAR(1), -- 'I' = Insert, 'U' = Update, 'D' = Delete
    change_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_by VARCHAR(255),
    old_name VARCHAR(255),
    old_email VARCHAR(255),
    new_name VARCHAR(255),
    new_email VARCHAR(255)
);
```

### history table

```ddl
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE customer_history (
    history_id SERIAL PRIMARY KEY,
    customer_id SERIAL,
    name VARCHAR(255),
    email VARCHAR(255),
    start_at TIMESTAMP,
    end_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);
```

```
SELECT * FROM customer_history
WHERE customer_id = 101 AND end_at IS NULL;
```

```
SELECT * FROM customer_history
WHERE customer_id = 101
AND start_at <= '2025-06-01 12:00:00'
AND (end_at IS NULL OR start_at > '2025-06-01 12:00:00');
```


## Reference
