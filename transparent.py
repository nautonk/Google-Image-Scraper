import concurrent.futures
import glob
import os
import time

from RemoveBG import RemoveBG
from patch import webdriver_executable


def worker_tread(image_path):
    removeBG.openService()
    linkDownload = removeBG.uploadImage(image_path)
    removeBG.save_image(linkDownload)

    time.sleep(10)

if __name__ == "__main__":
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))
    headless = False
    number_of_workers = 1
    images_target = list()

    removeBG = RemoveBG(webdriver_path,headless)
    driver = removeBG.getDriver()

    for name in glob.glob(image_path + '/*/*.*'):
        images_target.append(name)

    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_workers) as executor:
        executor.map(worker_tread, images_target)
