import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QValueAxis, QBarCategoryAxis
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

class BarChart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bar Chart with Negative and Positive Values Colored")
        self.setGeometry(100, 100, 800, 600)

        # Data
        categories = ['A', 'B', 'C', 'D', 'E']
        values = [5, -3, 8, -2, 4]

        # Create separate bar sets for positive and negative values
        positive_set = QBarSet("Positive Values")
        negative_set = QBarSet("Negative Values")

        # Fill bar sets based on the value
        for value in values:
            if value >= 0:
                positive_set.append(value)
                negative_set.append(0)  # Ensure alignment by adding 0 to the other set
            else:
                positive_set.append(0)  # Ensure alignment by adding 0 to the other set
                negative_set.append(value)

        # Set colors for the positive and negative sets
        positive_set.setColor(QColor(Qt.green))  # Green for positive values
        negative_set.setColor(QColor(Qt.red))    # Red for negative values

        # Create the bar series and add both sets
        series = QBarSeries()
        series.append(positive_set)
        series.append(negative_set)

        # Create the chart
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Bar Chart with Negative Values (Red) and Positive Values (Green)")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Customize X-axis
        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        # Customize Y-axis
        axis_y = QValueAxis()
        axis_y.setRange(-10, 10)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        # Create the chart view
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # Set the central widget
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(chart_view)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BarChart()
    window.show()
    sys.exit(app.exec_())
