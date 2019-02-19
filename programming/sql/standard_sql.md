---
title: Standard SQL
---

## standards SQL

## Bigquery
* [Functions & Operators  |  BigQuery Documentation  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators)

#### Extract
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
* `APPROX_QUANTILES([DISTINCT] expression, number [{IGNORE|RESPECT} NULLS])`
    * expressionが集計対象
    * numberはnumber of quantiles, 分位点
    * `APPROX_QUANTILES(x, 2)`で[最小値、 中央値、 最大値]の配列
* `PERCENTILE_CONT (value_expression, percentile [{RESPECT | IGNORE} NULLS])`
    * 線形補間つきのpercenttile点をだす
    * `PERCENTILE_CONT(x, 0)`
        * だとxのNULLを無視する
    * `PERCENTILE_CONT(x, 0 RESPECT NULLS)`
        * NULLを考慮する
        * NULLは最小値扱い
* `PERCENTILE_DISC (value_expression, percentile [{RESPECT | IGNORE} NULLS])`
    * 補間なしのpercentile点
    * APPROX_QUANTILESの挙動と同じ
    * `PERCENTILE_DISC(x, 0.5) OVER()`
        * でtable `x`の中央値を全ての行に付与する
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

### Array function
* array_expression[OFFSET(zero_based_offset)]
    * 配列の参照
    * 添字が0から始まる
    * out of rangeのときerorr
* array_expression[ORDINAL(one_based_offset)]
    * 配列の参照
    * 添字が1から始まる
    * out of rangeのときerorr
* array_expression[SAFE_OFFSET(zero_based_offset)]
    * 配列の参照
    * 添字が0から始まる
    * out of rangeのときNULL
* array_expression[SAFE_ORDINAL(one_based_offset)]
    * 配列の参照
    * 添字が1から始まる
    * out of rangeのときNULL
* ARRAY_REVERSE(array_expression)
    * 反転
* GENERATE_ARRAY(start_expression, end_expression[, step_expression])
    * 数字の配列をつくる
    * FLOAT64かINT64
* ARRAY_LENGTH(array_expression)
    * 配列のサイズ
    * 空のときは0
    * array_expressionがNULLのときNULL
* ARRAY_CONCAT(array_expression_1 [, array_expression_n])

### JSON function
JSON pathは以下のような形式

```json
{"class" : {"students" : [{"name" : "Jane"}]}}
```

* `$.class.students`

* JSON_EXTRACT(json_string_expr, json_path_string_literal)
* JSON_EXTRACT_SCALAR(json_string_expr, json_path_string_literal)

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

## Repeated Records or ARRAY of STRUCT
* standard SQLだとARRAY of STRUCT
* [Migrating to Standard SQL  |  BigQuery  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/standard-sql/migrating-from-legacy-sql#removing_repetition_with_flatten)

* arrayがある場合は、FROMでcolumnを`UNNEST`する必要がある
* repeated recordがnestしている場合は、`UNNEST`したものを`UNNEST`する必要がある

```sql
#standardSQL
SELECT
  repository.url,
  page.page_name
FROM
  `bigquery-public-data.samples.github_nested`,
  UNNEST(payload.pages) AS page
LIMIT 5;
```

Arrayの比較はsubqueryで行うのが良さそう。
subqueryをnestしていけばarrayのnestを同じ構造で扱える。

[sql - How do I find elements in an array in BigQuery - Stack Overflow](https://stackoverflow.com/questions/42989922/how-do-i-find-elements-in-an-array-in-bigquery)

```sql
#standardSQL
WITH yourTable AS (
  SELECT'192.168.1.1' AS ip,
  [('apple', 'red'), ('orange', 'orange'), ('grape', 'purple')] AS cookie
  UNION ALL
  SELECT '192.168.1.2', [('abc', 'xyz')]
)
SELECT ip
FROM yourTable
WHERE (
  SELECT COUNT(1)
  FROM UNNEST(cookie) AS pair
  WHERE pair IN (('grape', 'purple'),  ('orange', 'orange'))
) = 2
```

## subquery
* [sql - How do I find elements in an array in BigQuery - Stack Overflow](https://stackoverflow.com/questions/42989922/how-do-i-find-elements-in-an-array-in-bigquery)


## Array UNNEST
arrayの部分の値を持つ行をarray以外の部分にjoinする。
arrayが2つの値を持つことをcheckする必要がある場合は、下記のようなunnestをするとcheckが難しくなる。

```sql
WITH
  sample AS (
  SELECT
    1 AS col1
    , [
      5,
      6,
      7,
      8
    ] AS col2
)
SELECT
  *
FROM
  sample
  , UNNEST(col2)
```

この場合は、subqueryでcheckするか

```sql
WITH
  sample AS (
  SELECT
    1 AS col1
    , [
      5,
      6,
      7,
      8
    ] AS col2
)
SELECT
  *
FROM
  sample
WHERE
  # arrayに5と7を含むかのcheck
  (
    SELECT
      COUNT()
    FROM
      UNNEST(sample.col2) AS col2col
    WHERE
      5 = col2col
      OR
      7 = col2col
  ) = 2
```

もしくはselectでflattenにする。
この場合はarrayの中をwhereで一意に特定できない場合はqueryがfailする。
つまり、`[5,6,7,8,8]`は下記ではerror.

```sql
#standardSQL
WITH
  sample AS (
  SELECT
    1 AS col1
    , [
      5,
      6,
      7,
      8
    ] AS col2
)
SELECT
  col1
  , (SELECT x FROM UNNEST(col2) AS x WHERE x=5) AS col25
  , (SELECT x FROM UNNEST(col2) AS x WHERE x=6) AS col26
  , (SELECT x FROM UNNEST(col2) AS x WHERE x=8) AS col27
  , (SELECT x FROM UNNEST(col2) AS x WHERE x=9) AS col28
FROM
  sample
```
