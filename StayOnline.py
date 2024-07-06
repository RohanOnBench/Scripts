# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                  Please Follow Me Here                  #
#  Youtube    :                                           #
#  Instagram  :                                           #
#  X(Twitter) :                                           #
#  Facebook   :                                           #
#                                                         #
# To install pyautogui use command 'pip install pyautogui'#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import pyautogui as screen
import time

time_unit=10
count=0
message='|| Jai Shree Ram |'

start=time.time()
try:
    while True:
        time.sleep(time_unit)
        for c in message:
            screen.press(c)
        screen.press('|')
        screen.press('enter')
        count=count+1
except KeyboardInterrupt:
    end=time.time()
    duration=time.strftime('%H:%M:%S',time.gmtime(round(end-start)))
    print("\nTotal Count: "+str(count)+", Duration: "+duration)

    
