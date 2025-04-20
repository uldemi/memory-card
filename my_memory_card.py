#создай приложение для запоминания информации

from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMessageBox,
                             QPushButton, QRadioButton, QVBoxLayout, QWidget, QGroupBox, QButtonGroup)
from random import shuffle
class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
kittens = Question('Какой породы кошек не существует?', 'усатая', 'русская голубая', 'сфинкс', 'вислоухая')
roses = Question('Розы какого цвета нельзя вырастить, не крася их?', 'лиловые','жёлтые', 'апельсиновые' ,'белые')
leaves = Question('В какое время года опадают листья?', 'осень', 'весна', 'лето', 'зима')
fur = Question('Какое животное не меняет цвет меха на зиму?', 'бурундук', 'горностай', 'ласка', 'песец')
pattern = Question('Какой узор на шерсти у кошек называется леопардовым?','пятна на спине и боках','полоски','сочетание двух цветов в окрасе','большие пятна по всему телу')
turtle = Question('Сколько лет в среднем живёт красноухая черепаха?','30 лет','50 лет','95 лет','8 лет')
amphibian = Question('Какое животное не относится к земноводным?','ящерица','лягушка','саламандра','тритон')
  
  
question_list.append(kittens)
question_list.append(roses)
question_list.append(leaves)
question_list.append(fur)
question_list.append(pattern)
question_list.append(turtle)
question_list.append(amphibian)

app = QApplication([]) #создание приложения
main_win = QWidget() #окно
main_win.setWindowTitle('Memory Card') #название окна
main_win.move(90, 70) #сдвиг окна
main_win.resize(400, 200) #размер экрана


RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()




layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget (rbtn_2)
layout_ans3.addWidget (rbtn_3)
layout_ans3.addWidget (rbtn_4)
layout_ans1.addLayout (layout_ans2)
layout_ans1.addLayout (layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('dlcvdxld')
lb_Correct = QLabel('kdvkdk')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.setLayout(layout_ans1)

AnsGroupBox.hide()

# AnsGroupBox = QGroupBox('Результат теста')

# yesno = QLabel('Правильно/Неправильно')
# yes = QLabel('Правильный ответ')
# answersbox = QVBoxLayout()
# answersbox.addWidget(yesno)
# answersbox.addWidget(yes)
# AnsGroupBox.setLayout(answersbox)
# hardquest = QLabel('Самый сложый вопрос в мире!')
# line_1 = QHBoxLayout()
# line_1.addWidget(hardquest)
# line_2 = QHBoxLayout()
# line_2.addWidget(answersbox)
# line_3 = QHBoxLayout
# sldsh = QPushButton('Следующий вопрос')
# line_3.addWidget(sldsh)

# answersbox.addLayout(line_1)
# answersbox.addLayout(line_2)
# answersbox.addLayout(line_3)

box = QVBoxLayout() #коробочка для виджетов
line1 = QHBoxLayout()
lb_question = QLabel('Какой национальности не существует?')

line1.addWidget(lb_question, alignment = Qt.AlignCenter) #текст в line
line2 = QHBoxLayout() 
line2.addWidget(AnsGroupBox)
line2.addWidget(RadioGroupBox)

line3 = QHBoxLayout()
answer = QPushButton('Ответить')
line3.addWidget(answer)

AnsGroupBox.hide()
# line2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
# line2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
# line3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
# line3.addWidget(btn_answer4, alignment = Qt.AlignCenter)


box.addLayout(line1)
box.addLayout(line2)
box.addLayout(line3)

# def win():
#     victory_win = QMessageBox()
#     victory_win.setText('Верно!\nВы выиграли гироскутер')
#     victory_win.exec_()

# def lose():
#     victory_win = QMessageBox()
#     victory_win.setText('Нет, в 2015 году \nВы выиграли фирменный плакат')
#     victory_win.exec_()

# btn_answer1.clicked.connect(lose)
# btn_answer2.clicked.connect(lose)
# btn_answer3.clicked.connect(win)
# btn_answer4.clicked.connect(lose)

main_win.setLayout(box)
# main_win.setLayout(answersbox)
def show_result(): #панель ответов
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer.setText('Следующий вопрос')

def show_question(): #панель с вопросом и вариантами ответов
    AnsGroupBox.hide()
    RadioGroupBox.show()
    answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) #сбросить выбор кнопки


answerlist = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answerlist[0].isChecked():
        show_correct('Правильно!')
        main_win.score =+ 1
        print('Статистика: \n Всего вопросов:', main_win.total, '\n Правильных ответов:', main_win.score)
        print('Рейтинг:', (main_win.score/main_win.total)*100,'%')
    else:
        if answerlist[1].isChecked() or answerlist[2].isChecked() or answerlist[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:', (main_win.score/main_win.total*100), '%')
    

def next_quesion():
    
    main_win.cur_question += 1 #переход к следующему вопросу
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0 #обнуляем счетчик
    kittens = question_list[main_win.cur_question] #взяли вопрос
    ask(kittens) #спросили вопрос
    main_win.total += 1

def click_ok():
    if answer.text()=='Ответить':
        check_answer()
    else:
        next_quesion()
    
main_win.cur_question = -1 #создание номера вопроса


def ask(kittens: Question):
    shuffle(answerlist)
    answerlist[0].setText(kittens.right_answer)
    answerlist[1].setText(kittens.wrong1)
    answerlist[2].setText(kittens.wrong2)
    answerlist[3].setText(kittens.wrong3)
    lb_question.setText(kittens.question) #вопрос
    lb_Correct.setText(kittens.right_answer)
    show_question() #функция с панелью

kittens = Question('Какой породы кошек не существует?', 'усатая', 'русская голубая', 'сфинкс', 'вислоухая')

ask(kittens)

main_win.total = 0
main_win.score = 0


answer.clicked.connect(click_ok)
next_quesion()
main_win.show() #сделать окно видимым
app.exec_()