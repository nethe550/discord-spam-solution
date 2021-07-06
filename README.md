# Discord Spam Solution
A fun way to give discord spammers a taste of their own medicine.

## ***DISCLAIMER***
Please use this responsibly. This isn't for spamming innocent people or flooding servers.
To the maximum extent permitted by Discord's TOS, GPL-3.0, and common sense, I am not liable to the damage(s) caused by mistake of judgment or malicious use of this program by the user.

## Setup
Setup is relatively straightforward.
Settings (`config.json`):
- `messages`: a list of messages to send in chat
- `cursor`:
 * `x`: horizontal screen coordinate of Discord message box
 * `y`: vertical screen coordinate of Discord message box
- `delays`:
 * `type`: delay between keypresses when sending a message (0 < delay)
 * `msg`: random range of delays between messages (python interpreted list)
- `exit`:
 * `key`: keypress to exit program
 * `msg`: message displayed in console when program finishes execution

### Steps for proper setup:
1. Find the screen coordinates of your Discord's message box. Use the `find_mouse_coords.py` to get the screen coordinates of your mouse; place your mouse on the Discord message box and enter the x, y values into `config.json`. Make sure you do not move your Discord window after this, or you will have to re-set the coordinates.
2. Add your message(s) to `config.json`. These can be whatever you want, just be sure to escape any special characters with a `\`.
3. Run `python main.py` in the current directory. Sit back and watch the program automatically send messages.

> **NOTE: Do not move the mouse or type on your keyboard while the program is active, it uses your mouse and keyboard to send messages!**

To exit the program, press `Ctrl+C` in the command prompt or press `z` (exit key configurable; see `config.json`).

## Other Stuff
There are other settings for character type delay, message delay, exit keybinds, and exit messages. Feel free to adjust them to your liking, though some of them may break functionality if configured incorrectly. The only configuration that is strictly needed for operation is the Discord message box coordinates, and the custom messages.
