from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg


class PlotWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(PlotWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground((28, 38, 112))
        self.setCentralWidget(self.graphWidget)

        self.time_data = []  # 100 time points
        self.ear_data = []  # 100 data points

        self.graphWidget.setLabel('left', 'EAR Values')
        self.graphWidget.setLabel('bottom', 'Time (s)')
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setYRange(0, 0.5, padding=0)

        pen = pg.mkPen(color=(46, 195, 195), width=3)
        self.data_line =  self.graphWidget.plot(self.time_data, self.ear_data, pen=pen)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()


    def stop_switch(self):
        print("clearing plot")
        self.timer.stop()
        self.data_line.clear()


    def change_data(self, new_time_data, new_ear_data):

        self.time_data = new_time_data
        self.ear_data = new_ear_data


    def update_plot_data(self):

        time_data = self.time_data[-60:]  
        ear_data = self.ear_data[-60:]

        self.data_line.setData(time_data, ear_data)  # Update the data.
