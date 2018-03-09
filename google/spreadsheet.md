---
title: Spreadsheet
---

## Spreadsheet


## Functions

* Query
    * https://support.google.com/docs/answer/3093343?visit_id=1-636549486149332271-747246594&rd=1
* Importage
    * https://support.google.com/docs/answer/3093340?visit_id=1-636549486149332271-747246594&rd=1


* column nameは列番号で指定する
* `GROUP BY A` `PIVOT F` でpivto tableで作っている表が作れる
    * PIVOTは列
    * GROUP BYは行
    * alphabetでの参照はimportrangeは使えないので、`Col1`, `Col2`などと各必要がある
    * importrangeはauthorizationoが必要なので、初回は適当なcellでimportrangeを実行して認証を許可にする

```
=QUERY(A2:F24, "SELECT AVG(E) GROUP BY A PIVOT F", 1)
# Pivot table
=QUERY(IMPORTRANGE("spreadsheet_url", ""), "SELECT Col1, AVG(Col5) GROUP BY Col1 PIVOT Col6 LABEL Col1 'label'", 1)
```

## Reference
    * Queryは、query langage apiのsyntaxが使える
    * [Query Language Reference (Version 0.7)  |  Charts  |  Google Developers](https://developers.google.com/chart/interactive/docs/querylanguage#pivot)
    * [Google スプレッドシートからデータをSQLライクに取得してグラフを描く - Qiita](https://qiita.com/atsaki/items/6d2027c3bcb50b03fa18)
    * [Help with a "=QUERY(IMPORTRANGE(..." formula in Google Sheets - Web Applications Stack Exchange](https://webapps.stackexchange.com/questions/108327/help-with-a-queryimportrange-formula-in-google-sheets)

