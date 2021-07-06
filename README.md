# Discord Spam Solution
A fun way to give discord spammers a taste of their own medicine.

## ***DISCLAIMER***
Please use this responsibly. This isn't for spamming innocent people or flooding servers.
To the maximum extent permitted by Discord's TOS and common sense, I am not liable to the damages caused by mistakes of judgment or malicious use of this program by the user.

## Setup
Setup is relatively straightforward. 
- Within `main.py`, add one or more messages to the `messages` list. The messages are what will be sent in chat.
- Use `pyautogui.position()` in a command prompt or IDLE to find the correct mouse position for the Discord text box. Make sure that the coordinates are located within the message field in Discord. Enter the x and y coordinates into the `x` and `y` variables in `main.py`
That's all the required configuration for the program to work. Simply run `python main.py` in a command prompt to begin the program.
**NOTE: Do not move the mouse or type on your keyboard while the program is active, it uses your mouse and keyboard to send messages!**

To exit the program, press `Ctrl+C` in the command prompt or press `z` (exit key configurable; see below).

## Other Stuff
There are other settings for character type delay, message delay, exit keybinds, and exit messages. Feel free to adjust them to your liking, though some of them may break functionality if configured incorrectly.
