from pywinauto.keyboard import send_keys
import pywinauto
import time
import pyautogui
import win32api
import win32con
import random

from utils import click



class Destroyer:
    """Класс дестроера"""

    def __init__(self, hp_lvl, hp_color):
        """установка уровня и цвета ХП при котором следует начинать пить хилки"""

        self.hp_lvl = hp_lvl        # tuple с координатами: (x, y)
        self.hp_color = hp_color    # tuple RGB: (red, green, blue) 

    def set_target_hp(self, mob_min_hp, mob_hp_color):
        """установка уровня и цвета ХП моба, до какого момента он считается живым и его следует продолжать бить"""

        self.mob_min_hp = mob_min_hp        # tuple с координатами: (x, y)
        self.mob_hp_color = mob_hp_color    # tuple RGB: (red, green, blue) 

    def checkHp(self):
        """проверяет уровень HP (цвет в указанных ранее координатах) и если надо, пьет банку"""

        if not pyautogui.pixelMatchesColor(self.hp_lvl[0], self.hp_lvl[1], self.hp_color, tolerance=10):
            pyautogui.press('5')

    def get_target_by_name(self, lst: list):
        """
        выбор цели с помощью команды /target
        имя цели берется из списка
        """

        target = random.choice(lst)
        pyautogui.press('enter')
        pyautogui.write(f'/target {target}', interval=0.01)
        pyautogui.press('enter')
        time.sleep(.5)
        if self.isMob():
            return self.atack()
        time.sleep(.5)

    def getImageFromScreen(self, png_targrts_list: list):
        """
        проходит по списку скринов с именами целей
        если видит на экране совпадение со скрином кликает по нему или рядом
        и выходит из цикла
        """

        for target in png_targrts_list:
            img = pyautogui.locateOnScreen(target, confidence=0.5)
            if img != None:
                print(f'Вижу Моба: {target.split(".")[0]}')
                x, y, w, h= img.left, img.top, img.width, img.height
                click(x + int( w / 2 ), y + h*3)
                time.sleep(.1)
                return True
            else:
                print('Нихуя не вижу.')
                return False

    def isMob(self) -> bool:
        """проверка выбран ли бот и жив ли он еще"""

        return pyautogui.pixelMatchesColor(self.mob_min_hp[0], self.mob_min_hp[1], self.mob_hp_color, tolerance=10)

    def nextTarget(self):
        """выбор следующей цели"""

        print('Ищу жертву...')
        pyautogui.press('2')
        pyautogui.press('7')
        if self.isMob():
            self.atack()

    def atack(self):
        """атака бота"""

        print('Вижу цель - В АТАКУ!!!')
        while self.isMob():
            pyautogui.press('1')
            pyautogui.press('3')
            time.sleep(1)
            self.checkHp()
            self.cantSeeTagetCheck()
        self.get_loot()

    def get_loot(self):
        """подобрать лут"""

        print('Ищу лут')
        for _ in range(3):
            self.nextTarget()
            pyautogui.press("4")
            self.checkHp()
            time.sleep(.3)

    def cantSeeTagetCheck(self):
        """Если не видит цель, жмет ESC"""

        img = pyautogui.locateOnScreen('cantseetarget.png', confidence=.4)
        if img != None:
            print('Не вижу цель')
            for _ in range(3):
                pyautogui.press("esc")

    def turnRight(self):
        """поворот нарпаво"""

        pyautogui.keyDown("left")
        time.sleep(1)
        pyautogui.keyUp("left")

    def run_around(self):
        """если нет мобов, бегаем по окрестности"""

        # TODO: какая-то хуета получается, надо доработать
        send_keys("{VK_UP down}"
                "{VK_UP up}")
        win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0)