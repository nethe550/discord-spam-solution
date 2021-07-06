from pyautogui import position
from time import sleep

if __name__ == '__main__':
    try:
        while 1:
            print(position())
            sleep(1)
    except KeyboardInterrupt:
        print("Exiting coordinate finder.")
        exit()