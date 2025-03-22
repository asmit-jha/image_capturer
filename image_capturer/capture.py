# image_capturer/capture.py
import cv2

def capture_image(output_path='output.jpg'):
    """Capture image from the default camera and save it."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Could not open webcam")
        return

    ret, frame = cap.read()
    if ret:
        cv2.imwrite(output_path, frame)
        print(f"[SUCCESS] Image saved to {output_path}")
    else:
        print("[ERROR] Failed to capture image")

    cap.release()

if __name__ == "__main__":
    capture_image()
