from ultralytics import YOLO
from collections import Counter
from configs import CLASSES, ALLOWED_IMAGE_TYPES

class Model:
    def __init__(self, model='models/yolov8m.pt'):
        self.model = YOLO(model)

    def predict(self, filename):
        return self.model.predict(source=f'static/files/{filename}', save=True, project='static', name='results', line_thickness=2)


def label_count(results):
    counter = Counter(results[0].boxes.cls.cpu().numpy())
    for i in counter.copy():
        if i in CLASSES:
            counter[CLASSES[i].capitalize()] = counter.pop(i)
    return counter


def allowed_image(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGE_TYPES