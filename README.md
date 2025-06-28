# Vehicle Detection and Tracking with YOLOv8

This project detects and tracks vehicles (cars, motorcycles, trucks) in a video using YOLOv8 and a simple Euclidean distance tracker.

## Features

- Detects cars, motorcycles, and trucks in a specified region of interest (ROI)
- Assigns unique IDs to each detected object for tracking
- Uses YOLOv8 for detection and OpenCV for video processing

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/vehicle-detection.git
cd vehicle-detection
```

### 2. Create and activate a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install ultralytics opencv-python
pip install "numpy<2"
```

### 4. Download YOLOv8 model

The model (`yolov8n.pt`) will be downloaded automatically on first run.  
You can also download it manually from [Ultralytics YOLOv8 Releases](https://github.com/ultralytics/ultralytics/releases).

### 5. Add your video

Place your video file (e.g., `trafix.mp4`) in the project directory.

## Usage

```bash
python main.py
```

- Press `ESC` to exit the video window.

## File Structure

```
vehicle-detection/
├── main.py
├── tracker.py
├── trafix.mp4
├── README.md
└── .venv/
```

## Notes

- Make sure your video file name matches the one in `main.py`.
- The code tracks only objects detected within the ROI defined in `main.py`.
- For best results, use clear traffic videos.

## License

MIT License

