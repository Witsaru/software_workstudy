from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QVBoxLayout
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QValueAxis, QBarCategoryAxis
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import pyqtgraph as pg
import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from module import dumpdata
from module import calcuate as cal
from ui import plotGraphProcessTime as pgpt
from ui import chat_A_B as cAB
from ui import ST_win as stw
from ui import key_process_gpt as kpgpt

class active_sub_win():

    def plot_graph_proecss_time(self):
        plot_g_pt_win = QtWidgets.QDialog()
        plot_g_pt = pgpt.Ui_pgpt()
        plot_g_pt.setupUi(plot_g_pt_win)
        plot_g_pt.pushButton_Browse.clicked.connect(lambda: active_sub_button().browsefile(plot_g_pt.line_nameFile))
        print(plot_g_pt.line_nameFile.text())
        plot_g_pt.pushButton_2.clicked.connect(lambda: active_graph().line_graph(plot_g_pt.line_nameFile.text(), plot_g_pt.widget, "item", "time", trendline=True))
        plot_g_pt_win.exec_()

    def chart_compare(self):
        chart_c_win = QtWidgets.QDialog()
        chart_c = cAB.Ui_chart()
        chart_c.setupUi(chart_c_win)
        chart_c.pushButton_A.clicked.connect(lambda: active_sub_button().browsefile(chart_c.lineEdit_A))
        chart_c.pushButton_B.clicked.connect(lambda: active_sub_button().browsefile(chart_c.lineEdit_B))
        chart_c.pushButton_Done.clicked.connect(lambda: active_graph().chart_pn(chart_c.lineEdit_A.text(), chart_c.lineEdit_B.text(), chart_c.widget_chart))
        chart_c_win.exec_()

    def st_win(self):
        st_win = QtWidgets.QDialog()
        st = stw.Ui_ST()
        st.setupUi(st_win)
        st.pushButton_browse.clicked.connect(lambda: active_sub_button().browsefile(st.lineEdit_file))
        st.pushButton.clicked.connect(lambda: active_sub_button().lcdDisplayST(
            st.lineEdit_file.text(),
            st.lineEdit_2.value(),
            st.lineEdit_3.value(),
            lcd_list= [st.lcdNumber, st.lcdNumber_2, st.lcdNumber_3]
        ))
                

        st_win.exec_()

    def keyPgpt(self):
        keyprocess = QtWidgets.QDialog()
        keyset = kpgpt.keysaveP()
        # keyset.setupUi(keyprocess)
        keyset.show()
        # keyprocess.exec_()

class active_sub_button():

    def __init__(self):
        self.dumpF = dumpdata.dump_data()

    def browsefile(self, boxtext):
        fname, _ = QFileDialog.getOpenFileName(None, 'Open file','CSV files (.csv)')
        if fname:
            boxtext.setText(fname)

    def lcdDisplayST(self, boxtext, ra, ao, lcd_list = []):
        if boxtext:
            timeall = self.dumpF.pull_data(boxtext, "totaltime")
            if ra > 0.0 and ao > 0.0:
                stime = cal.calcu_stantime(timeall, ra, ao)
                lcd_list[0].display(stime[0])
                lcd_list[1].display(stime[1])
                lcd_list[2].display(stime[2])


class active_graph():

    def __init__(self):
        self.dumpF = dumpdata.dump_data()

    def line_graph(self, boxtext, area, axisX, axisY, trendline=False):
        # print(boxtext)
        if boxtext:
            x = self.dumpF.pull_data(boxtext, axisX)
            y = self.dumpF.pull_data(boxtext, axisY)

            area_plot = QtWidgets.QVBoxLayout(area)
            plot_line_graph = pg.PlotWidget()
            area_plot.addWidget(plot_line_graph)
            # plot_line_graph.plot(pen=pg.mkPen(color=(0, 255, 0), width=2))
            curve = plot_line_graph.plot(pen=pg.mkPen(color=(0, 255, 0), width=2))
            curve.setData(x,y)

            if trendline:
                coefficients = np.polyfit(x, y, 3)
                trendline_ = np.polyval(coefficients, x)

                trendline_curve =plot_line_graph.plot(pen=pg.mkPen(color=(255, 255, 51), width=2))
                trendline_curve.setData(x, trendline_)

    def chart_pn(self, boxtextA, boxtextB, area):

        if boxtextA and boxtextB:

            a_data = self.dumpF.pull_allTocip(boxtextA)
            b_data = self.dumpF.pull_allTocip(boxtextB)
            a_avr = []
            b_avr = []
            # print(a_data[1])

            for i in a_data[1][1::]:
                avr = np.average(i)
                a_avr.append(avr)

            for j in b_data[1][1::]:
                avr = np.average(j)
                b_avr.append(avr)

            np_a = np.array(a_avr)
            np_b = np.array(b_avr)
            np_cp = np_a - np_b

            num_itme = a_data[0][1:len(a_data[0])-1]
            list_time = np_cp[0:len(np_cp)-1]
            print(list_time)

            positive_set = QBarSet("Positive Values")
            negative_set = QBarSet("Negative Values")
            for value in list_time:
                if value >= 0:
                    positive_set.append(value)
                    negative_set.append(0)  # Ensure alignment by adding 0 to the other set
                else:
                    positive_set.append(0)  # Ensure alignment by adding 0 to the other set
                    negative_set.append(value)

            # Set colors for the positive and negative sets
            positive_set.setColor(QColor(Qt.green))  # Green for positive values
            negative_set.setColor(QColor(Qt.red))    # Red for negative values

            series = QBarSeries()
            series.append(positive_set)
            series.append(negative_set)

            chart = QChart()
            chart.addSeries(series)
            chart.setTitle("Bar Chart with Negative Values (Red) and Positive Values (Green)")
            chart.setAnimationOptions(QChart.SeriesAnimations)

            # Customize X-axis
            axis_x = QBarCategoryAxis()
            axis_x.append(num_itme)
            chart.addAxis(axis_x, Qt.AlignBottom)
            series.attachAxis(axis_x)

            # Customize Y-axis
            axis_y = QValueAxis()
            axis_y.setRange(np_cp[0:len(np_cp)-1].min(), np_cp[0:len(np_cp)-1].max())
            chart.addAxis(axis_y, Qt.AlignLeft)
            series.attachAxis(axis_y)

            # Create the chart view
            chart_view = QChartView(chart)
            chart_view.setRenderHint(QPainter.Antialiasing)

            # Set the central widget
            layout = QVBoxLayout(area)
            layout.addWidget(chart_view)
            # self.setCentralWidget(area)

