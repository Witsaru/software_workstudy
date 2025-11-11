import csv
import time

class data_pandas():

    def __init__(self, name):
        self.ts = time.asctime(time.gmtime(0))
        self.name = name
        self.directory = name

    def write_to_csv(writer, keypoints):
        # time_stamp = time.time()
        row = keypoints
        writer.writerow(row)

    def data_to_pasdan_side(self,list):

        list_ = list
        with open(f'data_collection/{self.name}/data/pose_data_side{time.strftime("%Y%m%d_%H%M%S", time.gmtime())}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            
            header = ['time_stamp']
            for i in range(33):
                header.extend([f'keypoint_{i}_x', f'keypoint_{i}_y', f'keypoint_{i}_z', f'keypoint_{i}_confidence'])
            header.extend(['angle_shoulder_right', 'angle_elbow_right','angle_neck', 'angle_body','label'])
            writer.writerow(header)

            for ti, key, a, l in list_:
                writer.writerow([ti]+key+a+[l])


    def data_to_pasdan_top(self,list):
        list_ = list
        with open(f'data_collection/{self.name}/data/pose_data_top{time.strftime("%Y%m%d_%H%M%S", time.gmtime())}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            
            header = ['time_stamp']
            for i in range(33):
                header.extend([f'keypoint_{i}_x', f'keypoint_{i}_y', f'keypoint_{i}_z', f'keypoint_{i}_confidence'])
            header.extend(['angle_elbow_left', 'angle_elbow_right','angle_shoulder_left', 'angle_shoulder_right', 'label'])
            writer.writerow(header)

            for ti, key, a, l in list_:
                # print(ti,key,sep='\t')
                writer.writerow([ti]+key+a+[l])

    def data_timeProcess(self, list, num_process):
        list_ = list
        with open(f'data_collection/{self.name}/time/timeprocess{time.strftime("%Y%m%d_%H%M%S", time.gmtime())}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            header = ['Piece number']
            for i in range(num_process):
                header.extend([f'Subtime{i}'])

            header.extend(['totaltime'])

            for num, sub, total in list_:
                
                writer.writerow([num]+sub+total)