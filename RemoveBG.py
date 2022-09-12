import io
import os
from urllib.parse import urlparse

import patch
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RemoveBG():

    def __init__(self, webdriver_path, headless=True):
        # check if chromedriver is updated
        while (True):
            try:
                # try going to www.google.com
                options = Options()
                if (headless):
                    options.add_argument('--headless')
                    # options.add_argument('--headless')
                    # options.add_argument('--no-sandbox')
                    # options.add_argument('--disable-dev-shm-usage')
                    # print(webdriver_path)

                profile_path = os.path.normpath(os.path.join(os.getcwd(), 'profiles'))
                options.add_argument(f"user-data-dir={profile_path}")
                options.add_experimental_option("useAutomationExtension", False)
                options.add_experimental_option("excludeSwitches", ["enable-automation"])
                # options.add_argument("--incognito")
                driver = webdriver.Chrome(webdriver_path, chrome_options=options)
                driver.set_window_size(1400, 1050)
                break
            except:
                # patch chromedriver if not available or outdated
                try:
                    driver
                except NameError:
                    is_patched = patch.download_lastest_chromedriver()
                else:
                    is_patched = patch.download_lastest_chromedriver(driver.capabilities['version'])
                if (not is_patched):
                    exit(
                        "[ERR] Please update the chromedriver.exe in the webdriver folder according to your chrome version:https://chromedriver.chromium.org/downloads")

        self.driver = driver

    def getDriver(self):
        return self.driver

    def openService(self):
        self.driver.get('https://www.remove.bg/upload')

    def uploadImage(self, image_path):
        self.image_path = image_path
        uploadArea = self.driver.find_element_by_xpath('//*[@id="page-content"]')
        self.drag_and_drop_file(uploadArea, image_path)

        # wait till download visible
        wait = WebDriverWait(self.driver, 50000)
        try:
            selectorDownload = "//a[contains(text(),'Download')]"
            wait.until(EC.visibility_of_element_located((By.XPATH, selectorDownload)))
            linkDownload = self.driver.find_element_by_xpath(selectorDownload).get_attribute('href')

            return linkDownload
        except:
            return False

    def closeResult(self):
        wait = WebDriverWait(self.driver, 50000)
        self.driver.find_element_by_xpath("//a[contains(text(),'×')]").click()
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//a[contains(text(),'×')]")))

    def drag_and_drop_file(self, drop_target, path):
        JS_DROP_FILE = "for(var b=arguments[0],k=arguments[1],l=arguments[2],c=b.ownerDocument,m=0;;){var e=b.getBoundingClientRect(),g=e.left+(k||e.width/2),h=e.top+(l||e.height/2),f=c.elementFromPoint(g,h);if(f&&b.contains(f))break;if(1<++m)throw b=Error('Element not interractable'),b.code=15,b;b.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var a=c.createElement('INPUT');a.setAttribute('type','file');a.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');a.onchange=function(){var b={effectAllowed:'all',dropEffect:'none',types:['Files'],files:this.files,setData:function(){},getData:function(){},clearData:function(){},setDragImage:function(){}};window.DataTransferItemList&&(b.items=Object.setPrototypeOf([Object.setPrototypeOf({kind:'file',type:this.files[0].type,file:this.files[0],getAsFile:function(){return this.file},getAsString:function(b){var a=new FileReader;a.onload=function(a){b(a.target.result)};a.readAsText(this.file)}},DataTransferItem.prototype)],DataTransferItemList.prototype));Object.setPrototypeOf(b,DataTransfer.prototype);['dragenter','dragover','drop'].forEach(function(a){var d=c.createEvent('DragEvent');d.initMouseEvent(a,!0,!0,c.defaultView,0,0,0,g,h,!1,!1,!1,!1,0,null);Object.setPrototypeOf(d,null);d.dataTransfer=b;Object.setPrototypeOf(d,DragEvent.prototype);f.dispatchEvent(d)});a.parentElement.removeChild(a)};c.documentElement.appendChild(a);a.getBoundingClientRect();return a;"
        driver = self.driver
        file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
        file_input.send_keys(path)

    def save_image(self, image_url):
        image = requests.get(image_url, timeout=5)
        if image.status_code == 200:
            with Image.open(io.BytesIO(image.content)) as image_from_web:
                # extact filename without extension from URL
                o = urlparse(image_url)
                image_url = o.scheme + "://" + o.netloc + o.path
                name = os.path.splitext(os.path.basename(image_url))[0]
                # join filename and extension
                filename = "%s.%s" % (name.replace('-removebg-preview',''), image_from_web.format.lower())
                original_path_location = os.path.dirname(self.image_path)+'/transparent'

                if not os.path.exists(original_path_location):
                    print("[INFO] Image path not found. Creating a new folder.")
                    os.makedirs(original_path_location)

                image_path = os.path.join(original_path_location, filename)
                print(f"[INFO] Image saved at: {image_path}")
                image_from_web.save(image_path)
                image_from_web.close()
                
        self.closeResult()
