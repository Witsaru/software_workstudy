import math
import numpy as np

import csv

def findDistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    try:
        dist = int(math.sqrt((x2-x1)**2 + (y2-y1)**2))
        return dist
    except:
        pass

def findAngle(p1,p2):
    x1, y1 = p1
    x2, y2 = p2
    try:
        theta = math.acos((y2-y1)*(-y1) / (math.sqrt(
            (x2 - x1) ** 2 +(y2 - y1)**2)*y1))
        # theta = math.atan2(y2 - y1 , x2 - x1)
        degree = round((180/math.pi)*theta,3)
        return degree
    except:
        pass

def calcu_stantime(timelist, ratfac, allowa):

    aver = np.average(timelist)
    nor = round(aver*(ratfac/100),3)
    sta = round(nor * (1+(allowa/100)),3)

    return [aver, nor, sta]