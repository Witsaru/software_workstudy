import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

# ข้อมูลกิจกรรมและสัญลักษณ์
left_hand_symbols = ["○", "□", "→", "D", "△", "○", "□", "→", "D", "△", "○", "→"]
right_hand_symbols = ["○", "□", "D", "△", "→", "○", "□", "D", "△", "→", "○", "△"]
left_hand_times = [6, 0, 1, 5, 3, 0, 5, 3, 0, 5, 3, 0]
right_hand_times = [5, 0, 1, 3, 0, 5, 3, 0, 5, 3, 5, 2]
total_activities = len(left_hand_symbols)

class TwoHandedProcessChart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.figure, self.ax = plt.subplots(figsize=(6, 8))
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        
        self.plot_chart()
    
    def plot_chart(self):
        self.ax.clear()
        self.ax.set_title("Two-Handed Process Chart")
        
        # สร้างตารางด้วยเส้นกริด
        self.ax.set_xlim(-1, 3)
        self.ax.set_ylim(-1, total_activities)
        self.ax.axis("off")

        # วาดเส้นกริดและใส่สัญลักษณ์ในแต่ละช่อง
        for i in range(total_activities):
            # เส้นแนวตั้งของมือซ้ายและมือขวา
            self.ax.plot([0, 0], [i, i + 1], 'k-', linewidth=1)
            self.ax.plot([2, 2], [i, i + 1], 'k-', linewidth=1)

            # ใส่สัญลักษณ์ของมือซ้ายและมือขวา
            self.ax.text(0, i, left_hand_symbols[i], ha='center', va='center', fontsize=12, color="blue")
            self.ax.text(2, i, right_hand_symbols[i], ha='center', va='center', fontsize=12, color="green")
            
            # วาดเส้นเชื่อมระหว่างมือซ้ายและมือขวา
            if i < total_activities - 1:
                self.ax.plot([0, 2], [i, i + 1], 'k-', linewidth=1)

        # แสดงเวลาของแต่ละกิจกรรมที่ด้านล่าง
        for i, (left_time, right_time) in enumerate(zip(left_hand_times, right_hand_times)):
            self.ax.text(0, i - 0.5, str(left_time), ha='center', va='center', fontsize=10, color="black")
            self.ax.text(2, i - 0.5, str(right_time), ha='center', va='center', fontsize=10, color="black")
        
        self.canvas.draw()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Two-Handed Process Chart")
        self.chart = TwoHandedProcessChart(self)
        self.setCentralWidget(self.chart)

# รันโปรแกรม
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
