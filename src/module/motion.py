from module.time_F import Timer
import calcuate as cal

class Motion_time():

    def __init__(self):
        self.forwardL = True
        self.backL = False
        self.startL = False

        self.forwardR = True
        self.backR = False
        self.startR = False

        self.time_fineL = Timer()
        self.time_disL = Timer()
        self.time_assemblyL = Timer()

        self.time_fineR = Timer()
        self.time_disR = Timer()
        self.time_assemblyR = Timer()

        self.timefine_waitL =[]
        self.dataTL = {
            "time_assembly_left" : []
        }
        self.nowProcsseL = 0

        self.timefine_waitR =[]
        self.dataTR = {
            "time_assembly_right" : []
        }
        self.nowProcsseR = 0

        self.itemL = 0
        self.itemR = 0

    def action_left(self, lenprocsseL, point_base, point_sto, point_procsseL, point_indexL):
        self.sub_time_left()

        if self.nowProcsseL >= lenprocsseL:

            if cal.findDistance(point_indexL, point_procsseL) <= 50:
                if self.forwardL and (not self.backL) :
                    self.time_fineL.start()
                    self.forwardL = False

            elif not self.forwardL and (not self.backL):
                if cal.findDistance(point_indexL, point_procsseL) >= 50:
                    self.dataTL[f"Wait at process {self.nowProcsseL+1}"].append(self.time_fineL.stop())
                    self.time_disL.start()
                    self.backL = True

            elif self.backL and (not self.forwardL):
                if(cal.findDistance(point_indexL, point_base) >= 50):
                    self.dataTL[f"Time distance 0to{self.nowProcsseL+1}"].append(self.time_disL.stop())
                    self.nowProcsseL+=1
                    self.backL = False
                    self.forwardL = True

        else:

            if self.forwardL and (not self.backL):
                if(cal.findDistance(point_indexL, point_base) <= 50):
                    self.time_assemblyL.start()

                elif cal.findDistance(point_indexL, point_base) >= 50:
                    if cal.findDistance(point_indexL, point_sto) <= 50:
                        self.dataTL['time_assembly_left'].append(self.time_assemblyL.stop())
                        self.nowProcsseL = 0


    def action_rigth(self, lenprocsseR, point_base, point_sto, point_procsseR, point_indexR):
        self.sub_time_rigth()

        if self.nowProcsseL >= lenprocsseR:

            if cal.findDistance(point_indexR, point_procsseR) <= 50:
                if self.forwardR and (not self.backR) :
                    self.time_fineR.start()
                    self.forwardR = False

            elif not self.forwardR and (not self.backR):
                if cal.findDistance(point_indexR, point_procsseR) >= 50:
                    self.dataTR[f"Wait at process {self.nowProcsseR+1}"].append(self.time_fineR.stop())
                    self.time_disR.start()
                    self.backR = True

            elif self.backR and (not self.forwardR):
                if(cal.findDistance(point_indexR, point_base) >= 50):
                    self.dataTR[f"Time distance 0to{self.nowProcsseR+1}"].append(self.time_disR.stop())
                    self.nowProcsseR+=1
                    self.backR = False
                    self.forwardR = True

        else:

            if self.forwardR and (not self.backR):
                if(cal.findDistance(point_indexR, point_base) <= 50):
                    self.time_assemblyR.start()

                elif cal.findDistance(point_indexR, point_base) >= 50:
                    if cal.findDistance(point_indexR, point_sto) <= 50:
                        self.dataTR['time_assembly_right'].append(self.time_assemblyR.stop())
                        self.nowProcsseR = 0

    
    def main_time_left(self):
        return self.dataTL

    def main_time_rigth(self):
        return self.dataTR

    def sub_time_left(self):
        key1 = f"Time distance 0to{self.nowProcsseL+1}"
        key2 = f"Wait at process {self.nowProcsseL+1}"

        if key1 not in self.dataTL:
            self.dataTL[key1] = []

        if key2 not in self.dataTL:
            self.dataTL[key2] = []

    def sub_time_rigth(self):
        key1 = f"Time distance 0to{self.nowProcsseR+1}"
        key2 = f"Wait at process {self.nowProcsseR+1}"

        if key1 not in self.dataTR:
            self.dataTL[key1] = []

        if key2 not in self.dataTR:
            self.dataTL[key2] = []