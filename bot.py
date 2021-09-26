import time
import pyautogui
import win32api
import win32con
from destroyer import Destroyer


# список скринов с именами целей
targets_png_list = ['warewolf_hunter.png', 'warewolf_chieftain.png', 'warewolf.png']

# список имен мобов
targets_names_list = ['giant mist leech', 'gray ant']


def befor_start_settings(text: str) -> tuple:
    """
    настраиваем координаты и цвет хп
    """

    pyautogui.alert(text)
    x, y = pyautogui.position()
    color = pyautogui.pixel(x, y)
    return (x, y), (color[0], color[1], color[2])


def main():
    PLAYER_MIN_HP, PLAYER_HP_RGB_COLOR = befor_start_settings('Установите курсор на HP игрока для настройки хила банкой и нажмите ENTER')
    MOB_MIN_HP, MOB_HP_RGB_COLOR = befor_start_settings('Установите курсор на минимальной отметке HP моба и нажмите ENTER')
    
    destr = Destroyer(PLAYER_MIN_HP, PLAYER_HP_RGB_COLOR)
    destr.set_target_hp(MOB_MIN_HP, MOB_HP_RGB_COLOR)
    time.sleep(3)

    while True:
        destr.checkHp()
        if destr.isMob():
            destr.atack()
        else:
            destr.get_loot()
            destr.nextTarget()
            destr.get_target_by_name(targets_names_list)
                

if __name__ == '__main__':
    time.sleep(5)
    main()

