# -*- coding: utf-8 -*-
from ImageOcr import ImageOcr
from AdbClient import adbClient
import json
import time

webpath = "https://item.mercari.com/jp/m19636521815/"
##web browser string list
webBuyStr = u"購入画面に進む"
appBuyStr = u"アプリで購入"

## app string list
AppFirtBuyStr = u"購入手続きへ"
AppSeconBuyStr = u"購入する"


Igor = ImageOcr()
adb = adbClient()

def delayS(sec):
    time.sleep(sec)
def getXYaxis(adb,Igor,match_str):
    ImagePath = adb.get_screenshot()
    image = Igor.get_file_content(ImagePath)
    imageinfo = Igor.get_image_info_for_cloud(image, "JAP")
    (x, y) = Igor.get_X_Y_axisByString(imageinfo, match_str)
    return (x,y)

print adb.connect_to_virtualmachine()
print adb.getdevices()
adb.open_web_with_browser(webpath)
delayS(15)
adb.swipe_action(320,1100,320,250,600)

x,y=getXYaxis(adb,Igor,appBuyStr)
print(x,y)
adb.click_action(x,y)
delayS(3)
x,y = getXYaxis(adb,Igor,AppFirtBuyStr)
adb.click_action(x,y)
