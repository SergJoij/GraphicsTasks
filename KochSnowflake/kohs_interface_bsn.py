from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSpinBox, QLabel
from PyQt5.QtCore import QCoreApplication
import turtle
import sys


class Window(QMainWindow):
    def __init__(self, size, iterations):
        super().__init__()
        self.s = size
        self.n = iterations
        self.title = "Kohs"
        self.top = 150
        self.left = 150
        self.height = 200
        self.width = 216
        self.turtle = turtle.Turtle()
        self.turtle.getscreen().setworldcoordinates(-10.0, -400.0, 490.0, 100.0)  # пользовательские координаты!

        self.paint_b = QPushButton('Нарисовать', self)
        self.paint_b.clicked.connect(self.draw_object)
        self.paint_b.resize(self.paint_b.sizeHint())
        self.paint_b.move(20, 20)

        quit_b = QPushButton('Выход', self)
        quit_b.clicked.connect(QCoreApplication.instance().quit)
        quit_b.resize(quit_b.sizeHint())
        quit_b.move(120, 20)

        self.box_iter = QSpinBox(self)
        self.box_iter.setRange(0, 6)
        self.box_iter.move(20, 70)
        self.box_iter.valueChanged.connect(self.iterations_changed)
        self.box_iter.show()

        self.loading_label = QLabel(self)
        self.loading_label.move(20, 120)
        self.loading_label.setFixedWidth(120)
        self.loading_label.show()

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def draw_object(self):
        self.turtle.reset()
        self.deactivated_all()
        self.loading_label.setText("Ждём...")
        self.draw_upper_triangle()
        self.turtle.hideturtle()
        self.loading_label.setText("Снежинка нарисована")
        self.activated_all()

    def draw_upper_triangle(self):
        self.turtle.speed(100)
        for i in range(3):
            self.details(self.s, self.n)
            self.turtle.right(120)

    def details(self, step, iterations):
        if iterations == 0:
            self.turtle.forward(step)
        else:
            self.details(step / 3, iterations - 1)
            self.turtle.left(60)
            self.details(step / 3, iterations - 1)
            self.turtle.right(120)
            self.details(step / 3, iterations - 1)
            self.turtle.left(60)
            self.details(step / 3, iterations - 1)

    def iterations_changed(self):
        self.n = self.box_iter.value()

    def activated_all(self):
        self.paint_b.setEnabled(True)
        self.box_iter.setEnabled(True)

    def deactivated_all(self):
        self.paint_b.setEnabled(False)
        self.box_iter.setEnabled(False)


size_n = 300
n = 0
app1 = QApplication(sys.argv)
window = Window(size_n, n)
window.show()
sys.exit(app1.exec())
