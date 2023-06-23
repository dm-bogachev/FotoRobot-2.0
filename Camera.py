import cv2
import json
import os.path

class Camera:

    __CAMERA_ID_STRING = 'camera_id'
    __RESOLUTION_WIDTH_STRING = 'resolution_width'
    __RESOLUTION_HEIGHT_STRING = 'resolution_height'

    def __init__(self, config_path = 'config/camera.json'):
        self.__config_path = config_path
        self.__config_dir, self.__config_file = os.path.split(config_path)
        if os.path.exists(self.__config_path):
            self.__load_settings()
        else:
            if not os.path.exists(self.__config_dir): os.makedirs(self.__config_dir)
            self.__load_defaults()
        print('Camera initialization begin')
        self.__camera_init()
        print(f'Camera initialization finished. Succeed = {self.is_active}')

    def __load_defaults(self):
        self.id = 0
        self.width = 1920
        self.height = 1080
        
        self.save_settings()

    def __load_settings(self):
        try: 
            with open(self.__config_path, 'r') as file:
                config = json.load(file)
            self.id = config[self.__CAMERA_ID_STRING]
            self.width = config[self.__RESOLUTION_WIDTH_STRING]
            self.height = config[self.__RESOLUTION_HEIGHT_STRING]
        except Exception as e:
            print(e)
            self.__load_defaults()

    def __camera_init(self):
        self.__camera = cv2.VideoCapture(self.id)
        self.__camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.__camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)

        _, temp = self.__camera.read()

        if not _:
            self.is_active = False
            return

        height, width, dim = temp.shape
        if height != self.height or width != self.width:
            print(f'Unable to set resolution {self.width}x{self.height}')
            print(f'Resolution {width}x{height} is set')
        self.is_active = True

    def get_frame(self):
        ret, frame = self.__camera.read()
        if ret:
            return frame
        print('Bad frame received!!!')
        return None

    def save_settings(self):
        try:
            with open(self.__config_path, 'r') as file:
                    config = json.load(file)
        except Exception as e:
                print(e)
                config = {}

        config[self.__CAMERA_ID_STRING] = self.id
        config[self.__RESOLUTION_WIDTH_STRING] = self.width
        config[self.__RESOLUTION_HEIGHT_STRING] = self.height

        with open(self.__config_path, 'w') as file:
            json.dump(config, file, indent=4)


if __name__ == '__main__':
    camera = Camera(config_path='config/parameters.json')
    cv2.namedWindow('Frame', cv2.WINDOW_KEEPRATIO)
    while True:
        frame = camera.get_frame()
        if type(frame) is not type(None):
            cv2.imshow('Frame', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break