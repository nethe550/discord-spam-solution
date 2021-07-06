from pyautogui import moveTo, click
from keyboard import is_pressed, write, send
from random import shuffle, choice
from time import sleep


def get_new_message():
    new = messages[:]
    shuffle(new)
    return choice(new)

if __name__ == '__main__':
    # add messages to fit your taste
    messages = [
        "",
    ]

    # put the x, y coords of the discord text box on your screen here
    # use pyautogui.position() to output current mouse position to find the coords easier
    x = 2508
    y = 1018
    
    # delay between each keypress (note: setting this to 0 will freeze the program)
    #  default: 0.001
    type_delay = 0.001
    
    # delay between each message send
    #   default: range(0, 20)
    msg_delay = [x for x in range(0, 20)]
    
    # key to exit program
    #   default: 'z'
    exit_key = 'z'
    
    # program exit message (optional)
    #   default: "sufficiently annoyed spammers"
    exit_msg = "sufficiently annoyed spammers"
    
    
    # =============== # =============== # =============== #
    
    
    while not is_pressed(exit_key):
        moveTo(x, y)
        click()
        write(get_new_message(), delay=type_delay, restore_state_after=False, exact=None)
        sleep(choice([x for x in range(0, 20)]))
        send('enter')
    print(exit_msg)