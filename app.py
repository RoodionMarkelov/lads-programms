import sys
import xandy, years, weeks, function, iterator
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication,
                             QDesktopWidget, QInputDialog, QLineEdit, QFileDialog, QLabel, QMessageBox)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self._iterator = None
        QToolTip.setFont(QFont('SansSerif', 14))

        self.setToolTip('This is a <b>QWidget</b> widget')
        self.label = QLabel(self)
        self.label.setText("Hello, User!")
        self.label.adjustSize()
        self.label.move(200, 50)

        self.date = QLabel(self)
        self.temp_morning = QLabel(self)
        self.pres_morning = QLabel(self)
        self.wind_morning = QLabel(self)
        self.temp_evening = QLabel(self)
        self.pres_evening = QLabel(self)
        self.wind_evening = QLabel(self)

        btn1 = QPushButton('X and Y', self)
        btn1.setToolTip('Click on the button to divide file on date and meteodata.')
        btn1.clicked.connect(self._divide_on_two)
        btn1.resize(btn1.sizeHint())
        btn1.move(50, 50)

        btn2 = QPushButton('Divide by years', self)
        btn2.setToolTip('Click on the button to divide csv_file by years.')
        btn2.clicked.connect(self._divide_on_years)
        btn2.resize(btn2.sizeHint())
        btn2.move(50, 100)

        btn3 = QPushButton('Divide by weeks', self)
        btn3.setToolTip('Click on the button to divide csv_file by weeks.')
        btn3.clicked.connect(self._divide_on_week)
        btn3.resize(btn3.sizeHint())
        btn3.move(50, 150)

        btn4 = QPushButton('Get data', self)
        btn4.setToolTip('Click on the button to get data for the transmitted date.')
        btn4.clicked.connect(self._find_date_from_file)
        btn4.resize(btn4.sizeHint())
        btn4.move(50, 200)

        btn5 = QPushButton('create_iterator', self)
        btn5.setToolTip('Click on the button to create iterator for csv_file')
        btn5.clicked.connect(self.create_iterator)
        btn5.resize(btn5.sizeHint())
        btn5.move(50, 250)

        btn6 = QPushButton('Next data.', self)
        btn6.setToolTip('Click on the button to get next data in current file')
        btn6.clicked.connect(self._window_next)
        btn6.resize(btn6.sizeHint())
        btn6.move(50, 300)

        qbtn = QPushButton('Quit', self)
        qbtn.setToolTip('Click on the button to exit.')
        qbtn.clicked.connect(self._quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(350, 400)

        self.resize(450, 450)
        self.center()
        self.setWindowTitle('app')
        self.setWindowIcon(QIcon('web.png'))

        self.show()

    def center(self):
        location = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        location.moveCenter(center)
        self.move(location.topLeft())

    def _divide_on_two(self):
        csv_file = self.get_file()
        xandy.divide_on_x_y(csv_file)

    def _divide_on_years(self):
        csv_file = self.get_file()
        years.divide_by_years(csv_file)

    def _divide_on_week(self):
        csv_file = self.get_file()
        weeks.divide_by_week(csv_file)

    def _find_date_from_file(self):
        date, ok_pressed = QInputDialog.getText(self, "Get text", "Input date (format year-mouth-day or ****-**-**):", QLineEdit.Normal, "")
        if ok_pressed and date != '':
            target_date = date
            file_name = self.get_file()
            if file_name:
                data = function.get_date_from_file(target_date, file_name)
                if data is not None:
                    self.label.setText("Data for transmitted date:")
                    self.label.adjustSize()
                    self.label.move(200, 50)
                    self.print_dict(data)
                else:
                    self.label.setText("Data for transmitted date is not exist.")
                    self.label.adjustSize()
                    self.label.move(200, 50)
                    self.date.setText("")
                    self.temp_morning.setText("")
                    self.pres_morning.setText("")
                    self.wind_morning.setText("")
                    self.temp_evening.setText("")
                    self.pres_evening.setText("")
                    self.wind_evening.setText("")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def create_iterator(self):
        csv_file = self.get_file()
        self._iterator = iterator.Iterator(csv_file)

    def _window_next(self):
        if self._iterator is not None:
            next_data = self._iterator.__next__()
            self.label.setText("Next data in csv_file:")
            self.label.adjustSize()
            self.label.move(200, 50)
            self.print_dict(next_data)
        else:
            reply = QMessageBox.question(self, 'Message', "You have to create an iterator for the file. Are you want to create iterator?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.create_iterator()
            else:
                return
    def get_file(self):
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        file_name = QFileDialog.getOpenFileName(self, 'Choose file', folderpath, 'CSV File (*.csv)')
        return file_name[0]

    def print_dict(self, dictionary):
        dictionary_items = []
        for i, j in dictionary.items():
            dictionary_items.append(str(i) + ": " + str(j))
        self.date.setText(dictionary_items[0])
        self.date.adjustSize()
        self.date.move(200, 80)
        self.temp_morning.setText(dictionary_items[1])
        self.temp_morning.adjustSize()
        self.temp_morning.move(200, 110)
        self.pres_morning.setText(dictionary_items[2])
        self.pres_morning.adjustSize()
        self.pres_morning.move(200, 140)
        self.wind_morning.setText(dictionary_items[3])
        self.wind_morning.adjustSize()
        self.wind_morning.move(200, 170)
        self.temp_evening.setText(dictionary_items[4])
        self.temp_evening.adjustSize()
        self.temp_evening.move(200, 200)
        self.pres_evening.setText(dictionary_items[5])
        self.pres_evening.adjustSize()
        self.pres_evening.move(200, 230)
        self.wind_evening.setText(dictionary_items[6])
        self.wind_evening.adjustSize()
        self.wind_evening.move(200, 260)

    def _quit(self):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            QApplication.instance().quit()
        else:
            return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

