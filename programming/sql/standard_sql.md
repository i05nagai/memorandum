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

## Function
* [Functions & Operators  |  BigQuery  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#supported-format-elements-for-date)
* [Functions & Operators  |  BigQuery  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#supported-format-elements-for-datetime)

```sql
FORMAT_DATE('%U', DATE '2013-12-25')
FORMAT_DATETIME("%c", DATETIME "2008-12-25 15:30:00")
FORMAT_DATETIME('%Y-%m-%d', DATETIME "2008-12-25 15:30:00")
FORMAT_TIMESTAMP('%Y-%m-%d', TIMESTAMP "2008-12-25 15:30:00")
```

* `%U`
    * week number of the year 0-53
* `%a`
    * abbreviated weekday name
* `%u`
    * weekday number 1-7
* `%D`
    * `%m/%d/%y`
* `%m`
    * 
* `%d`
    * 日
* `%Y`
* `%H`
    * hours
    * 00-23
* `%M`
    * minutes
    * 00-59
* `%S`
    * second
    * 00-59
* `%T`
    * `%H:%M:%S`
* `%`

## UDF
standard SQLとlegacy SQLで定義方法や扱いが異なる。

### Standard SQL
* [User-Defined Functions  |  BigQuery  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions)

standard SQLで外部JSのUDFは利用できない。
standard SQLでUDFを使う場合は以下の形式で使う。

```sql
CREATE TEMPORARY FUNCTION nullToZero(x Integer)
RETURNS FLOAT64
LANGUAGE js AS """
  if (x === null) {
    return 0;
  }
  return x;
"""
;
```

languageはSQLも使える。

```sql
#standardSQL
-- Computes the harmonic mean of the elements in 'arr'.
-- The harmonic mean of x_1, x_2, ..., x_n can be expressed as:
--   n / ((1 / x_1) + (1 / x_2) + ... + (1 / x_n))
CREATE TEMPORARY FUNCTION HarmonicMean(arr ARRAY<FLOAT64>) AS
(
  ARRAY_LENGTH(arr) / (SELECT SUM(1 / x) FROM UNNEST(arr) AS x)
);

WITH T AS (
  SELECT GENERATE_ARRAY(1.0, x * 4, x) AS arr
  FROM UNNEST([1, 2, 3, 4, 5]) AS x
)
SELECT arr, HarmonicMean(arr) AS h_mean
FROM T;
```

optionsで外部のUDFを読み込めるがJSのUDFのみ。

```sql
OPTIONS (
  library="gs://my-bucket/path/to/lib1.js",
  library=["gs://my-bucket/path/to/lib2.js", "gs://my-bucket/path/to/lib3.js"]
);
```

javascript UDFのBest Practice

* JSのUDFに渡す前に、SQLで入力をfilterした方が安く早い
    * JSのUDFは遅い
* JSのUDFにstateを持たせない
* JSのUDFが利用できるmemoryは限られているので、UDF内のmemory使用には気をつける

## Types
* [Data Types  |  BigQuery  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types)

* INT64
* FLOAT64
* BOOL
* STRING
