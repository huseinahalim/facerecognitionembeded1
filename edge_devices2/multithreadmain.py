import cv2
import numpy as np
import argparse
import threading
import time

# Function to capture video frames in a separate thread
def capture_frames():
    while True:
        ret, img = cam.read()
        if not ret:
            break
        frame_queue.put(img)

# Function to process frames
def process_frames():
    while True:
        img = frame_queue.get()
        if img is None:
            break
        start_time = time.time()
        
        # ... Your frame processing code ...

        end_time = time.time()
        frame_time = end_time - start_time
        print(f"Inference time for frame: {frame_time:.4f} seconds")

# Initialize a queue for frames
frame_queue = queue.Queue(maxsize=5)  # Adjust the queue size as needed

# Create and start threads
capture_thread = threading.Thread(target=capture_frames)
process_thread = threading.Thread(target=process_frames)

# Start the threads
capture_thread.start()
process_thread.start()

# Wait for threads to finish
capture_thread.join()
process_thread.join()

# Release resources
cam.release()
