# To install pyautogui use command 'pip install pyautogui'
import pyautogui as screen
import random
import time

screen.FAILSAFE=False
def fetchTime(seconds):
  hours = seconds // 3600
  remaining_seconds = seconds % 3600
  minutes = remaining_seconds // 60
  seconds = remaining_seconds % 60
  hours_str = f"{hours:02d}"
  minutes_str = f"{minutes:02d}"
  seconds_str = f"{seconds:02d}"
  return f"{hours_str}:{minutes_str}:{seconds_str}"

time_unit=10
count=0
message='Jai Shree Ram'
try:
    while True:
        time.sleep(time_unit)
        screen.typewrite(message)
        screen.hotkey('enter')
        count=count+1
except KeyboardInterrupt:
    print("\nTotal Count:"+str(count)+", Duration: "+fetchTime(count*time_unit))

    
