import os
import json
import socket as sockets
from threading import Thread


class Robot(Thread):
    
    __HOST_STRING = 'host'
    __PORT_STRING = 'port'
    __TIMEOUT_STRING = 'timeout'
    __DEBUG_MODE_STRING = 'debug_mode'
    __SEPARATOR_STRING = 'separator'

    def __init__(self, config_path = 'config/robot.json'):
        Thread.__init__(self)

        self.__config_path = config_path
        self.__config_dir, self.__config_file = os.path.split(config_path)
        if os.path.exists(self.__config_path):
            self.__load_settings()
        else:
            if not os.path.exists(self.__config_dir): os.makedirs(self.__config_dir)
            self.__load_defaults()

        self.__data = ''
        self.is_connected = False

    def __load_defaults(self):
        self.host = ''
        self.port = 48569
        self.timeout = 5
        self.debug_mode = True
        self.separator = ';'
        
        self.save_settings()

    def __load_settings(self):
        try:
            with open(self.__config_path, 'r') as file:
                config = json.load(file)
                self.host = config[self.__HOST_STRING]
                self.port = config[self.__PORT_STRING]
                self.timeout = config[self.__TIMEOUT_STRING]
                self.debug_mode = config[self.__DEBUG_MODE_STRING]
                self.separator = config[self.__SEPARATOR_STRING]
        except Exception as e:
            print(e)
            self.__load_defaults()


    def __print_debug(self, msg):
        if self.debug_mode: print(msg)


    def __connect(self):
        print("Server started. Waiting for connect...")
        socket = sockets.socket(sockets.AF_INET, sockets.SOCK_STREAM)
        socket.bind((self.host, self.port))
        socket.listen()
        self.__connection, ip_address = socket.accept()
        self.__connection.settimeout(self.timeout)
        print(f"Client with IP {ip_address} was connected")
        self.is_connected = True

    def __thread(self):
        __wait = lambda: self.__connection.sendall(b'wait;')
        self.__connect()
        while True:
            try:
                if self.__data != '':
                    self.__connection.sendall(self.__data.encode())
                    self.__data = ''
                else:
                    __wait()
                received_data = self.__connection.recv(1024)
                self.__print_debug(received_data)
            except Exception as e:
                self.__print_debug(e)
                self.is_connected = False
                try:
                    self.__connection.close()
                except Exception as e:
                    self.__print_debug(e)
                print("Connection broken or timeout exceeded. Restarting server")
                self.__connect()

    def run(self):
        self.__thread()
        self.__print_debug("RobotData thread started")

    def send(self, data):
        if isinstance(data, str):
            self.__data = data + self.separator
        if isinstance(data, list):
            self.__data = self.separator.join(map(str, data)) + self.separator


    def save_settings(self):
        try:
            with open(self.__config_path, 'r') as file:
                    config = json.load(file)
        except Exception as e:
                print(e)
                config = {}

        config[self.__HOST_STRING] = self.host
        config[self.__PORT_STRING] = self.port
        config[self.__TIMEOUT_STRING] = self.timeout
        config[self.__DEBUG_MODE_STRING] = self.debug_mode
        config[self.__SEPARATOR_STRING] = self.separator

        with open(self.__config_path, 'w') as file:
            json.dump(config, file, indent=4)




if __name__ == "__main__":
    import cv2
    rdt = Robot(config_path='config/parameters.json')
    rdt.start()
    while not rdt.is_connected: pass
    cv2.namedWindow("test")
    while True:
        key = cv2.waitKey(100)
        if key == ord('s'):
            rdt.send("a123")
        if key == ord('d'):
            rdt.send([1213, 'hhgf', 3.0])
    # for i in range(10):
    #     rdt.send("a123")
    #     time.sleep(1)