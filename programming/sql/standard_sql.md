## standards SQL

## Bigquery
* [Functions & Operators  |  BigQuery Documentation  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators)

### Extract
UTC+0からJSTに変更する場合は以下で良い。

```sql
SELECT
    EXTRACT(DATETIME FROM TIMESTAMP "2008-12-25 15:30:00" AT TIME ZONE "Asia/Tokyo")
```

`TIMESTAMP "2008-12-25 15:30:00"`の部分は、TIMESTAMP型のcolumn_nameに変更できる。


## widnow function
* [Rows between unbounded preceding](http://www.dba-oracle.com/t_advanced_sql_windowing_clause.htm)

`rows between unbounded preceding`


```sql
SELECT
   ENAME,
   HIREDATE,
   SAL,
   # orderby でSALを並び替えた時に、現在の行の[start, SAL-1]まででMAX
   # HIREDATEが自分より先の中でSALの最大
   MAX(SAL) OVER (
      ORDER BY 
         HIREDATE, 
         ENAME 
      ROWS BETWEEN 
         UNBOUNDED PRECEDING 
         AND 
         1 PRECEDING
   ) MAX_BEFORE, 
   # orderby でSALを並び替えた時に、現在の行の[SAL+1, end]まででMAX
   # HIREDATEが自分より後の中でSALの最大
   MAX(SAL) OVER (
      ORDER BY 
         HIREDATE, 
         ENAME 
      ROWS BETWEEN 
         1 FOLLOWING 
         AND 
         UNBOUNDED FOLLOWING
   ) MAX_AFTER
FROM
   EMP
ORDER BY 
   HIREDATE, 
   ENAME;

ENAME      HIREDATE         SAL MAX_BEFORE  MAX_AFTER
---------- --------- ---------- ---------- ----------
SMITH      17-DEC-80        800                  5000
ALLEN      20-FEB-81       1600        800       5000
WARD       22-FEB-81       1250       1600       5000
JONES      02-APR-81       2975       1600       5000
BLAKE      01-MAY-81       2850       2975       5000
CLARK      09-JUN-81       2450       2975       5000
TURNER     08-SEP-81       1500       2975       5000
MARTIN     28-SEP-81       1250       2975       5000
KING       17-NOV-81       5000       2975       3000
FORD       03-DEC-81       3000       5000       3000
JAMES      03-DEC-81        950       5000       3000
MILLER     23-JAN-82       1300       5000       3000
SCOTT      19-APR-87       3000       5000       1100
ADAMS      23-MAY-87       1100       5000
```


