# Игра крестики нолики, алгоритм взят с ДЗ 5.
# использовано виртуальное окружение (версия python понижена до 3.9 т.к. на 3.10 не устанавливается pyqt5-tools)
# прикручен Qt GUI, . Для разработки внешнего вида формы применен Qt Designer

# Q: получить список объектов - ?

import sys
from PyQt5 import QtWidgets
import MainForm as mForm
import numpy as np
import random

class RunForm(QtWidgets.QMainWindow, mForm.Ui_MainWindow):
    # ходы игрового поля
    fields = np.zeros((3, 3))
    # выбор игрока
    active_gamer = 0
    #кол-во побед 1 игрока
    win_cnt_1 = 0
    win_cnt_2 = 0
    #кол-во побед 2 игрока

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setEnableBtn(False)

        # привязка событий
        self.btnQuit.clicked.connect(self.quit)
        self.btnStart.clicked.connect(self.game_start)
        self.b00.clicked.connect(self.field_click)
        self.b01.clicked.connect(self.field_click)
        self.b02.clicked.connect(self.field_click)
        self.b10.clicked.connect(self.field_click)
        self.b11.clicked.connect(self.field_click)
        self.b12.clicked.connect(self.field_click)
        self.b20.clicked.connect(self.field_click)
        self.b21.clicked.connect(self.field_click)
        self.b22.clicked.connect(self.field_click)

    # нажатие на поле (ход игрока)
    def field_click(self):
        snd = self.sender()
        x = int(snd.objectName()[1])
        y = int(snd.objectName()[2])

        self.fields[x, y] = 1 if self.active_gamer == 1 else 4

        if self.active_gamer == 1:
            snd.setText('Х')
        else:
            snd.setText('0')

        info_text = ''
        game_result = self.game_over()
        # проверить победу
        if game_result == 1:
            info_text = 'Победа игрока 1'
            self.win_cnt_1 += 1
            self.cntGamer1.display(self.win_cnt_1)
        elif game_result == 2:
            info_text = 'Победа игрока 2'
            self.win_cnt_2 += 1
            self.cntGamer2.display(self.win_cnt_2)
        elif game_result == 3:
            info_text = 'Ничья'
        else:
            self.active_gamer = 1 if self.active_gamer == 2 else 2
            info_text = f'Ход игрока {self.active_gamer}'

        self.lbInfo.setText(info_text)
        if game_result > 0:
            self.setEnableBtn(False)


    # проверка окончания игры
    # 0 - игра не окончена
    # 1 - победа 1го игрока
    # 2 - победа второго
    # 3 - ничья
    def game_over(self) -> int:
        # проверить победу 1го игрока
        win = sum(np.diagonal(self.fields, 0)) == 3 or sum(np.diagonal(self.fields, 1)) == 3
        for i in range(0, 3):
            win = win or sum(self.fields[:, i]) == 3 or sum(self.fields[i, :]) == 3
        if win:
            return 1

        # проверить победу 2го игрока
        win = sum(np.diagonal(self.fields, 0)) == 12 or sum(np.diagonal(self.fields, 1)) == 12
        for i in range(0, 3):
            win = win or sum(self.fields[:, i]) == 12 or sum(self.fields[i, :]) == 12
        if win:
            return 2

        # проверить ничью
        if (self.fields == 0).sum() == 0:
            return 3

        # играем дальше
        return 0


    # завершение работы
    def quit(self):
        self.close()

    # старт игры
    def game_start(self):
        # обнулить игровой массив
        self.fields.fill(0)
        # жеребъевка активного игрока
        self.active_gamer = random.randint(1, 2)
        # включить поле
        self.setEnableBtn(True)
        self.clearField()
        # Информация
        self.lbInfo.setText(f'Ход игрока {self.active_gamer}')

    # активировать / деактивировать поле
    def setEnableBtn(self, enable):
        self.b00.setEnabled(enable)
        self.b01.setEnabled(enable)
        self.b02.setEnabled(enable)
        self.b10.setEnabled(enable)
        self.b11.setEnabled(enable)
        self.b12.setEnabled(enable)
        self.b20.setEnabled(enable)
        self.b21.setEnabled(enable)
        self.b22.setEnabled(enable)

    # очистить поле
    def clearField(self):
        # обнуление поля при активации/деактивации
        self.b00.setText('')
        self.b01.setText('')
        self.b02.setText('')
        self.b10.setText('')
        self.b11.setText('')
        self.b12.setText('')
        self.b20.setText('')
        self.b21.setText('')
        self.b22.setText('')


## MAIN ###
def main():
    app = QtWidgets.QApplication(sys.argv)
    win = RunForm()
    win.show()
    app.exec_()

if __name__ == "__main__":
    main()
