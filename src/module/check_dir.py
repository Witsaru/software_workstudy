import os

class checkDir():

    def __init__(self, path):
        self.path = path

        if self.path_ecists(self.path):
            print(f" select file {self.path}")

        else:
            print(f"create file {self.path}")
            os.makedirs(f"{self.path}")


    def path_ecists(self,path):
        isExist= os.path.exists(path)
        return isExist
    
if __name__ == '__main__' :
    Path = checkDir('data_collection')
