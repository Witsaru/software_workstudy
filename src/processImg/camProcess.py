import sys
import os
import cv2
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from module import holistucModule as hm
from module import aruco
from module import calcuate
from module import collectData
from module import motion_gpt

class ProcessCam():
    def __init__(self) -> None:
        # self.listProcess_l = listProcess_l
        # self.listProcess_r = listProcess_r
        # self.lenprocess_l = len(self.listProcess_l)-1
        # self.lenprocess_r = len(self.listProcess_r)-1
        self.motion = motion_gpt.MotionTime()
        self.l_step = self.motion.nowProcess['L']
        self.r_step = self.motion.nowProcess['R']
        self.holi = hm.holistic_module()
        self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
        self.time_save_data = time.time()
        
    def Top_cam(self, image, listProcess_l, listProcess_r, test = False):
        self.listProcess_l = listProcess_l
        self.listProcess_r = listProcess_r
        self.lenprocess_l = len(self.listProcess_l)-1
        self.lenprocess_r = len(self.listProcess_r)-1
        # print(self.listProcess_l,self.listProcess_r, sep=" ")
        try :
            Id0 = aruco.memory_aruco(0, image, self.aruco_dict)
            Id10 = aruco.memory_aruco(10, image, self.aruco_dict)
            Id11 = aruco.memory_aruco(11, image, self.aruco_dict)
            Id12 = aruco.memory_aruco(12, image, self.aruco_dict)
            #create value ID AruCo

            IdPro_l = aruco.memory_aruco(self.listProcess_l[self.l_step], image, self.aruco_dict)
            IdPro_r = aruco.memory_aruco(self.listProcess_r[self.r_step], image, self.aruco_dict)
            
        except Exception as e:
            print(f"{e}:Don't can fine ID Aruco")
        try:
            self.holi.show_action(image)

            if len(self.holi.finepos(image)) > 0:
                l_index = self.holi.memory_pose[19]
                r_index = self.holi.memory_pose[20]

                if test:
                    self.motion.action_left(self.lenprocess_l, Id0, Id10, IdPro_l, l_index)
                    self.motion.action_right(self.lenprocess_r, Id11, Id12, IdPro_r, r_index)

        except:
            image

        # print(l_index)

    def Side_cam(self, image):
        try:
            self.holi.show_action(image)
        
        except:
            image

    def Front_cam(self, image):
        try:
            # self.holi.show_action(image)
            pass
        
        except:
            image


