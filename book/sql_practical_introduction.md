---
title: SQL実践入門
---

## SQL実践入門

## Chapter5

```sql
CREATE TABLE IF NOT EXISTS Sales
(company VARCHAR(1) NOT NULL,
 year int NOT NULL,
 sale int);
CREATE TABLE IF NOT EXISTS Sales2
(company VARCHAR(1) NOT NULL,
 year int NOT NULL,
 sale int,
 var VARCHAR(1) NOT NULL);

INSERT INTO Sales (company, year, sale)
VALUES
('A', 2002, 50);
INSERT INTO Sales (company, year, sale)
VALUES
('A', 2003, 52);
INSERT INTO Sales (company, year, sale)
VALUES
('A', 2004, 55);
INSERT INTO Sales (company, year, sale)
VALUES
('A', 2007, 55);
INSERT INTO Sales (company, year, sale)
VALUES
('B', 2001, 27);
INSERT INTO Sales (company, year, sale)
VALUES
('B', 2005, 28);
INSERT INTO Sales (company, year, sale)
VALUES
('B', 2006, 28);
INSERT INTO Sales (company, year, sale)
VALUES
('B', 2009, 30);
INSERT INTO Sales (company, year, sale)
VALUES
('C', 2001, 40);
INSERT INTO Sales (company, year, sale)
VALUES
('C', 2005, 39);
INSERT INTO Sales (company, year, sale)
VALUES
('C', 2006, 38);
INSERT INTO Sales (company, year, sale)
VALUES
('C', 2010, 35);
```

```sql
SELECT
  company,
  year,
  sale,
  CASE SIGN(sale - MAX(sale)
    OVER (PARTITION BY company
          ORDER BY year
          ROWS BETWEEN 1 PRECEDING
            AND 1 PRECEDING)
            )
  WHEN 0 THEN '='
  WHEN 1 THEN '+'
  WHEN -1 THEN '-'
  ELSE NULL END AS var
FROM Sales;
           
```

## Reference
* [SQL Fiddle](http://sqlfiddle.com/)
