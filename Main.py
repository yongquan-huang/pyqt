import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from CallMainWin import MainForm
from historyWin4 import history_data
from realtimeWin import realtime_data

class Controller():
    def __init__(self):
        pass

    def show_main(self):
        self.main = MainForm()
        self.main.pushButton_3.clicked.connect(self.show_history)
        self.main.pushButton_3.clicked.connect(self.main.close)
        self.main.pushButton_2.clicked.connect(self.show_realtime)
        self.main.pushButton_3.clicked.connect(self.main.close)
        self.main.show()

    def show_history(self):
        self.history = history_data()
        self.history.pushButton.clicked.connect(self.history.close)
        self.history.pushButton.clicked.connect(self.show_main)
        self.history.pushButton_2.clicked.connect(self.history.close)
        self.history.pushButton_2.clicked.connect(self.show_realtime)
        self.history.show()

    def show_realtime(self):
        self.realtime = realtime_data()
        self.realtime.pushButton.clicked.connect(self.realtime.close)
        self.realtime.pushButton.clicked.connect(self.show_main)
        self.realtime.pushButton_3.clicked.connect(self.realtime.close)
        self.realtime.pushButton_3.clicked.connect(self.show_history)
        self.realtime.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())