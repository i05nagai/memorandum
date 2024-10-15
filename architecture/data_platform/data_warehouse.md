---
title: Data Warehouse
---

## Data Warehouse


## Design
https://www.zentut.com/data-warehouse/kimball-and-inmon-data-warehouse-architectures/#:~:text=Kimball%20uses%20the%20dimensional%20model,uses%20it%20for%20all%20data
https://en.wikipedia.org/wiki/Star_schema

- Kimball
    - Use dimensional model like star schema or snowflake schema
- Inmon
    - 
- Star schema
    - Diemnsional table
        - Dimension tables usually have a relatively small number of records compared to fact tables, but each record may have a very large number of attributes to describe the fact data
        - for instance
            - Transaction fact table
            - Snapshot fact table (account details at month end)
            - Accumulating snapshot tables record aggregate facts at a given point in time 
    - Fact table
        - Fact table refers to dimensional table with foreign key
        - for example
            - Time dimension
            - Geography dimension
            - Product dimension
            - Employee dimension
    - Benefits
        - Simpler queries
        - Simplified business reporting logic
        - Query performance gains
        - Fast aggregations
        - Feeding cubes
- snowflake schema
    - https://en.wikipedia.org/wiki/Snowflake_schema
    - https://www.geeksforgeeks.org/snowflake-schema-in-data-warehouse-model/
- data mesh

## Reference
