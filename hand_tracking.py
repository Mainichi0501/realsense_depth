import time
import cv2
import mediapipe as mp
import pyrealsense2 as rs
import numpy as np

# MediaPipe Hand Trackingモジュールの初期化
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# RealSenseカメラの設定
pipeline = rs.pipeline()
config = rs.config()

# カメラの設定（解像度を下げる）
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)  # 低解像度に設定
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)  # 低解像度に設定

# パイプラインの開始
pipeline.start(config)

# 少し待機してからフレームを取得
time.sleep(2)  # 2秒待機してカメラが初期化されるのを待つ

# フレームを処理するループ
while True:
    try:
        frames = pipeline.wait_for_frames()
    except RuntimeError as e:
        print(f"Error: {e}")
        continue

    # 深度フレームとカラーフレームの取得
    depth_frame = frames.get_depth_frame()
    color_frame = frames.get_color_frame()

    if not color_frame:
        continue

    # OpenCVでフレームを処理
    color_image = np.asanyarray(color_frame.get_data())

    # 手の検出
    results = hands.process(color_image)

    # 手が検出された場合、手の位置を描画
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # 手のひらの中心に対応するランドマーク（通常、ランドマーク番号9が中心）
            center_landmark = hand_landmarks.landmark[9]  # 手のひらの中心（ランドマーク番号9）

            # 画像内の座標に変換
            h, w, c = color_image.shape
            cx, cy = int(center_landmark.x * w), int(center_landmark.y * h)

            # 深度情報を取得（手のひらの中心に対応する深度値）
            depth_value = depth_frame.get_distance(cx, cy)

            # 手の中心の座標と深度値を表示
            print(f"Hand center (x, y): ({cx}, {cy}), Depth: {depth_value} meters")

            # 手の中心を画像に描画
            cv2.circle(color_image, (cx, cy), 5, (0, 255, 0), -1)

    # 画像を表示
    cv2.imshow('Hand Tracking', color_image)

    # 'q' キーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
pipeline.stop()
cv2.destroyAllWindows()

