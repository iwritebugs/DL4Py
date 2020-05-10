import cv2


class Preprocessor:

    def __init__(self, width, height, inter=cv2.INTER_AREA):
        self.width = width
        self.height = height
        self.inter = inter

    def process(self, image):
        return cv2.resize(src=image,
                          dsize=(self.width, self.height),
                          interpolation=self.inter)
