import schedule
import time
import datetime
from PIL import ImageGrab
import os


print("Take screenhots daily at 9 AM...")
print("Don't close this window.")

path = "C:\\Users\\HaemOnco\\Documents\\screenshots\\"

def take_screenshot():

    print("take screenshot...")

    date_string = datetime.datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
    folder = datetime.datetime.now().strftime("%d-%m-%Y")

    if not os.path.isdir( path + folder):
        os.mkdir(path + folder) 
    save_path = path + folder + "\\" + date_string + "_DN.png"

    print(save_path)

    snapshot = ImageGrab.grab()

    snapshot.save(save_path)

for hour in range(0, 24): 
    schedule.every().day.at(f"{hour:02d}:00").do(take_screenshot)


while True:
    
    schedule.run_pending()
    time.sleep(60) # wait one minute

#take_screenshot()
    
