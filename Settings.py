import os
import json

class Settings:
    __ROI_RECT_STRING = 'roi_rect'
    __BLUR_VALUE_STRING = 'blur_value'
    __CANNNY_THRESHOLD_STRING = 'canny_values'
    __MINIMAL_CONTOUR_LENGTH_STRING = 'minimal_contour_length'
    __APPROXIMATION_EPSILON_STRING = 'approximation_epsilon'
    __PAPER_SIZE_STRING = 'paper_size'
    __CONTOUR_APPEARANCE_STRING = 'appearance_filled'

    # From camera class
    __CAMERA_ID_STRING = 'camera_id'
    __RESOLUTION_WIDTH_STRING = 'resolution_width'
    __RESOLUTION_HEIGHT_STRING = 'resolution_height'

    # Rrom robot class
    __HOST_STRING = 'host'
    __PORT_STRING = 'port'
    __TIMEOUT_STRING = 'timeout'
    __DEBUG_MODE_STRING = 'debug_mode'
    __SEPARATOR_STRING = 'separator'

    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


    def __load_defaults(self):
        self.roi_rect = [0, 0, 297, 210]
        self.paper_size = (210, 297)
        self.blur_value = 1
        self.canny_threshold = (100, 100)
        self.minimal_contour_length = 10
        self.approximation_epsilon = 100
        self.appearance_filled = True
        #
        self.camera_id = 0
        self.camera_width = 1920
        self.camera_height = 1080
        #
        self.robot_host = ''
        self.robot_port = 48569
        self.robot_timeout = 5
        self.robot_debug_mode = True
        self.robot_separator = ';'
        self.save_settings()

    def __load_settings(self):
        try: 
            with open(self.__config_path, 'r') as file:
                config = json.load(file)
            self.roi_rect = config[self.__ROI_RECT_STRING]
            self.blur_value = config[self.__BLUR_VALUE_STRING] 
            self.canny_threshold = config[self.__CANNNY_THRESHOLD_STRING] 
            self.minimal_contour_length = config[self.__MINIMAL_CONTOUR_LENGTH_STRING] 
            self.approximation_epsilon = config[self.__APPROXIMATION_EPSILON_STRING] 
            self.paper_size = config[self.__PAPER_SIZE_STRING] 
            self.appearance_filled = config[self.__CONTOUR_APPEARANCE_STRING] 
            #
            self.camera_id = config[self.__CAMERA_ID_STRING]
            self.camera_width = config[self.__RESOLUTION_WIDTH_STRING]
            self.camera_height = config[self.__RESOLUTION_HEIGHT_STRING]
            #
            self.robot_host = config[self.__HOST_STRING]
            self.robot_port = config[self.__PORT_STRING]
            self.robot_timeout = config[self.__TIMEOUT_STRING]
            self.robot_debug_mode = config[self.__DEBUG_MODE_STRING]
            self.robot_separator = config[self.__SEPARATOR_STRING]
        except Exception as e:
            print(e)
            self.__load_defaults()

    def save_settings(self):
        try:
            with open(self.__config_path, 'r') as file:
                    config = json.load(file)
        except Exception as e:
                print(e)
                config = {}
                
        config[self.__ROI_RECT_STRING] = self.roi_rect
        config[self.__BLUR_VALUE_STRING] = self.blur_value
        config[self.__CANNNY_THRESHOLD_STRING] = self.canny_threshold
        config[self.__MINIMAL_CONTOUR_LENGTH_STRING] = self.minimal_contour_length
        config[self.__APPROXIMATION_EPSILON_STRING] = self.approximation_epsilon
        config[self.__PAPER_SIZE_STRING]  = self.paper_size 
        config[self.__CONTOUR_APPEARANCE_STRING] = self.appearance_filled 
        #
        config[self.__CAMERA_ID_STRING] = self.camera_id
        config[self.__RESOLUTION_WIDTH_STRING] = self.camera_width
        config[self.__RESOLUTION_HEIGHT_STRING] = self.camera_height
        #
        config[self.__HOST_STRING] = self.robot_host
        config[self.__PORT_STRING] = self.robot_port
        config[self.__TIMEOUT_STRING] = self.robot_timeout
        config[self.__DEBUG_MODE_STRING] = self.robot_debug_mode
        config[self.__SEPARATOR_STRING] = self.robot_separator


        with open(self.__config_path, 'w') as file:
            json.dump(config, file, indent=4)

    def init(self, config_path = 'config/settings.json'):
        self.__config_path = config_path
        self.__config_dir, self.__config_file = os.path.split(config_path)
        if os.path.exists(self.__config_path):
            self.__load_settings()
        else:
            if not os.path.exists(self.__config_dir): os.makedirs(self.__config_dir)
            self.__load_defaults()

if __name__ == '__main__':
     settings = Settings()
     settings.init(config_path='config/parameters.json')
