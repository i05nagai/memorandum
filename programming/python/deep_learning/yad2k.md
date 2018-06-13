---
title: YAD2K
---

## YAD2K
Yet Another Darknet 2 Keras
Yoloを実装したDarknetのKeras interface.

```
git clone https://github.com/allanzelener/yad2k.git
cd yad2k

# [Option 1] To replicate the conda environment:
conda env create -f environment.yml
source activate yad2k
# [Option 2] Install everything globaly.
pip install numpy h5py pillow
pip install tensorflow-gpu  # CPU-only: conda install -c conda-forge tensorflow
pip install keras # Possibly older release: conda install keras
```

```
curl -L -O http://pjreddie.com/media/files/yolo.weights
curl -L -O https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolo.cfg
# wget http://pjreddie.com/media/files/yolo.weights
# wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolo.cfg
./yad2k.py yolo.cfg yolo.weights model_data/yolo.h5
./test_yolo.py model_data/yolo.h5  # output in images/out/
```

## CLI
yad2k

* `--test_path`
* `--output_path`

## Training your own data set
* [How to train YOLOv2 to detect custom objects](https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/)




## Reference
* [GitHub - allanzelener/YAD2K: YAD2K: Yet Another Darknet 2 Keras](https://github.com/allanzelener/YAD2K)
