---
title: Puppeteer
---

## Puppeteer

## API
* [puppeteer/api.md at master · GoogleChrome/puppeteer](https://github.com/GoogleChrome/puppeteer/blob/master/docs/api.md)


```javascript
page.on('event_name', callback)
```

* eventの一覧
    * [puppeteer/api.md at master · GoogleChrome/puppeteer](https://github.com/GoogleChrome/puppeteer/blob/master/docs/api.md#class-page)


## Download canvas image
* [Saving Images from a Headless Browser](https://intoli.com/blog/saving-images/)

```javascript
const puppeteer = require('puppeteer');

const fs = require('fs');
const mime = require('mime');
const URL = require('url').URL;

const parseDataUrl = (dataUrl) => {
  const matches = dataUrl.match(/^data:(.+);base64,(.+)$/);
  if (matches.length !== 3) {
    throw new Error('Could not parse data URL.');
  }
  return {
    mime: matches[1],
    buffer: Buffer.from(matches[2], 'base64'),
  };
};

(async() => {
  const browser = await puppeteer.launch({
    headless: true,
    args: [],
  });
  const page = await browser.newPage();

  // this is for debugging functions inside of page.evaluate()
  page.on('console', msg => {
    console.log(msg);
  });

  const getDataUrlThroughCanvas = async () => {
    // Create a new image element with unconstrained size.
    const image = document.createElement('img');
    image.crossOrigin = "anonymous";
    // wait until load is finished
    await (() => {
      return new Promise((resolve) => {
        image.onload = (() => resolve());
        image.src = '/url/to/image';
      })
    })();
    // Create a canvas and context to draw onto.
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    canvas.width = image.width;
    canvas.height = image.height;
    context.drawImage(image, 0, 0);
    return canvas.toDataURL();
  };

  try {
    const dataUrl = await page.evaluate(getDataUrlThroughCanvas);
    const { buffer } = parseDataUrl(dataUrl);
    fs.writeFileSync('./output.png', buffer, 'base64');
  } catch (error) {
    console.log(error);
  }

  browser.close();
})();
```


## Reference
* [GoogleChrome/puppeteer: Headless Chrome Node API](https://github.com/GoogleChrome/puppeteer)
* [Question: How do I get puppeteer to download a file? · Issue #299 · GoogleChrome/puppeteer](https://github.com/GoogleChrome/puppeteer/issues/299)
