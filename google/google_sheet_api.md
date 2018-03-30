---
title: Google Sheet API
---

## Google Sheet API

## Conditional formatting
* [Conditional Formatting  |  Sheets API  |  Google Developers](https://developers.google.com/sheets/api/samples/conditional-formatting)
* [Requests  |  Sheets API  |  Google Developers](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/request#AddConditionalFormatRuleRequest)


```javascript
  var sheet = SpreadsheetApp.getActiveSheet();
  var numRows = range.getNumRows();
  var numColumns = range.getNumColumns(); 
  var startRow = range.getRowIndex();
  var startColumn = range.getColumn();
  
  for (var i = 0; i < numColumns; ++i) {
    sheet.getRange(starRow, startColumn + i, numRows, 1)
  }
```

## Reference
* https://www.googleapis.com/auth/spreadsheets
* [Google apps script でfilterをかける方法](https://xn--t8j3bz04sl3w.xyz/google-apps-script/filter/3874/)
