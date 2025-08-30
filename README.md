# Basketball Video Analysis

This project detects, tracks, and analyzes basketball actions from video footage. It uses object detection models to identify the ball, players, and extract advanced statistics.

## Project Structure

- **basketball_analysis/**  
  - `main.py`: Main entry point  
  - **ball_aquisition/**: Ball acquisition  
  - **drawers/**: Visualization and annotation  
  - **input_videos/**: Source videos for analysis  
  - **models/**: Trained detection models  
  - **output_videos/**: Annotated output videos  
  - **pass_and_interception_detector/**: Pass and interception detection  
  - **stubs/**: Saved detections for faster execution
  - **team_assigner/**: Assign players to teams  
  - **trackers/**: Object tracking  
  - **training_notebook/**: Model training notebooks  
  - **utils/**: Utility functions 

## Installation

1. Clone the repository:
   ```sh
   git clone <repo_url>
   cd object_detection-projects
   ```
2. Install Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   Notebooks use packages like `ultralytics`, `opencv-python`, `roboflow`, etc.

## Usage

1. Place your videos in the `input_videos/` folder.
2. Run the analysis:
   ```sh
   python basketball_analysis/main.py
   ```
3. Annotated results will be saved in `output_videos/`.

## Model Training

Jupyter notebooks are available in [`basketball_analysis/training_notebook`](basketball_analysis/training_notebook) for training or fine-tuning detection models (ball, players, etc.).

## Key Folders

- `models/`: YOLO or other detection models.
- `output_videos/`: Generated annotated videos.
- `stubs/`: Saved detections for faster execution.
