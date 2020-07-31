import cv2
from CameraCapture import CameraCapture

if __name__ == '__main__':
    print('Hello, Naruto Project!')

    camera_capture = CameraCapture()

    while True:
        image = camera_capture.get_camera_image()
        cv2.imshow('image', image)
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()
