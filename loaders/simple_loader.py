import logging
import os

import cv2


class Loader:

    def __init__(self, preprocessors=None):
        self.preprocessors = preprocessors if preprocessors is not None else []

    def load(self, images):
        data = []
        labels = []

        raw_data = []
        for i, image in enumerate(images):
            if i % 100 == 0:
                info_msg = f'Loading {i} of {len(images)}'
                logging.info(info_msg)
            raw_data.append(cv2.imread(image))
            for preprocessor in self.preprocessors:
                raw_data = preprocessor.process(raw_data)
            data.append(raw_data)
            labels.append(image.split(os.path.sep)[-2])

        return data, labels

