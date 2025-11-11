import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage

import cv2, imutils

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from module import holistucModule as hm
from module import aruco
from module import calcuate
from module import collectData
from module import motion 

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("R&D Workstudy")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frontview_label = QtWidgets.QLabel(self.centralwidget)
        self.frontview_label.setGeometry(QtCore.QRect(126, 10, 351, 20))
        self.frontview_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frontview_label.setTextFormat(QtCore.Qt.AutoText)
        self.frontview_label.setObjectName("frontview_label")
        self.topview_label = QtWidgets.QLabel(self.centralwidget)
        self.topview_label.setGeometry(QtCore.QRect(120, 330, 351, 20))
        self.topview_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.topview_label.setTextFormat(QtCore.Qt.AutoText)
        self.topview_label.setObjectName("topview_label")
        self.side_label = QtWidgets.QLabel(self.centralwidget)
        self.side_label.setGeometry(QtCore.QRect(480, 10, 351, 20))
        self.side_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.side_label.setTextFormat(QtCore.Qt.AutoText)
        self.side_label.setObjectName("side_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(1040, 220, 31, 251))
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(880, 290, 161, 171))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 159, 169))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.topvideo_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.topvideo_label.setGeometry(QtCore.QRect(0, 130, 141, 17))
        self.topvideo_label.setObjectName("topvideo_label")
        self.video_front_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.video_front_button.setGeometry(QtCore.QRect(0, 0, 141, 25))
        self.video_front_button.setObjectName("video_front_button")
        self.video_top_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.video_top_button.setGeometry(QtCore.QRect(0, 100, 141, 25))
        self.video_top_button.setObjectName("video_top_button")
        self.video_side_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.video_side_button.setGeometry(QtCore.QRect(0, 50, 141, 25))
        self.video_side_button.setObjectName("video_side_button")
        self.sidevideo_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sidevideo_label.setGeometry(QtCore.QRect(0, 80, 141, 17))
        self.sidevideo_label.setObjectName("sidevideo_label")
        self.frontvideo_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.frontvideo_label.setGeometry(QtCore.QRect(0, 30, 141, 17))
        self.frontvideo_label.setObjectName("frontvideo_label")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(860, 30, 151, 161))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.start_button = QtWidgets.QPushButton(self.splitter)
        self.start_button.setObjectName("start_button")
        self.stop_button = QtWidgets.QPushButton(self.splitter)
        self.stop_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stop_button.setAutoFillBackground(False)
        self.stop_button.setObjectName("stop_button")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(860, 200, 181, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.source_label = QtWidgets.QLabel(self.layoutWidget)
        self.source_label.setObjectName("source_label")
        self.verticalLayout.addWidget(self.source_label)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.wedcam_radiobutton = QtWidgets.QRadioButton(self.layoutWidget)
        self.wedcam_radiobutton.setObjectName("wedcam_radiobutton")
        self.verticalLayout.addWidget(self.wedcam_radiobutton)
        self.video_radiobutton = QtWidgets.QRadioButton(self.layoutWidget)
        self.video_radiobutton.setObjectName("video_radiobutton")
        self.verticalLayout.addWidget(self.video_radiobutton)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(1070, 200, 121, 106))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # self.view_label = QtWidgets.QLabel(self.layoutWidget1)
        # self.view_label.setObjectName("view_label")
        # self.verticalLayout_2.addWidget(self.view_label)
        # self.front_radiobutton = QtWidgets.QRadioButton(self.layoutWidget1)
        # self.front_radiobutton.setObjectName("front_radiobutton")
        # self.verticalLayout_2.addWidget(self.front_radiobutton)
        # self.side_radiobutton = QtWidgets.QRadioButton(self.layoutWidget1)
        # self.side_radiobutton.setObjectName("side_radiobutton")
        # self.verticalLayout_2.addWidget(self.side_radiobutton)
        # self.top_radiobutton = QtWidgets.QRadioButton(self.layoutWidget1)
        # self.top_radiobutton.setObjectName("top_radiobutton")
        # self.verticalLayout_2.addWidget(self.top_radiobutton)

        self.cam_frontlabel = QtWidgets.QLabel(self.centralwidget)
        self.cam_frontlabel.setGeometry(QtCore.QRect(120, 30, 352, 288))
        # self.cam_frontlabel.setPixmap(QtGui.QPixmap())
        # self.cam_frontlabel.setTabletTracking(False)
        self.cam_frontlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.cam_frontlabel.setObjectName("cam_frontlabel")
        # self.cam_frontlabel.setPixmap(QtGui.QPixmap(self.img1))

        self.cam_sidelabel = QtWidgets.QLabel(self.centralwidget)
        self.cam_sidelabel.setGeometry(QtCore.QRect(480, 30, 352, 288))
        # self.cam_sidelabel.setTabletTracking(False)
        self.cam_sidelabel.setFrameShape(QtWidgets.QFrame.Box)
        self.cam_sidelabel.setObjectName("cam_sidelabel")
        # self.cam_frontlabel.setPixmap(QtGui.QPixmap(self.img2))

        self.cam_toplabel = QtWidgets.QLabel(self.centralwidget)
        self.cam_toplabel.setGeometry(QtCore.QRect(120, 350, 352, 288))
        # self.cam_toplabel.setTabletTracking(False)
        self.cam_toplabel.setFrameShape(QtWidgets.QFrame.Box)
        self.cam_toplabel.setObjectName("cam_toplabel")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1070, 20, 67, 17))
        self.label.setObjectName("label")
        self.pushButton_name = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_name.setGeometry(QtCore.QRect(1150, 180, 61, 31))
        self.pushButton_name.setObjectName("pushButton_name")
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(480, 470, 67, 17))
        self.label_output.setObjectName("label_output")
        self.label_textoutput = QtWidgets.QLabel(self.centralwidget)
        self.label_textoutput.setGeometry(QtCore.QRect(480, 490, 511, 141))
        self.label_textoutput.setFrameShape(QtWidgets.QFrame.Box)
        self.label_textoutput.setMidLineWidth(0)
        self.label_textoutput.setObjectName("label_textoutput")
        self.label_Left_step = QtWidgets.QLabel(self.centralwidget)
        self.label_Left_step.setGeometry(QtCore.QRect(1070, 70, 111, 17))
        self.label_Left_step.setObjectName("label_Left_step")
        self.label_Right_step = QtWidgets.QLabel(self.centralwidget)
        self.label_Right_step.setGeometry(QtCore.QRect(1070, 120, 111, 17))
        self.label_Right_step.setObjectName("label_Right_step")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(1070, 40, 221, 25))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_left_step = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_left_step.setGeometry(QtCore.QRect(1070, 90, 221, 25))
        self.lineEdit_left_step.setObjectName("lineEdit_left_step")
        self.lineEdit_right_step = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_right_step.setGeometry(QtCore.QRect(1070, 140, 221, 25))
        self.lineEdit_right_step.setObjectName("lineEdit_right_step")

        self.label_seatofheight = QtWidgets.QLabel(self.centralwidget)
        self.label_seatofheight.setGeometry(QtCore.QRect(480, 340, 101, 17))
        self.label_seatofheight.setObjectName("label_seatofheight")
        self.label_biacromial = QtWidgets.QLabel(self.centralwidget)
        self.label_biacromial.setGeometry(QtCore.QRect(600, 340, 161, 17))
        self.label_biacromial.setObjectName("label_biacromial")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(480, 360, 95, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcdNumber_seatofheight = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber_seatofheight.setObjectName("lcdNumber_seatofheight")
        self.horizontalLayout.addWidget(self.lcdNumber_seatofheight)
        self.label_cm_seafiofheight = QtWidgets.QLabel(self.widget)
        self.label_cm_seafiofheight.setObjectName("label_cm_seafiofheight")
        self.horizontalLayout.addWidget(self.label_cm_seafiofheight)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(600, 360, 92, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lcdNumber_biacromialbreadth = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber_biacromialbreadth.setObjectName("lcdNumber_biacromialbreadth")
        self.horizontalLayout_2.addWidget(self.lcdNumber_biacromialbreadth)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1209, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Tool = QtWidgets.QMenu(self.menubar)
        self.menu_Tool.setObjectName("menu_Tool")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Graph_process_Round_Time_s = QtWidgets.QAction(MainWindow)
        self.action_Graph_process_Round_Time_s.setObjectName("action_Graph_process_Round_Time_s")
        # self.action_Graph_process_Round_Time_s.triggered.connect(self.plot_process_time)

        self.Graph_poor = QtWidgets.QAction(MainWindow)
        self.Graph_poor.setObjectName("Graph_poor")
        # self.Graph_poor.triggered.connect(self.plot_poor)

        self.calculate_st = QtWidgets.QAction(MainWindow)
        self.calculate_st.setObjectName("calculate_st")
        # self.calculate_st.triggered.connect(self.calculate_standas)

        self.process_chart = QtWidgets.QAction(MainWindow)
        self.process_chart.setObjectName("process_chart")
        # self.process_chart.triggered.connect(self.process_ch)

        self.menu_Tool.addAction(self.action_Graph_process_Round_Time_s)
        self.menu_Tool.addAction(self.Graph_poor)
        self.menu_Tool.addAction(self.calculate_st)
        self.menu_Tool.addAction(self.process_chart)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Tool.menuAction())

        self.retranslateUi(MainWindow)
        # if self.wedcam_radiobutton.isChecked() == True or self.video_radiobutton.isChecked() == True:
        self.start_button.clicked.connect(self.start_video)
        self.stop_button.clicked.connect(self.stop_video)

        # self.pushButton_name.clicked.connect(self.get_name_lastname)
        # self.stop_button.clicked.connect(self.stop_video_ros_)  # type: ignore

        # self.action_Graph_process_Round_Time_s.triggered.connect(self.plot_process_time)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Workstudy DPU"))
        self.frontview_label.setText(_translate("MainWindow", "Top"))
        self.topview_label.setText(_translate("MainWindow", "Front"))
        self.side_label.setText(_translate("MainWindow", "Side"))
        self.topvideo_label.setText(_translate("MainWindow", "Top video"))
        self.video_front_button.setText(_translate("MainWindow", "select front video"))
        self.video_top_button.setText(_translate("MainWindow", "select top video"))
        self.video_side_button.setText(_translate("MainWindow", "select side video"))
        self.sidevideo_label.setText(_translate("MainWindow", "Side video"))
        self.frontvideo_label.setText(_translate("MainWindow", "Front video"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.source_label.setText(_translate("MainWindow", "Source"))
        self.wedcam_radiobutton.setText(_translate("MainWindow", "Wedcam"))
        self.video_radiobutton.setText(_translate("MainWindow", "Video"))
        # self.view_label.setText(_translate("MainWindow", "View"))
        # self.front_radiobutton.setText(_translate("MainWindow", "Front"))
        # self.side_radiobutton.setText(_translate("MainWindow", "Side"))
        # self.top_radiobutton.setText(_translate("MainWindow", "Top"))
        self.cam_frontlabel.setText(_translate("MainWindow", "cam1"))
        self.cam_sidelabel.setText(_translate("MainWindow", "cam2"))
        self.cam_toplabel.setText(_translate("MainWindow", "cam3"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.pushButton_name.setText(_translate("MainWindow", "Ok"))
        self.label_output.setText(_translate("MainWindow", "output"))
        self.label_textoutput.setText(_translate("MainWindow", "message"))
        self.label_Left_step.setText(_translate("MainWindow", "Left step"))
        self.label_Right_step.setText(_translate("MainWindow", "Right step"))
        self.lineEdit_left_step.setText(_translate("MainWindow", "[6,7,8]"))
        self.lineEdit_right_step.setText(_translate("MainWindow", "[5,4,3]"))

        self.label_seatofheight.setText(_translate("MainWindow", "distance between buttocks and toes"))
        self.label_biacromial.setText(_translate("MainWindow", "biacromial breadth"))
        self.label_cm_seafiofheight.setText(_translate("MainWindow", "cm"))
        self.label_2.setText(_translate("MainWindow", "cm"))
        # self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Tool.setTitle(_translate("MainWindow", "&Tool"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_Graph_process_Round_Time_s.setText(_translate("MainWindow", "&Graph process : Item/Time(s)"))
        self.Graph_poor.setText(_translate("MainWindow", "&Graph poor : Time(s)/Event Index"))
        self.calculate_st.setText(_translate("MainWindow", "&Standard Time"))
        self.process_chart.setText(_translate("MainWindow", "&Process chart"))

    def start_video(self):
        if self.wedcam_radiobutton.isChecked():
            self.video0 = cv2.VideoCapture("/dev/v4l/by-id/usb-046d_Logitech_Webcam_C930e_BF5EB0FE-video-index0")
            self.video1 = cv2.VideoCapture("/dev/v4l/by-id/usb-046d_081b_78315560-video-index0")
            self.video2 = cv2.VideoCapture("/dev/v4l/by-id/usb-046d_081b_03345560-video-index0")

            while(self.video0.isOpened() and self.video1.isOpened() and self.video2.isOpened()):
                QtWidgets.QApplication.processEvents()
                img0, self.image0 = self.video0.read()
                img1, self.image1 = self.video1.read()
                img2, self.image2 = self.video2.read()

                self.update()
                # if MainWindow().closeEvent():
                #     break

    def stop_video(self):
        self.video0.release()
        self.video1.release()
        self.video2.release()
        # return True
    
    def setPhoto(self,image, camLabel):
        try:
            self.tmp = image
            image = imutils.resize(image,width=640)
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
            camLabel.setPixmap(QtGui.QPixmap.fromImage(image))

        except:
            print("Stop Camera!")

    def update(self):
        self.setPhoto(self.image0, self.cam_frontlabel)
        self.setPhoto(self.image1, self.cam_sidelabel)
        self.setPhoto(self.image2, self.cam_toplabel)
        # self.img0 = self.image0
        # self.img1 = self.image1
        # self.img2 = self.image2
        # self.img0 = self.setPhoto(self.img0)
        # self.img1 = self.setPhoto(self.img1)
        # self.img2 = self.setPhoto(self.img2)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        # คำสั่งที่จะทำเมื่อผู้ใช้ปิดหน้าต่าง
        reply = QtWidgets.QMessageBox.question(self, 'Close Confirmation',
                                               "Are you sure you want to close the window?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()  # ยอมรับการปิดหน้าต่าง
            self.ui.stop_video()
            # return True
        else:
            event.ignore()  # ยกเลิกการปิดหน้าต่าง
            # return False

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
