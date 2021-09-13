from pywinauto import application
from pywinauto.keyboard import send_keys
import pywinauto
import time
import pyautogui
import win32api
import win32con
import random



def click(x, y):
    """функция нажатия левой кнопки мыши в указанные координаты x и y"""
    
    win32api.SetCursorPos((x, y))
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def checkIfMod() -> bool:
    """проверка выбран ли бот и жив ли он еще"""

    MOB_HB_COORDINATES = (444, 103)
    MOB_HP_COLOR = (231, 73, 132)
    if pyautogui.pixel(MOB_HB_COORDINATES[0], MOB_HB_COORDINATES[1]) == MOB_HP_COLOR:
        return True
    return False


def lowHp():
    """Если мало жизней"""

    if not pyautogui.pixel(122, 122) == (181, 0, 24):
        return True
    return False
    

def checkHp():
    """проверяет уровень HP и если надо, пьет банку"""

    if lowHp():
        send_keys("{VK_F5 down}"
                  "{VK_F5 up}")


def nextTarget():
    """выбор следующей цели"""

    print('Ищу жертву...')
    send_keys("{VK_F2 down}"
              "{VK_F2 up}")
    if checkIfMod():
        atack()


def turnRight():
    """поворот нарпаво"""

    send_keys("{VK_RIGHT down}")
    time.sleep(1)
    send_keys("{VK_RIGHT up}")


def atack():
    """атака бота"""

    print('Вижу цель - В АТАКУ!!!')
    while checkIfMod():
        send_keys("{VK_F1 down}"
                  "{VK_F1 up}")
        checkHp()
        time.sleep(.2)


def run_around():
    """если нет мобов, бегаем по окрестности"""

    # TODO: какая-то хуета получается, надо доработать
    send_keys("{VK_UP down}"
              "{VK_UP up}")
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0)


def get_loot():
    """подобрать лут"""

    print('Ищу лут')
    for _ in range(4):
        nextTarget()
        send_keys("{VK_F4 down}"
                  "{VK_F4 up}")
        checkHp()
        time.sleep(.5)
