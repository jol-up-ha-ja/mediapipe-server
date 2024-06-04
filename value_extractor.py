import numpy as np


def calculate_midpoint(point1, point2):
    xm = (point1[0] + point2[0]) / 2
    ym = (point1[1] + point2[1]) / 2
    zm = (point1[2] + point2[2]) / 2

    return xm, ym, zm


def calculate_angle(vector, standard_vector):
    # 벡터의 크기 계산
    vector_magnitude = np.linalg.norm(vector)
    horizon_magnitude = np.linalg.norm(standard_vector)

    # 벡터와 지평선 벡터 사이의 내적 계산
    dot_product = np.dot(vector, standard_vector)

    # 각도 계산 (라디안 단위)
    angle_rad = np.arccos(dot_product / (vector_magnitude * horizon_magnitude))

    # 각도를 도 단위로 변환
    angle_deg = np.degrees(angle_rad)

    return angle_deg


def calculate_angle_to_horizon(point1, point2):
    p1 = np.array(point1)
    p2 = np.array(point2)

    vector = p2 - p1
    horizon_vector = np.array([vector[0], vector[1], 0])

    return calculate_angle(vector, horizon_vector)


def calculate_angle_to_vertical(point1, point2):
    p1 = np.array(point1)
    p2 = np.array(point2)
    p1[1] = 0
    p2[1] = 0

    vector = p2 - p1
    vertical_vector = np.array([0, 0, 1])

    return calculate_angle(vector, vertical_vector)


def calculate_front_angle(langmarks):
    # 어깨, 골반, 무릎, 발목 순
    indices = [(11, 12), (23, 24), (25, 26), (27, 28)]
    extracted_data = []

    for r, l in indices:
        r_part = langmarks[r]
        l_part = langmarks[l]
        angle = calculate_angle_to_horizon([r_part.x, r_part.y, r_part.z], [l_part.x, l_part.y, l_part.z])
        extracted_data.append(round(angle, 3))

    return extracted_data


def calculate_side_angle(langmarks):
    # 어깨, 골반 순
    indices = [(11, 12), (23, 24)]
    mid = []
    # 목, 어깨 - 골반 순
    extracted_data = []

    mid.append((langmarks[0].x, langmarks[0].y, langmarks[0].z))
    for r, l in indices:
        r_part = langmarks[r]
        l_part = langmarks[l]
        mid_point = calculate_midpoint([r_part.x, r_part.y, r_part.z], [l_part.x, l_part.y, l_part.z])
        mid.append(mid_point)

    for i in range(2):
        angle = calculate_angle_to_vertical(mid[i], mid[i + 1])
        extracted_data.append(angle)

    return extracted_data
