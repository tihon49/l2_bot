from pywinauto import application
from pywinauto.keyboard import send_keys
import pywinauto
import time
import pyautogui
# import keyboard
import win32api
import win32con
import random

from utils import *


# узнать координаты и цвет
# iml = pyautogui.displayMousePosition()

# список скринов с именами целей
targets_list = ['warewolf_hunter.png', 'warewolf_chieftain.png', 'warewolf.png']
targets_names_list = ['werewolf hunter', 'werewolf chieftain', 'werewolf']


def get_target_by_name(lst: list):
    for target in lst:
        split_name = target.split()
        send_keys(f"/target")
        for name_part in split_name:
            send_keys("{VK_SPACE down}")
            send_keys("{VK_SPACE up}")
            send_keys(name_part)

        send_keys("{VK_RETURN down}"
                  "{VK_RETURN up}")
        if checkIfMod():
            atack()
        time.sleep(.5)



def getImageFromScreen():
    """
    проходит по списку скринов с именами целей
    если видит на экране совпадение со скрином кликает по нему или рядом
    и выходит из цикла
    """

    for target in targets_list:
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


def main():
    time.sleep(3)
    while True:
        checkHp()
        if checkIfMod():
            atack()
        else:
            get_loot()
            nextTarget()
            # if not getImageFromScreen():
            #     turnRight()
            get_target_by_name(targets_names_list)
                


if __name__ == '__main__':
    time.sleep(5)
    main()



















# time.sleep(15)
# for i in range(10):
#     time.sleep(5)
#     pywinauto.mouse.click(button='left', coords=(520, 432))
#     time.sleep(1)
#     send_keys('tihon49')
#     time.sleep(2)
#     pywinauto.mouse.click(button='left', coords=(520, 455))
#     send_keys('7111354')
