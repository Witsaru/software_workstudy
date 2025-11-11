import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from module import time_F
from module import calcuate as cal

class MotionTime:
    DISTANCE_THRESHOLD = 50  # Define a threshold as a class constant

    def __init__(self):
        self.forward = {'L': True, 'R': True}
        self.backward = {'L': False, 'R': False}
        self.start = {'L': False, 'R': False}

        self.timers = {
            'L': {'fine': time_F.Timer(), 'dis': time_F.Timer(), 'assembly': time_F.Timer()},
            'R': {'fine': time_F.Timer(), 'dis': time_F.Timer(), 'assembly': time_F.Timer()},
        }

        self.data = {'L': {"time_assembly_left": []}, 'R': {"time_assembly_right": []}}
        self.nowProcess = {'L': 0, 'R': 0}
        self.items = {'L': 0, 'R': 0}

    def action(self, side, lenProcess, point_base, point_sto, point_process, point_index):
        self._sub_time(side)

        if self.nowProcess[side] >= lenProcess:
            if cal.findDistance(point_index, point_process) <= self.DISTANCE_THRESHOLD:
                if self.forward[side] and not self.backward[side]:
                    self.timers[side]['fine'].start()
                    self.forward[side] = False

            elif not self.forward[side] and not self.backward[side]:
                if cal.findDistance(point_index, point_process) >= self.DISTANCE_THRESHOLD:
                    key_wait = f"Wait at process {self.nowProcess[side] + 1}"
                    self.data[side][key_wait].append(self.timers[side]['fine'].stop())
                    self.timers[side]['dis'].start()
                    self.backward[side] = True

            elif self.backward[side] and not self.forward[side]:
                if cal.findDistance(point_index, point_base) >= self.DISTANCE_THRESHOLD:
                    key_time = f"Time distance 0to{self.nowProcess[side] + 1}"
                    self.data[side][key_time].append(self.timers[side]['dis'].stop())
                    self.nowProcess[side] += 1
                    self.backward[side] = False
                    self.forward[side] = True

        else:
            if self.forward[side] and not self.backward[side]:
                if cal.findDistance(point_index, point_base) <= self.DISTANCE_THRESHOLD:
                    self.timers[side]['assembly'].start()

                elif cal.findDistance(point_index, point_base) >= self.DISTANCE_THRESHOLD:
                    if cal.findDistance(point_index, point_sto) <= self.DISTANCE_THRESHOLD:
                        self.data[side][f"time_assembly_{'left' if side == 'L' else 'right'}"].append(
                            self.timers[side]['assembly'].stop()
                        )
                        self.nowProcess[side] = 0

    def action_left(self, *args):
        self.action('L', *args)

    def action_right(self, *args):
        self.action('R', *args)

    def main_time(self, side):
        return self.data[side]

    def main_time_left(self):
        return self.main_time('L')

    def main_time_right(self):
        return self.main_time('R')

    def _sub_time(self, side):
        key1 = f"Time distance 0to{self.nowProcess[side] + 1}"
        key2 = f"Wait at process {self.nowProcess[side] + 1}"

        if key1 not in self.data[side]:
            self.data[side][key1] = []

        if key2 not in self.data[side]:
            self.data[side][key2] = []
