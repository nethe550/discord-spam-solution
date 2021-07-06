#########################
# Discord Spam Solution #
#   by nethe550 (2021)  #
# Under GPL-3.0 license #
#########################

from keyboard import is_pressed, write, send
from pyautogui import moveTo, click

from time import sleep, time, gmtime, strftime
from random import shuffle, choice
from json import loads

def get_new_message():
    new = config["messages"][:]
    shuffle(new)
    return choice(new)

if __name__ == '__main__':
    config = open('./config.json', 'r').read()
    config = loads(config)

    num_of_messages = 0
    start = time()
    
    try:
        while not is_pressed(config["exit"]["key"]):
            moveTo(config["cursor"]["x"], config["cursor"]["y"])
            click()
            write(
                get_new_message(), 
                delay=config["delays"]["type"], 
                restore_state_after=False, 
                exact=None
            )
            sleep(int(choice(eval(config["delays"]["msg"]))))
            send('enter')
            num_of_messages = num_of_messages + 1
    except KeyboardInterrupt:
        end = time()
        elapsed = end - start
        secs = gmtime(round(elapsed))
        time_ = strftime("%H:%M:%S", secs)
        
        print(f'Sent {num_of_messages} messages over a {time_} period.')
        print(config["exit"]["msg"])
        exit()