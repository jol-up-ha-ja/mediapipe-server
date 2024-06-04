from analysis_image import get_landmarks
from get_image import load_img, delete_img
from value_extractor import calculate_side_angle, calculate_front_angle


def get_marks(img_key):
    image = load_img(img_key)
    landmarks = get_landmarks(image)
    delete_img(img_key)
    return landmarks


def analysis_front_image(img_key):
    landmarks = get_marks(img_key)
    return calculate_front_angle(landmarks)


def analysis_side_image(img_key):
    landmarks = get_marks(img_key)
    return calculate_side_angle(landmarks)
