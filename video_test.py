import cv2
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8s.pt")

# Open video
cap = cv2.VideoCapture("videos/sample.mp4")   # Change filename if needed

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Video Finished!")
        break

    # Resize frame
    frame = cv2.resize(frame, (640, 480))

    # Detect and track
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        conf=0.55,
        verbose=False
    )

    annotated_frame = results[0].plot()

    cv2.imshow("Video Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()