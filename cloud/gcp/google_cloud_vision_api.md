---
title: Google Cloud Vision API
---

## Google Cloud Vision API


## Samples

### Label Detection Sample
* [python-docs-samples/detect.py at master · GoogleCloudPlatform/python-docs-samples](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/cloud-client/detect/detect.py)
    * in python

Localのimageを作る例

```python
from google.cloud import vision 
from google.cloud.vision import types

def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)
```

GCSに保存してあるimageをそのまま利用できる。

```python
def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)
```

戻り値は`EntityAnnotation`型のlist

* [Method: images.annotate  |  Google Cloud Vision API  |  Google Cloud Platform](https://cloud.google.com/vision/docs/reference/rest/v1/images/annotate)

```
{
  "mid": string,
  "locale": string,
  "description": string,
  "score": number,
  "confidence": number,
  "topicality": number,
  "boundingPoly": {
    object(BoundingPoly)
  },
  "locations": [
    {
      object(LocationInfo)
    }
  ],
  "properties": [
    {
      object(Property)
    }
  ],
}
```

* mid
    * id
* locale
    * descriptionの言語
* description
    * このentityの説明
* score
    * entityの総合的なscoreで[0, 1]
* confidence
    * このdetectionの精度
    * 例えば、Eiffel towerをdetectした時のimageの中にTowerがあるconfidenceを[0, 1]で表現
* topicality
    * Image Content Annotation の類似度を[0, 1]
    * Eiffel towerをdetectしたimageはtowerとの類似度が高いなど
* boundingPoly
    * BoundingPolyがた　
* locations[]
    * LocationsInfo型のarray
    * 写真の撮られた場所と写真上の物体の位置を表すためにarrayになっている
    * Landmark Detectionで良く利用される
* properties[]
    * Propety型のarray
    * user specifiedなkey/valueのproperty

## Supported Images
* JPEG
* PNG8
* PNG24
* GIF
* Animated GIF (first frame only)
* BMP
* WEBP
* RAW
* ICO

Supported image size.
recommendes sizeは、抽出したい特徴の大きさを反映している。
Faceは画像の中で小さいsizeであることが大きいため、画像自体が大きなサイズである必要がある。
一方Label detectionでは画像全体を考慮するので、画像自体が大きい必要はない。
経験的には、640 x 480で多くの場合うまくいく。
これより大きいサイズは処理測度の劣化に対する精度上の大きなメリットはない。


* minimum size
    * 640 x 480 pixels 
* recommended size
    * FACE_DETECTION
        * 1600 x 1200
    * LANDMARK_DETECTION/LOGO_DETECTION/LABEL_DETECTION/SAFE_SEARCH_DETECTION
        * 640 x 480
    * TEXT_DETECTION/DOCUMENT_TEXT_DETECTION
        * 1024 x 768

File sizes

* 4MB以下である必要がある
* batchで送る場合は8MB /request


## Price
機能のtypeごとに料金がかかる。

| 機能のタイプ            | 説明                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------|
| LABEL_DETECTION         | 画像の内容に基づいてラベルを追加
| TEXT_DETECTION          | 画像内のテキストに対してOCR
| SAFE_SEARCH_DETECTION   | 画像の画像セーフサーチ プロパティ
| FACE_DETECTION          | 画像内の顔を検出 
| LANDMARK_DETECTION      | 画像内の地理的ランドマーク 
| LOGO_DETECTION          | 画像内の企業ロゴを検出 
| IMAGE_PROPERTIES        | 画像の一連のプロパティ（画像のドミナント カラーなど）を計算
| WEB_DETECTION           | ニュース、イベント、画像内の有名人などの時事的なエンティティを検出し、Google 画像検索の機能を使用してウェブ上で同様の画像を検索 
| DOCUMENT_TEXT_DETECTION | 密度の高いテキスト用に特別に調整されたモデルを使用して、ドキュメントなどの密度の高いテキストの画像に OCR を実行                      

機能の1000unit(画像)/monthごとの料金が以下。

* 最初の1000unit/monthは全て無料
* 1,001～5,000,000は
    * SAFE_SEARCH_DETECTIONはLabel検出を利用している場合は無料
    * WEB_DETECTIONとDOCUMENT_TEXT_DETECTIONは1000unitごとに3.5 USD
    * それ以外は1000unit 1.5USD
* 5,000,001～20,000,000
    * SAFE_SEARCH_DETECTIONはLabel検出を利用している場合は無料
    * WEB_DETECTIONとDOCUMENT_TEXT_DETECTIONは問い合わせが必要
    * LABEL_DETECTIONは1000unit ごとに1USD
    * それ以外は1000unit 0.6USD



## Reference
* [Vision API - 画像コンテンツ分析  |  Google Cloud Platform](https://cloud.google.com/vision/?hl=ja)
