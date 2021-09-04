# pip3 install selenium
from selenium import webdriver
import xlrd
import time
import os

start = time.time()

# To run it, we need chrome or firefox driver. Download the driver for platform (Linux/Windows) and for specific
# version of browser
# firefox
# driver = webdriver.Firefox(executable_path='./geckodriver')
# chrome
driver = webdriver.Chrome(executable_path='C:/work/spotphish-data-collection/webpage_to_image/chromedriver_win32/chromedriver')

# path to excel file
loc = "newsites.xls"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)   

# base path to save images
path = "images"


for i in range(2, 98):
    try:
        url = sheet.cell_value(i, 2)                            # url
        image_name = sheet.cell_value(i,1)                      # image name
        class_name = sheet.cell_value(i,0)                      # class name
        image_path = os.path.join(path, class_name)             # path to save image
        
        driver.get(url)                                         # fire up browser, load webpage
        time.sleep(5)
        ret = driver.get_screenshot_as_file(os.path.join(image_path, image_name+'.png'))
        if not ret:
            os.makedirs(image_path, exist_ok=True)
            driver.get_screenshot_as_file(os.path.join(image_path, image_name+'.png'))
        print(i, os.path.join(image_path, image_name+'.png'))
        
    except:
        pass
driver.quit()
end = time.time()
print("end...\ntime taken ", end-start)