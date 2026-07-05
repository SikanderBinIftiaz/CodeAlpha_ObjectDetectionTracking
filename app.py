import cv2
import time
from ultralytics import YOLO

# ============================================
# Load YOLOv8 Small Model
# ============================================
print("Loading YOLOv8 Small Model...")
model = YOLO("yolov8s.pt")   # Downloads automatically the first time
print("Model Loaded Successfully!")

# ============================================
# Open DroidCam (Camera Index 1)
# ============================================
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Unable to open camera.")
    exit()

print("Camera Connected Successfully!")

previous_time = time.time()

while True:

    success, frame = cap.read()

    if not success:
        print("Failed to read frame.")
        break

    # Resize frame for faster processing
    frame = cv2.resize(frame, (640, 480))

    # Detect and Track
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
    fps = 1 / (current_time - previous_time)
    previous_time = current_time

    cv2.putText(
        annotated_frame,
        f"FPS: {int(fps)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        annotated_frame,
        "YOLOv8s - CodeAlpha Project",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    cv2.imshow("Object Detection & Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("Program Closed Successfully!")