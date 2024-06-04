from mediapipe.tasks import python
from mediapipe.tasks.python import vision


def get_detector():
    # Create an PoseLandmarker object.
    base_options = python.BaseOptions(model_asset_path='pose_landmarker.task')
    options = vision.PoseLandmarkerOptions(
        base_options=base_options,
        output_segmentation_masks=True)
    return vision.PoseLandmarker.create_from_options(options)


def get_landmarks(image):
    detector = get_detector()
    detection_result = detector.detect(image)
    return detection_result.pose_landmarks[0]
