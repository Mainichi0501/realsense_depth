# realsense_hand_depth
このプログラムはMediaPipeとRealSenseを使用した手の位置と奥行きの検出プログラムです。
## 機能
- RealSenseカメラで手の位置と奥行きを検出。
- MediaPipe Hand TrackingとRealSense深度データの組み合わせ。
## このプログラムを使う前に
### 必要環境
- Python 3.8以上
- mediapipe
- pyrealsense2
- OpenCV
### 必要なライブラリインストール
  
    # RealSense SDK (librealsense) インストール
    sudo apt-get install librealsense2-dkms librealsense2-utils librealsense2-dev

    # Python ライブラリ（pyrealsense2）
    pip install pyrealsense2

    # MediaPipe（手の認識用）
    pip install mediapipe

# このプログラムの使い方
## インストール
```
git clone https://github.com/Mainichi0501/realsense_depth/blob/main/hand_tracking.py
```
## 実行
```
python3 hand_tracking.py
```
このプログラムを実行すると、RGB 映像が表示され、手のランドマーク座標に対応する奥行きデータがコンソールに出力されます。

# ライセンス
(C) 2024 Mainichi

このプログラムは、[Apache License 2.0](./LICENSE) に基づいて公開されています。

このプログラムでは、以下のライブラリを使用しています：
- [MediaPipe](https://github.com/google/mediapipe)（Apache License 2.0）
- [Intel RealSense SDK](https://github.com/IntelRealSense/librealsense)（Apache License 2.0）

ライセンスの詳細については [LICENSE](./LICENSE) ファイルをご確認ください。
