import cv2
import time
from ultralytics import YOLO

# =====================================================
# LOAD YOLOv8 MODEL
# =====================================================

print("=" * 60)
print("Loading YOLOv8s Model...")
model = YOLO("yolov8s.pt")
print("Model Loaded Successfully!")
print("=" * 60)

# =====================================================
# OPEN DROIDCAM (INDEX 2)
# =====================================================

CAMERA_INDEX = 2

cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)

if not cap.isOpened():
    print(f"Cannot Open Camera Index {CAMERA_INDEX}")
    exit()

# Camera Settings
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

print(f"Camera {CAMERA_INDEX} Connected Successfully!")
print("Press Q to Exit")

prev_time = time.time()

# =====================================================
# MAIN LOOP
# =====================================================

while True:

    ret, frame = cap.read()

    if not ret:
        continue

    frame = cv2.resize(frame, (640, 480))

    # Object Detection + Tracking
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        conf=0.55,
        imgsz=640,
        verbose=False
    )

    annotated_frame = results[0].plot()

    # FPS
    current_time = time.time()
    fps = int(1 / max(current_time - prev_time, 0.001))
    prev_time = current_time

    # Object Count
    try:
        object_count = len(results[0].boxes)
    except:
        object_count = 0

    # Display Information
    cv2.putText(
        annotated_frame,
        f"FPS : {fps}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        annotated_frame,
        f"Objects : {object_count}",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    cv2.putText(
        annotated_frame,
        "",
        (20, 115),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.putText(
        annotated_frame,
        "",
        (20, 155),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.imshow("", annotated_frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("Program Closed Successfully!")