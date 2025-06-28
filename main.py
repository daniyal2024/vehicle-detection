import cv2
from ultralytics import YOLO
from tracker import *

tracker = EuclideanDistTracker()
model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture("trafix.mp4")

# ROI coordinates
y1_roi, y2_roi = 170, 1200
x1_roi, x2_roi = 500, 1200

while True:
    ret, frame = cap.read()
    if not ret:
        break

    roi = frame[y1_roi:y2_roi, x1_roi:x2_roi]

    # Run YOLOv8 inference on ROI only
    results = model(roi)[0]

    detections = []
    for box in results.boxes:
        cls = int(box.cls[0])
        # Optional: filter by class (car=2, motorcycle=3, truck=7)
        if cls in [2, 3, 7]:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            w, h = x2 - x1, y2 - y1
            # Adjust coordinates to original frame
            detections.append([x1 + x1_roi, y1 + y1_roi, w, h])

    # Update tracker and draw results
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, str(id), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Show only the ROI with tracking
    #cv2.imshow("ROI Tracking", frame[y1_roi:y2_roi, x1_roi:x2_roi])
    
    cv2.imshow("YOLOv8 + Tracking", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()