from random import randint
from random import choice
import webbrowser
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox

def get_random_film():
    film = choice(lst_films)
    if film == 'surprise':
        message = QMessageBox()
        message.setWindowTitle('окно')
        message.setText('ПАСХАЛОЧКА!!!!!')
        message.exec()
    else:
        webbrowser.open(film)




lst_films = [
    'https://www.kinopoisk.ru/film/3498/',
    'https://www.kinopoisk.ru/film/444/',
    'https://www.kinopoisk.ru/film/41519/',
    'https://www.kinopoisk.ru/film/195334/?utm_referrer=yandex.ru',
    'https://www.kinopoisk.ru/film/301/',
    'https://www.kinopoisk.ru/film/160977/',
    'surprise'
]

def get_film_TheLordoftheRings():
    webbrowser.open('https://www.kinopoisk.ru/film/3498/')

def get_film_Terminator2():
    webbrowser.open('https://www.kinopoisk.ru/film/444/')

def get_film_Brother():
    webbrowser.open('https://www.kinopoisk.ru/film/41519/')

def get_film_Prestige():
    webbrowser.open('https://www.kinopoisk.ru/film/195334/?utm_referrer=yandex.ru')

def get_film_TheMatrix():
    webbrowser.open('https://www.kinopoisk.ru/film/301/')

def get_film_Apocalypsis():
    webbrowser.open('https://www.kinopoisk.ru/film/160977/')

app = QApplication([])

window = QWidget()
window.resize(600, 500)
window.setWindowTitle('Кинопоиск')

main_line = QHBoxLayout()
line1 = QVBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()
line4 = QVBoxLayout()



text = QLabel('Выберите фильм:')
button1 = QPushButton('Властелин колец')
button2 = QPushButton('Терминатор 2')
button3 = QPushButton('Апокалипсис')
button4 = QPushButton('Брат')
button5 = QPushButton('Престиж')
button6 = QPushButton('Матрица')
button7 = QPushButton('Случайный фильм')



button1.clicked.connect(get_film_TheLordoftheRings)
button2.clicked.connect(get_film_Terminator2)
button3.clicked.connect(get_film_Apocalypsis)
button4.clicked.connect(get_film_Brother)
button5.clicked.connect(get_film_Prestige)
button6.clicked.connect(get_film_TheMatrix)
button7.clicked.connect(get_random_film)




line1.addWidget(button1, alignment=Qt.AlignCenter)
line1.addWidget(button2, alignment=Qt.AlignCenter)
line2.addWidget(button3, alignment=Qt.AlignCenter)
line2.addWidget(button4, alignment=Qt.AlignCenter)
line3.addWidget(button5, alignment=Qt.AlignCenter)
line3.addWidget(button6, alignment=Qt.AlignCenter)
line4.addWidget(button7, alignment=Qt.AlignCenter)




main_line.addWidget(text, alignment=Qt.AlignCenter)
main_line.addLayout(line1)
main_line.addLayout(line2)
main_line.addLayout(line3)
main_line.addLayout(line4)



window.setLayout(main_line)

window.setStyleSheet('font-size: 20px')

window.show()
app.exec()
