<<<<<<< HEAD
import argparse
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Function to classify traffic
def classify_traffic(count):
    if count > 30:
        return "High Traffic"
    elif count > 20:
        return "Medium Traffic"
    else:
        return "Low Traffic"

def main(image_path, model_path):
    # Load YOLO model
    model = YOLO(model_path)

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

    # Save and show labeled image
    for r in results:
        im_bgr = r.plot()

        # Save output
        output_path = "output.jpg"
        cv2.imwrite(output_path, im_bgr)
        print(f"Result saved as {output_path}")

        # Convert BGR to RGB for matplotlib
        im_rgb = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)

        # Show inline
        plt.imshow(im_rgb)
        plt.axis("off")
        plt.title("Traffic Congestion Detection")
        plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, required=True, help="Path to the test image")
    parser.add_argument(
        "--model",
        type=str,
        default="v8/best.pt",
        choices=["v8/best.pt", "v10/best.pt", "v12/best.pt"],
        help="Choose which model to use (default: v8)"
    )
    args = parser.parse_args()
    main(args.image, args.model)

