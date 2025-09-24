import argparse
from ultralytics import YOLO
import cv2

# Load trained YOLO model
model = YOLO("best.pt")  # Ensure best.pt is in the same folder

# Function to classify traffic
def classify_traffic(count):
    if count > 30:
        return "High Traffic"
    elif count > 20:
        return "Medium Traffic"
    else:
        return "Low Traffic"

def main(image_path):
    # Run YOLO prediction
    results = model(image_path)

    # Count vehicles
    count = 0
    for result in results:
        for _ in result.boxes:
            count += 1  

    # Traffic level
    traffic_status = classify_traffic(count)
    print(f"Detected Vehicles: {count}")
    print(f"Traffic Status: {traffic_status}")

    # Show labeled image
    for r in results:
        im_bgr = r.plot()
        cv2.imshow("Traffic Congestion Detection", im_bgr)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, required=True, help="Path to the test image")
    args = parser.parse_args()
    main(args.image)
