import cv2

for i in range(10):
    print(f"\nTrying Camera Index: {i}")

    cap = cv2.VideoCapture(i)

    if not cap.isOpened():
        print("Not Available")
        continue

    print("Opened Successfully")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.putText(
            frame,
            f"Camera Index: {i}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        cv2.imshow(f"Camera {i}", frame)

        key = cv2.waitKey(1)

        if key == ord("n"):
            break

        if key == ord("q"):
            cap.release()
            cv2.destroyAllWindows()
            exit()

    cap.release()
    cv2.destroyAllWindows()

print("Finished")