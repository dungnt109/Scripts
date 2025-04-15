import schedule
import time
import datetime
import pyscreenshot as ImageGrab
#from PIL import ImageGrab
import os
from PIL import Image

print("take screenthots...")

path = "/home/dungnt/Downloads/tms/" 
#path = "C:\\Users\\HaemOnco\\Documents\\screenshots\\"

separator = "/"  
#separator = "\\"

def take_screenshot():

	

	current_time = datetime.datetime.now()

	year = str(current_time.year) 

	month = current_time.strftime("%m")

	date_string = current_time.strftime("%d-%m-%Y_%H_%M_00")
	folder = current_time.strftime("%d-%m-%Y")

	if not os.path.isdir( path + year + separator + month + separator + folder ):

		os.makedirs(path + year + separator + month + separator + folder) 

	save_path = path + year + separator + month + separator + folder + separator + date_string 

	print(save_path)

	snapshot = ImageGrab.grab()


	width, height = snapshot.size


	new_size = (int(width * 3/4), int(height * 3/4))
	resized_snapshot = snapshot.resize(new_size, Image.LANCZOS)


	resized_snapshot.convert("RGB").save(save_path + ".jpg", "JPEG")
	resized_snapshot.save(save_path + ".webp", "WEBP")

	print("take screenshot at " + date_string)

for hour in range(0, 12): 
    #schedule.every().day.at(f"{hour:02d}:00").do(take_screenshot)
    schedule.every().hour.at(":"+str(hour*5).zfill(2)).do(take_screenshot)


#while True:
    
#    schedule.run_pending()
#    time.sleep(60) # wait one minute

take_screenshot()
    
