import cv2


class CameraCapture:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)

    def get_camera_image(self):
        is_available, image = self.capture.read()
        if is_available:
            return image
        else:
            raise RuntimeError('Camera problems occurred!')

    def __del__(self):
        self.capture.release()
