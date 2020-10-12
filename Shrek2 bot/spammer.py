import  pyautogui, time, os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'script')

time.sleep(5)

f = open(filename,"r")

for word in f:
    pyautogui.typewrite(word)iram
    pyautogui.press("enter")

