from pywinauto.keyboard import send_keys
import pywinauto
import time
import pyautogui
import win32api
import win32con


# узнать координаты и цвет
# iml = pyautogui.displayMousePosition()


PLAYER_MIN_HP = None
PLAYER_HP_RGB_COLOR = None

MOB_MIN_HP = None
MOB_HP_RGB_COLOR = None


# список скринов с именами целей
targets_list = ['warewolf_hunter.png', 'warewolf_chieftain.png', 'warewolf.png']

# список имен мобов
targets_names_list = ['vuku orc fighter', 'langk lizardman']
# targets_names_list = ['crasher', 'blade spider', 'talon spider']


def get_target_by_name(lst: list):
    """
    выбор цели с помощью команды /target
    имя цели берется из списка
    """

    for target in lst:
        pyautogui.write(f'/target {target}', interval=0.05)
        pyautogui.press('enter')
        time.sleep(.5)
        if checkIfMob():
            return atack()
        time.sleep(.5)


def befor_start_settings(text: str) -> tuple:
    """
    настраиваем координаты и цвет хп
    """

    pyautogui.alert(text)
    x, y = pyautogui.position()
    color = pyautogui.pixel(x, y)
    return ( (x, y), (color[0], color[1], color[2]) )


def click(x, y):
    """функция нажатия левой кнопки мыши в указанные координаты x и y"""
    
    win32api.SetCursorPos((x, y))
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def checkIfMob() -> bool:
    """проверка выбран ли бот и жив ли он еще"""

    return pyautogui.pixelMatchesColor(MOB_MIN_HP[0], MOB_MIN_HP[1], MOB_HP_RGB_COLOR, tolerance=10)
    

def checkHp():
    """проверяет уровень HP (цвет в указанных ранее координатах) и если надо, пьет банку"""

    if not pyautogui.pixelMatchesColor(PLAYER_MIN_HP[0], PLAYER_MIN_HP[1], PLAYER_HP_RGB_COLOR, tolerance=10):
        pyautogui.press('f5')


def nextTarget():
    """выбор следующей цели"""

    print('Ищу жертву...')
    pyautogui.press('f2')
    if checkIfMob():
        atack()


def turnRight():
    """поворот нарпаво"""

    pyautogui.keyDown("left")
    time.sleep(1)
    pyautogui.keyUp("left")


def atack():
    """атака бота"""

    print('Вижу цель - В АТАКУ!!!')
    while checkIfMob():
        pyautogui.press('f1')
        pyautogui.press('f3')
        checkHp()
        cantSeeTagetCheck()
    get_loot()


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
        pyautogui.press("f4")
        checkHp()
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


def cantSeeTagetCheck():
    """Если не видит цель, жмет ESC"""

    img = pyautogui.locateOnScreen('cantseetarget.png', grayscale=True, confidence=0.8)
    if img != None:
        print('Не вижу цель')
        for _ in range(5):
            pyautogui.press("esc")


def main():
    time.sleep(3)
    while True:
        checkHp()
        if checkIfMob():
            atack()
        else:
            get_loot()
            nextTarget()
            # if not getImageFromScreen():
            #     turnRight()
            get_target_by_name(targets_names_list)
                


if __name__ == '__main__':
    time.sleep(5)
    PLAYER_MIN_HP, PLAYER_HP_RGB_COLOR = befor_start_settings('Установите курсор на HP игрока для настройки хила банкой и нажмите ENTER')
    MOB_MIN_HP, MOB_HP_RGB_COLOR = befor_start_settings('Установите курсор на минимальной отметке HP моба и нажмите ENTR')
    main()

