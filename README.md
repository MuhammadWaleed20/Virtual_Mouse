# AI Virtual Hand-Tracking Mouse

A computer vision project that allows users to control their operating system's mouse using hand gestures captured via a standard webcam. 

## Features
* **Cursor Movement:** Tracks the index finger using MediaPipe to drive the mouse.
* **Click Detection:** Calculates the real-time distance between the thumb and index finger to trigger OS-level left clicks.
* **Movement Smoothing:** Utilizes a low-pass interpolation filter to eliminate coordinate micro-jitter for fluid cursor control.

## Tech Stack
* Python 3.11
* OpenCV (cv2) - Video capture and rendering
* MediaPipe - Hand landmark machine learning model
* PyAutoGUI - Operating system automation

## Setup Instructions
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment
4. Install dependencies: `pip install -r requirements.txt`
5. Run the application: `python main.py`