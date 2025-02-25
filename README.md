# Video Object Detection using YOLO

This Python script performs real-time object detection in a video file using the YOLOv8 model. It detects objects like people and cars and can be configured to only show detections of people. Additionally, you can adjust whether you want the video to be displayed during processing.

## Sample

![sample](https://github.com/adnerscarpelini/video-object-detection-yolo/blob/main/sample.gif)

## Features

- Object detection in a video (can detect people and cars).
- Option to display the video with bounding boxes around detected objects.
- Option to only detect people.
- Ability to save detection timestamps to a file.
- Easy-to-use interface for setting up and running the detection.

## Requirements

Make sure to have the following installed:

- Python 3.7 or higher
- OpenCV (for video processing)
- Ultralytics YOLOv8 (for object detection)

### Installing dependencies

To set up your environment, you can use the following steps:

1. Clone or download this repository.

2. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:

   **On Windows:**

   ```
   venv\Scripts\activate
   ```

   **On macOS/Linux:**

   ```
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, you can manually install the necessary packages by running:

   ```
   pip install opencv-python ultralytics
   ```

## Configuring the Script

1. Download the YOLOv8 model:
   - The script will automatically download the `yolov8n.pt` model when run for the first time. Ensure you have internet access for this.
2. Set the path to your video:
   - Change the `video_path` variable in the script to point to your video file.
3. Configure detection settings:
   - **`exibir_video`**: Set this variable to `True` if you want to view the video with bounding boxes around detected objects in real-time. Set it to `False` to process the video without showing it.
   - **`exibir_apenas_pessoas`**: Set this to `True` to detect only people, or `False` to detect both people and cars.

## Running the Script

Once you have set everything up, you can run the script using the following command:

```
python detect_video_objects.py
```

This will start the detection process. The script will:

1. Analyze the video and detect objects in each frame.
2. Display the video with bounding boxes if `exibir_video` is set to `True`.
3. Save the timestamps of detected objects (people or cars) to a file called `horarios_detectados.txt`.

### Stopping the Script

To stop the script while it's running, press the `q` key when the video window is displayed.

## Output

- A file named `horarios_detectados.txt` will be generated. This file contains the timestamps (in seconds) of each detection event.
