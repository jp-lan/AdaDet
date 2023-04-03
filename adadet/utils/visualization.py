# Copyright (c) Alibaba, Inc. and its affiliates.
import cv2


def get_color(idx):
    idx = (idx + 1) * 3
    color = ((10 * idx) % 255, (20 * idx) % 255, (30 * idx) % 255)
    return color


def vis_bbox(img, bboxes):
    for i, box in enumerate(bboxes):
        x1, y1, x2, y2 = box
        color = get_color(i)
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
    return img


def vis_det_img(input_path, res):
    img = cv2.imread(input_path)
    unique_label = list(set(res['labels']))
    for idx in range(len(res['scores'])):
        x1, y1, x2, y2 = res['boxes'][idx]
        score = str(res['scores'][idx])
        label = str(res['labels'][idx])
        color = get_color(unique_label.index(label))
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
        cv2.putText(img, label, (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_PLAIN, 1, color)
        cv2.putText(img, score, (int(x1), int(y2) + 10),
                    cv2.FONT_HERSHEY_PLAIN, 1, color)
    return img


def vis_face_img(input_path, res):
    img = cv2.imread(input_path)
    for idx in range(len(res['scores'])):
        x1, y1, x2, y2 = res['boxes'][idx]
        score = str(res['scores'][idx])
        color = get_color(5)
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
        if 'keypoints' in res.keys() and res['keypoints']:
            kp = res['keypoints'][idx]
            for i in range(1, len(kp), 2):
                cv2.circle(img, (int(kp[i - 1]), int(kp[i])), 2, color, -1)
        cv2.putText(img, score, (int(x1), int(y2) + 10),
                    cv2.FONT_HERSHEY_PLAIN, 1, color)
    return img
