---
title: Selemium
---

## Selemium


## Chrome
- https://medium.com/jaanvi/headless-browser-in-python-9a1dcc2b608b
- [ChromeDriver \- WebDriver for Chrome \- Getting started](https://chromedriver.chromium.org/getting-started)

```
brew install --cask chromedriver
```

## Modify elements

```
element = driver.find_element_by_id("some_id")
driver.execute_script("arguments[0].innerText = 'what_you_want_to_show'", element)
```

## Reference
- https://selenium-python.readthedocs.io/
