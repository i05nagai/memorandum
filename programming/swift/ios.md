---
title: Swift for iOS
---

## Swift for iOS

## PHImgeManager
* [requestImage(for:targetSize:contentMode:options:resultHandler:) - PHImageManager | Apple Developer Documentation](https://developer.apple.com/documentation/photos/phimagemanager/1616964-requestimage)
    * 

* [requestLivePhoto(for:targetSize:contentMode:options:resultHandler:) - PHImageManager | Apple Developer Documentation](https://developer.apple.com/documentation/photos/phimagemanager/1616984-requestlivephoto)

* PHImageContentMode
    * enum
    * `aspectFit`
        * width, height大きい方に合わせる
    * `aspectFill`
        * width, height小さい方を拡大する
* PHImageRequestOptions
    * [PHImageRequestOptions - Photos | Apple Developer Documentation](https://developer.apple.com/documentation/photos/phimagerequestoptions)
    * normalizedCropRect

* PHLivePhotoRequestOptions
    * [PHLivePhotoRequestOptions - Photos | Apple Developer Documentation](https://developer.apple.com/documentation/photos/phlivephotorequestoptions)
    * `deliveryMode`
        * PHImageRequestOptionsDeliveryMode
* PHImageRequestOptionsDeliveryMode
    * qualityとdelivery priority

## PHPhotoLibrary
* [PHPhotoLibrary - Photos | Apple Developer Documentation](https://developer.apple.com/documentation/photos/phphotolibrary)

* shared()
    * returns `PHPhotoLibrary`
* register(_ observer: PHPhotoLibraryChangeObserver)
    * 

## CIImage
* [CIImage - Core Image | Apple Developer Documentation](https://developer.apple.com/documentation/coreimage/ciimage)

* applyingFilter
    * [Core Image Filter Reference](https://developer.apple.com/library/content/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346)
    * `filterName: String`
    * `parameter: [String: Any]`
        * dictionary

* CIFilter
    * [CIFilter - Core Image | Apple Developer Documentation](https://developer.apple.com/documentation/coreimage/cifilter)


## UITableViewCell


## UICollectionView
* [iOSアプリ、UICollectionView で Grid 表示](https://i-app-tec.com/ios/collectionview.html)

* UICollectionViewのMin Spacingを確認
* Autoresizingを設定すると画面sizeに合わせてresizeできる
    * cellの中身もAutoresizngに対応する
* IndexPath
    * [IndexPath - Foundation | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/indexpath)


## UIImageView
* [005 UIImageViewで画像を表示 - Swift Docs](https://sites.google.com/a/gclue.jp/swift-docs/ni-yinki100-ios/uikit/005-uiimageviewde-hua-xiangwo-biao-shi)

```swisft
        // UIImageViewを作成する.
        myImageView = UIImageView(frame: CGRectMake(0,0,100,120))
        // 表示する画像を設定する.
        let myImage = UIImage(named: "logo.png")
        // 画像をUIImageViewに設定する.
        myImageView.image = myImage
        // 画像の表示する座標を指定する.
        myImageView.layer.position = CGPoint(x: self.view.bounds.width/2, y: 200.0)
        // UIImageViewをViewに追加する.
        self.view.addSubview(myImageView)
```

## Simulator
* https://stackoverflow.com/questions/468879/adding-images-to-iphone-simulator/35271607#35271607

以下でdevice IDを取得できる。

```
xcrun simctl list
```

### Add images
simulatorに画像を追加位

```
xcrun simctl addmedia booted ./MyFile.jpg
```

特定のdeviceに加える場合は、device IDを指定する。

```
xcrun simctl addmedia <device_id> ./MyFile.jpg
```

## Graphics
iOS上での画像処理は以下の4つの選択肢がある。

1. Core Graphics
    * 古くから画像処理用のAPI
    * Interfaceが古く使いにくい
    * [Introduction](https://developer.apple.com/library/content/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
2. Core Image
    * modernなCore Graphics
    * [CICategoryBlur - Core Image Filter Reference](https://developer.apple.com/library/content/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP30000136-SW29)
        * filterの一覧
    * [About Core Image](https://developer.apple.com/library/content/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
        * officialのCore imageのdocument
    * [An Introduction to Core Image · objc.io](https://www.objc.io/issues/21-camera-and-photos/core-image-intro/)
    * defaltのfilterのsample
        * [GitHub - makomori/Sharaku: Image filtering UI library like Instagram.](https://github.com/makomori/Sharaku)
        * [GitHub - KawabataLemon/PhotoSample](https://github.com/KawabataLemon/PhotoSample)
        * [CoreImageのフィルターを試してみる(CICategoryColorAdjustment、その2) - しめ鯖日記](http://llcc.hatenablog.com/entry/2017/09/15/151745)
        * [08. CoreImage - Swift Docs](https://sites.google.com/a/gclue.jp/swift-docs/ni-yinki100-ios/coreimage)
        * [001 セピア処理 · GitBook](http://docs.fabo.io/swift/coreimage/001_coreimage.html)
3. Metal
    * GPUを明示的に使い画像処理や3D renderingができる
    * [[iOS] MetalでGPUコンピューティング (1) 最小限のコードの記述と特性の把握 - Qiita](https://qiita.com/yuky_az/items/ece9b64befc635e89f1a)
    * [iOSの新グラフィックAPI - Metal入門してみる - Qiita](https://qiita.com/edo_m18/items/0fd6971c98c27a125d6e)
4. OpenGL
    * iOS上でのOpenGLが利用できる
    * [SwiftでOpenGL　その１ - Qiita](https://qiita.com/JunSuzukiJapan/items/4f3e7265b8e1175bbfda)
    * [iOSでのOpenGLをちゃんと理解する（GLKitでブラックボックスになっている部分を理解する） - Qiita](https://qiita.com/ykensuke/items/e706f7c57d8df6aee911)

Core Image(CI)とCore Graphics(CG)がある。
Core Imageは画像処理が簡単に行えるAPIが多く使いやすい。

* Feature detecting
    * Face detecting
* Auto enhancement filters
    * Red eye correction
    * face skin color balance
    * vibrance (saturaition adjustment)
    * tone curve (contrast adjustment)

## Core Image
Core Image graphisでは画像は、基本的に`CIImage` classで扱う。
画像を描画する際は、`UIImage`や`UIImageView`(のUIImage)を扱うことが多いが、これらのclassからは簡単に相互変換できる。

**UIImageからCIImageへの変換**

```swift
    let ciImage:CIImage? = CIImage(image: uiImage)
```

**CIImageからUIImageへの変換**

```swift
    let uiImage:UIImage? = UIImage(ciImage: ciImage)
```

**UIImage -> filter -> UIImageview**

また、iOSで`UIImage`を`UIImageView`に反映させる処理は以下のようになる。

```swift
class ViewController: UIViewController {
    let filter = CIFilter(name: "CISepiaTone",
                          withInputParameters: [kCIInputIntensityKey: 0.5])!
    @IBOutlet var imageView: UIImageView!

    func displayFilteredImage(image: UIImage) {
        // UIImage -> CIImage
        let inputImage = CIImage(image: image)!
        // filterにinputImageを入力
        filter.setValue(inputImage, forKey: kCIInputImageKey)
        // filterを適用してiamgeView
        imageView.image = UIImage(CIImage: filter.outputImage!)
    }
}
```

以下では`CIImage`を受け取って、`UIImage`を返すfilterを上げていく。

**Nashville**


**Hefe**



### 補足

**処理速度について**

* [Getting the Best Performance](https://developer.apple.com/library/content/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_performance/ci_performance.html#//apple_ref/doc/uid/TP30001185-CH10-SW1)



**Filter chain**

複数のfilterをmethod chainのようにつなげることができる。
filter chainが推奨される理由は、CIImageは描画が必要となるまでfilterの計算はしないので、chainとなったfilterは描画時に最適化され、適用される。
高速に複数のfilterを適用できる。

```swift
    // filter chain
    let outputImage: CIImage? = ciImage
        .applyingFilter("CIPhotoEffectProcess")
        .applyingFilter("CIBloom", parameters:[
            kCIInputRadiusKey: 10.0,
            kCIInputIntensityKey: 1.0
        ])
    // 以下と同じ( CIPhotoEffectProcess + CIBloom)
    let colorFilter = CIFilter(
        name: "CIPhotoEffectProcess",
        withInputParameters: [kCIInputImageKey: ciImage])!
    let outputImage: CIImage? = colorFilter
        .outputImage!
        .applyingFilter("CIBloom", parameters: [
            kCIInputRadiusKey: 10.0,
            kCIInputIntensityKey: 1.0
        ])
```

<img src="https://developer.apple.com/library/content/documentation/GraphicsImaging/Conceptual/CoreImaging/art/filter_chain01_2x.png">
画像はofficialのdocumentから引用


**CIContext**

`CIFilter`で多くの複雑な処理が可能だが、CPUやGPUに対するよりlow levelの実装が必要な場合は`CIContext`を使う。
`CIContext`の生成は時間がかかるので、一度生成したらstoreしたり、非同期に生成するなどする。
`CIContext`は生成時のoptionにもとづき、自動的に適切なdeviceを決定する。
この自動的な選択は、画像のjpeg保存などの処理では十分である。

**Custom Filter**

Defaultで100種類以上のfilterが提供されているが、必要とするfilterがない場合は自分でfilterを定義できる。
RGBAの画像を変換する処理は、`openGL Shading Language (GLSL)`をbaseとした`Core Image Kernel Language`と呼ばれる言語で記述する必要がある。
CoreImageのtutorialにある`HazeRemovalFilter`を、custom filterとして作る場合は以下のようなfilterを作る。

```

```

`Core Image Kernel Language`は`GLSL`と比較して以下のようにかなり制約が強いので、あまり複雑な処理はできない。

* `if, for, while`などの制御文はcompile時に決定可能なloopにしか使えない
* `mat2, mat3, mat4, struct, arrays`をsupportしていない
* `% << >> | & ^ || && ^^ ~`などのoperatorをsupportしていない
* `ftransform, matrixCompMult, dfdx, dfdy, fwidth, noise1, noise2, noise3, noise4, refract`のbuilt in functionをsupportしていない

どうしても必要な場合は、以下のsiteは参考になる。

* [Core Image Kernel Language](https://developer.apple.com/library/content/documentation/GraphicsImaging/Reference/CIKernelLangRef/ci_gslang_ext.html#//apple_ref/doc/uid/TP40004397-CH206-BCIEGAIJ)
    * officialの`Core Image Kernel Language`のrefeernce
* [CIKernel を使用してCore Imageのカスタムフィルタをつくる - Qiita](https://qiita.com/shu223/items/6959dc7ba6ac0844340b)
    * swiftでのcustom filterの作り方
* [GitHub - KawabataLemon/PhotoSample](https://github.com/KawabataLemon/PhotoSample)



**Blending algorithm**

FilterのBlendingのalgorithmは以下のPDFのblendingのalgorithmにもとづいている。
blendingの正確な計算式が必要であれば参照する。

http://wwwimages.adobe.com/content/dam/acom/en/devnet/pdf/PDF32000_2008.pdf


### Creating Custom filter
* [Creating Custom Filters](https://developer.apple.com/library/content/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_custom_filters/ci_custom_filters.html#//apple_ref/doc/uid/TP30001185-CH6-TPXREF101)

Customで作ったfilterはpackaging可能
CPU上で実行されるcustom filterを作る。

* color filter
* warp filter
* general filter
    * pixel colorとpixel locationを変更するGPUのkernel routineを使ったfilterも作成可能
    * color filterとwarp filterで足りる場合は、iOSとMac上で最適になるように作られているので、color/warp filterを使った方が良い


1. Write the Kernel Code
2. Use Quartz Composer to Test the Kernel Routine
3. Declare an Interface for the Filter
4. Write an Init Method for the CIKernel Object
5. Write a Custom Attributes Method
6. Write an Output Image Method
7. Register the Filter
8. Write a Method to Create Instances of the Filter

haze removal filterを例に作成方法を記載する。

**1. Write the kernel code**

`.cikernel`の拡張子でkernelのcodeを記載する。
`.cikernel`はOpenGL Shading Language (glslang)のsubsetである。
利用可能な言語機能の一覧は以下を参照する必要がある。

* [Introduction](https://developer.apple.com/library/content/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397)

```
// filterのinterface
kernel vec4 myHazeRemovalKernel(
    sampler src,
    __color color,
    float distance,
    float slope)
{
    vec4   t;
    float  d;
    // destCoord().y 処理中のpixelのy座標
    d = destCoord().y * slope  +  distance;              // 2
    // sample(src, samplerCoord(src))でsrcの画素値を取得
    t = unpremultiply(sample(src, samplerCoord(src)));   // 3
    // have removal formulaの計算
    t = (t - d*color) / (1.0-d);                         // 4
    return premultiply(t);                               // 5
}
```

**Quartz Composer**

自身で作成したkernel filterは`Quartz Composer`でtestできる。
`Quartz Composer`は以下の手順で　DLできるが、余り使い勝手は良くない。

1. Open Xcode.
2. Choose Xcode > Open Developer Tool > More Developer Tools...
3. Choosing this item will take you to developer.apple.com.
4. Sign in to developer.apple.com.
5. You should then see the Downloads for Apple Developers webpage.
6. Additoional tools for Xcode9
7. Open `Additional tools for Xcode9.dmg` and Copy `Graphics` folder


### Times

On simulator

```
Time elapsed for collectionView 0: 0.00168603658676147 seconds
Time elapsed for collectionView 1: 0.593058049678802 seconds
Time elapsed for collectionView 2: 0.158993005752563 seconds
Time elapsed for collectionView 3: 0.0159239768981934 seconds
```

On iPhone SE with debug build

```
Time elapsed for collectionView 0: 0.0253379940986633 seconds
Time elapsed for collectionView 1: 0.0149459838867188 seconds
Time elapsed for collectionView 2: 0.0117970108985901 seconds
Time elapsed for collectionView 3: 0.0110309720039368 seconds
```

On iPhone SE with release

```
Time collectionView 3: 0.00973397493362427 seconds
Time collectionView 0: 0.0127999782562256 seconds
Time collectionView 1: 0.0114859938621521 seconds
Time collectionView 2: 0.010906994342804 seconds
Time collectionView 3: 0.0102810263633728 seconds
Time collectionView 0: 0.0175189971923828 seconds
Time collectionView 1: 0.0103849768638611 seconds
Time collectionView 2: 0.00894105434417725 seconds
Time collectionView 3: 0.00812500715255737 seconds
```

```swift
    static func applyTestFilter(ciImage: CIImage) -> CIImage? {
        let width = ciImage.extent.width
        let height = ciImage.extent.height
        let centerWidth = width / 2.0
        let centerHeight = height / 2.0
        let length0 = min(width / 4.0, height / 4.0, 10)
        let length1 = min(width / 3.0, height / 3.0, 50)
        print(width, height, centerWidth, centerHeight, length0, length1)
        let color0 = self.getColor(red: 0, green: 0, blue: 0, alpha: 100)
        let color1 = self.getColor(red: 255, green: 255, blue: 255, alpha: 100)
        let filter1 = CIFilter(
            name: "CILinearGradient", withInputParameters: [
                "inputPoint0": CIVector(x: length0, y:centerHeight),
                "inputPoint1": CIVector(x: length1, y:centerHeight),
                "inputColor0": color0,
                "inputColor1": color1,
                ])!
            .outputImage!
            .cropped(to: ciImage.extent)
        let filter2 = CIFilter(
            name: "CILinearGradient", withInputParameters: [
                "inputPoint0": CIVector(x: centerWidth, y:length1),
                "inputPoint1": CIVector(x: centerWidth, y:length0),
                "inputColor0": color0,
                "inputColor1": color1,
                ])!
            .outputImage!
            .cropped(to: ciImage.extent)
        return ciImage
            .applyingFilter("CIMultiplyBlendMode", parameters: [
                "inputBackgroundImage": filter1,
                ])
            .applyingFilter("CIAdditionCompositing", parameters: [
                "inputBackgroundImage": filter2,
                ])
    }
```

```
    static func applyHudsonFilter(ciImage: CIImage) -> CIImage? {
        let width = ciImage.extent.width
        let height = ciImage.extent.height
        let centerWidth = width / 2.0
        let centerHeight = height / 2.0
        let radius0 = min(width / 4.0, height / 4.0)
        let radius1 = min(width / 1.5, height / 1.5)
        
        let color0 = self.getColor(red: 166, green: 177, blue: 255, alpha: 255)
        let color1 = self.getColor(red: 52, green: 33, blue: 52, alpha: 255)
        let circle = CIFilter(name: "CIRadialGradient", withInputParameters: [
            "inputCenter": CIVector(x: centerWidth, y: centerHeight),
            "inputRadius0": radius0,
            "inputRadius1": radius1,
            "inputColor0": color0,
            "inputColor1": color1,
            ])?.outputImage?.cropped(to: ciImage.extent)
        return ciImage
            .applyingFilter("CIColorControls", parameters: [
                "inputSaturation": 1.1,
                "inputBrightness": 0.2,
                "inputContrast": 0.95,
                ])
            .applyingFilter("CIMultiplyCompositing", parameters: [
                "inputBackgroundImage": circle!,
                ])
            .settingAlphaOne(in: ciImage.extent)
            .applyingFilter("CIColorClamp", parameters: [
                "inputMinComponents": CIVector(x: 0, y: 0, z: 0, w: 0),
                "inputMaxComponents": CIVector(x: 1, y: 1, z: 1, w: 0.5),
                ])
    }
```

CollectionViewのthumbnailのfilterの処理時間
3回の平均

| filter      | device (sec) | simulator (sec) |
+=============|==============|=================+
| 1977        | 0.0121       | 1.4867          |
| Chrome      | 0.0150       | 0.6211          |
| Clarendon   | 0.0094       | 1.2565          |
| Fade        | 0.0097       | 0.3077          |
| HazeRemoval | 0.0130       | 0.6795          |
| Instant     | 0.0094       | 0.1236          |
| Linear      | 0.0062       | 0.0006          |
| Mono        | 0.0087       | 0.0222          |
| Nashville   | 0.0330       | 1.6097          |
| Noir        | 0.0087       | 0.0212          |
| Process     | 0.0091       | 0.0236          |
| Toaster     | 0.0147       | 0.8657          |
| Tonal       | 0.0083       | 0.1920          |
| Tone        | 0.0061       | 0.3095          |
| Transfer    | 0.0095       | 0.0238          |

Collection viewとviewDidloadの時間
3回の平均

| object      | device (sec)     | simulator (sec)   |
+=============|==================|===================+
| 1st cell    | 0.0121466517448  | 0.00180900096893  |
| 2nd cell    | 0.0022016565005  | 0.00115235646566  |
| 3rd cell    | 0.00155603885651 | 0.000826338926951 |
| 4th cell    | 0.00167268514633 | 0.000815014044444 |
| viewDidload | 0.17617102464    | 7.54655232032     |

simulatorの1回目のfilter処理と2回目のfilter処理の時間
3回の平均

| filter      | 1st simulator (sec) | 2nd simulator (sec) |
+=============|=====================|=====================+
| 1977        | 2.0348              | 1.3711              |
| Chrome      | 0.6523              | 0.2420              |
| Clarendon   | 1.0200              | 0.6433              |
| Fade        | 0.6509              | 0.0414              |
| HazeRemoval | 0.7720              | 0.4865              |
| Instant     | 0.4845              | 0.2717              |
| Linear      | 0.3063              | 0.1394              |
| Mono        | 0.4311              | 0.2414              |
| Nashville   | 1.9360              | 0.2677              |
| Noir        | 0.2444              | 0.0456              |
| Process     | 0.2538              | 0.4670              |
| Toaster     | 1.0061              | 0.4198              |
| Tonal       | 0.2417              | 0.2498              |
| Tone        | 0.2053              | 0.1266              |
| Transfer    | 0.2363              | 0.0418              |

実機の1回目のfilter処理と2回目のfilter処理の時間
3回の平均

| filter      | 1st device (sec) | 2nd device (sec) |
+=============|==================|==================+
| 1977        | 0.0180           | 0.0180           |
| Chrome      | 0.0159           | 0.0169           |
| Clarendon   | 0.0159           | 0.0175           |
| Fade        | 0.0159           | 0.0165           |
| HazeRemoval | 0.0181           | 0.0174           |
| Instant     | 0.0172           | 0.0159           |
| Linear      | 0.0146           | 0.0152           |
| Mono        | 0.0160           | 0.0164           |
| Nashville   | 0.0206           | 0.0180           |
| Noir        | 0.0153           | 0.0164           |
| Process     | 0.0162           | 0.0160           |
| Toaster     | 0.0177           | 0.0169           |
| Tonal       | 0.0162           | 0.0169           |
| Tone        | 0.0151           | 0.0146           |
| Transfer    | 0.0164           | 0.0154           |

simulatorと実機の1回目のfilter処理の差
3回の平均

| filter      | 1st device (sec) | 1st simulator (sec) |
+=============|==================|=====================+
| 1977        | 0.0180           | 2.0348              |
| Chrome      | 0.0159           | 0.6523              |
| Clarendon   | 0.0159           | 1.0200              |
| Fade        | 0.0159           | 0.6509              |
| HazeRemoval | 0.0181           | 0.7720              |
| Instant     | 0.0172           | 0.4845              |
| Linear      | 0.0146           | 0.3063              |
| Mono        | 0.0160           | 0.4311              |
| Nashville   | 0.0206           | 1.9360              |
| Noir        | 0.0153           | 0.2444              |
| Process     | 0.0162           | 0.2538              |
| Toaster     | 0.0177           | 1.0061              |
| Tonal       | 0.0162           | 0.2417              |
| Tone        | 0.0151           | 0.2053              |
| Transfer    | 0.0164           | 0.2363              |



## CIImage
* [iphone - Using a CIImage from CIColor in a CIFilter: getting empty image - Stack Overflow](https://stackoverflow.com/questions/10903066/using-a-ciimage-from-cicolor-in-a-cifilter-getting-empty-image)

## CIKernel
* [Swift 3.0 for Core Image Developers](http://flexmonkey.blogspot.jp/2016/05/swift-30-for-core-image-developers.html)
* [CIKernel を使用してCore Imageのカスタムフィルタをつくる - Qiita](https://qiita.com/shu223/items/6959dc7ba6ac0844340b)

## UIImageView
* [iphone - Crop UIImage to fit a frame image - Stack Overflow](https://stackoverflow.com/questions/14609132/crop-uiimage-to-fit-a-frame-image)

* Mode: Aspect Fill
* Drawing: Clip to bounds

## Reference
* [GitHub - robovm/apple-ios-samples](https://github.com/robovm/apple-ios-samples)
* [Swiftで実行時間計測 - Qiita](https://qiita.com/ken0nek/items/7577d26143a6fe4355f9)
* [XCODEでデバッグビルドとリリースビルドを切り替える方法 - Qiita](https://qiita.com/nakamurau1@github/items/d12a63c4f06d1a70a53d)
* [Tuning for Performance and Responsiveness](https://developer.apple.com/library/content/documentation/General/Conceptual/MOSXAppProgrammingGuide/Performance/Performance.html)
* [Performance Tips](https://developer.apple.com/library/content/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/PerformanceTips/PerformanceTips.html)
* [【iOS】パフォーマンス改善で参考にした記事まとめ（随時更新） - Qiita](https://qiita.com/xxxAIRINxxx/items/e7d7f6b16c01ce42b6ef)
* [Core Image Filter Reference](https://developer.apple.com/library/content/documentation/GraphicsImaging/Reference/CoreImageFilterReference/)
* [shader入門 -CIKernelでカスタムフィルター作成- | eureka tech blog](https://developers.eure.jp/tech/shader_introduction/)
* [Advanced Image Processing with Core Image](https://academy.realm.io/posts/tryswift-gladman-simon-advanced-core-image/)
* [GitHub - YuAo/Vivid: Filters and Utilities for Core Image](https://github.com/YuAo/Vivid)
* [PDF32000.book](http://wwwimages.adobe.com/content/dam/acom/en/devnet/pdf/PDF32000_2008.pdf)
* [GPUImage/GPUImageHazeFilter.m at 167b0389bc6e9dc4bb0121550f91d8d5d6412c53 · BradLarson/GPUImage](https://github.com/BradLarson/GPUImage/blob/167b0389bc6e9dc4bb0121550f91d8d5d6412c53/framework/Source/GPUImageHazeFilter.m)
