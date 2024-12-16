# realsense_hand_depth
realsenseで手の深度の値を検出。書き換えれば中央だけや顔、全身の深度検出可能
## このプログラムを使う前に
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
このプログラムを実行すると、RGB 映像が表示され、手のランドマーク座標に対応する奥行きデータがコンソールに出力されます。
