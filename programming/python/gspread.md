---
title: Gspread
---

## Gspread
Google Spreadsheets Python API.

* [Using Google Spreadsheets and Python](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html)

* Go to the Google APIs Console.
* Create a new project.
* Click Enable API. Search for and enable the Google Drive API.
* Create credentials for a Web Server to access Application Data.
* Name the service account and grant it a Project Role of Editor.
* Download the JSON file.
* Copy the JSON file to your code directory and rename it to client_secret.json

spread sheeetの作成し、`client_email`のaddressとshareする必要がある。
shareを忘れると、`gspread.exceptions.SpreadsheetNotFound`がでる。
認証

```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

path_to_json_key = '/Users/makotonagai/.config/gcloud/gcp-sandbox-7939a79057a7.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(path_to_json_key, scope)

gc = gspread.authorize(credentials)
```

## API
* `gc.open()`
    * Return: Spreadsheet
* `gc.open_by_url()`
    * Return: Spreadsheet
* `gc.open_by_key()`
    * Return: Spreadsheet
* `spread_sheet.sheet1`
    * 最初のsheet
* `spread_sheet.title`
    * spread sheetのtitle
* `spread_sheet.updated`
    * updateされた時間をRFC3339
* `spread_sheet.worksheet(title)`
    * titleのworksheetを取得
    * 複数同じtitleがある場合は、最初にmatchしたもの
    * Return: Worksheet
* `spread_sheet.worksheets()`
    * list of Worksheet
* `worksheet.acell('A1')`
    * 指定した場所のcell instance
* `worksheet.cell(row, col)`
    * 数値でcell指定
* `worksheet.find(query)`
    * queryは正規表現
* `worksheet.findall(query)`
    * 全てのcell
* `worksheet.update_acell(label, value)`
    * labelのcellをvalueにupdate
* `worksheet.update_cell(row, col, value)`
    * (row, col)のvalue


## Reference
* https://github.com/burnash/gspread.git
* [gspread API Reference — gspread 0.6.2 documentation](http://gspread.readthedocs.io/en/latest/#gspread.Spreadsheet)
