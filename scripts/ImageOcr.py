#-*-coding:utf-8-*-
from aip import AipOcr


"""APPID AK SK """

APP_ID="14428712"
API_KEY="AWvhbHqO0ZRN7cSqedQqYqjf"
SECRET_KEY="Y20qKyMR9GTbip98tFlGWwtxZ6V6hIsH"


"""通用文字识别（含位置信息版） 请求参数详情

##参数名称      是否必选        类型    可选值范围      默认值  说明
##image 是      string                  图像数据，base64编码，要求base64编码后大小不超过4M，最短边至少15px，最长边最大4096px,支持
jpg/png/bmp格式
##url   是      string                  图片完整URL，URL长度不超过1024字节，URL对应的图片base64编码后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式，当image字段存在时url字段失效
##recognize_granularity 否      string  big - 不定位单字符位置
##small - 定位单字符位置        small   是否定位单字符位置，big：不定位单字符位置，默认值；small：定位单字符位置
##language_type 否      string  CHN_ENG
##ENG
##POR
##FRE
##GER
##ITA
##SPA
##RUS
##JAP
##KOR
##CHN_ENG       识别语言类型，默认为CHN_ENG。可选值包括：
##- CHN_ENG：中英文混合；
##- ENG：英文；
##- POR：葡萄牙语；
##- FRE：法语；
##- GER：德语；
##- ITA：意大利语；
##- SPA：西班牙语；
##- RUS：俄语；
##- JAP：日语；
##- KOR：韩语；
##detect_direction      否      string  true
##false
##false 是否检测图像朝向，默认不检测，即：false。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。可选值包括:
##- true：检测朝向；
##- false：不检测朝向。
##detect_language       否      string  true
##false
##false 是否检测语言，默认不检测。当前支持（中文、英语、日语、韩语）
##vertexes_location     否      string  true
##false
##false 是否返回文字外接多边形顶点位置，不支持单字位置。默认为false
##probability   否      string  true
##false
##是否返回识别结果中每一行的置信度
##通用文字识别（含位置信息版） 返回数据参数详情
##
##字段  必选    类型    说明
##direction     否      number  图像方向，当detect_direction=true时存在。
##- -1:未定义，
##- 0:正向，
##- 1: 逆时针90度，
##- 2:逆时针180度，
##- 3:逆时针270度
##log_id        是      number  唯一的log id，用于问题定位
##words_result  是      array   定位和识别结果数组
##words_result_num      是      number  识别结果数，表示words_result的元素个数
##+vertexes_location    否      array   当前为四个顶点: 左上，右上，右下，左下。当vertexes_location=true时存在
##++x   是      number  水平坐标（坐标0点为左上角）
##++y   是      number  垂直坐标（坐标0点为左上角）
##+location     是      array   位置数组（坐标0点为左上角）
##++left        是      number  表示定位位置的长方形左上顶点的水平坐标
##++top 是      number  表示定位位置的长方形左上顶点的垂直坐标
##++width       是      number  表示定位位置的长方形的宽度
##++height      是      number  表示定位位置的长方形的高度
##+words        否      number  识别结果字符串
##+chars        否      array   单字符结果，recognize_granularity=small时存在
##++location    是      array   位置数组（坐标0点为左上角）
##+++left       是      number  表示定位位置的长方形左上顶点的水平坐标
##+++top        是      number  表示定位位置的长方形左上顶点的垂直坐标
##+++width      是      number  表示定位定位位置的长方形的宽度
##+++height     是      number  表示位置的长方形的高度
##++char        是      string  单字符识别结果
##probability   否      object  行置信度信息；如果输入参数 probability = true 则输出
##+ average     否      number  行置信度平均值
##+ variance    否      number  行置信度方差
##+ min 否      number  行置信度最小值
##通用文字识别（含位置信息版） 返回示例
##
##{
##"log_id": 3523983603,
##"direction": 0, //detect_direction=true时存在
##"words_result_num": 2,
##"words_result": [
##    {
##        "location": {
##            "left": 35,
##            "top": 53,
##            "width": 193,
##            "height": 109
##        },
##        "words": "感动",
##        "chars": [    //recognize_granularity=small时存在
##            {
##                "location": {
##                    "left": 56,
##                    "top": 65,
##                    "width": 69,
##                    "height": 88
##                },
##                "char": "感"
##            },
##            {
##                "location": {
##                    "left": 140,
##                    "top": 65,
##                    "width": 70,
##                    "height": 88
##                },
##                "char": "动"
##            }
##        ]
##    }
##    ...
##]
##}"""
""" 如果有可选参数 """
#options = {}
#options["language_type"] = "JAP"
#options["detect_direction"] = "true"
#options["detect_language"] = "true"
#options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为远程url图片 """
#print(client.general(image1, options))

class ImageOcr:
    def __init__(self):
        self.client = AipOcr(APP_ID,API_KEY,SECRET_KEY)
    def get_file_content(self,filePath):
        with open(filePath,"rb") as fp:
            return fp.read()
    def get_image_info_for_cloud(self,image,language,detect_direction="true",detect_language="true"):
        options = {}
        options["language_type"] = language
        options["detect_direction"] = detect_direction

        options["detect_language"] = detect_language
        options["probability"] = "true"
        return self.client.general(image,options)
    def getDicValueByKey(self,dic, key):
        if dic.has_key(key) == True:
            return dic[key]
        else:
            return -1
    def encode_utf8(self,string):
        return string.encode('utf-8')
    def decode_utf8(self,string):
        return unicode(string, encoding='utf-8')
    def get_X_Y_axisByString(self,imginfo, val):
        wdnum = self.getDicValueByKey(imginfo, "words_result_num")
        if wdnum > 0:
            for dic in imginfo["words_result"]:
                if dic.get("words") == val:
                    x = dic["location"]["left"] + dic["location"]["width"] / 2
                    y = dic["location"]["top"] + dic["location"]["height"] / 2
                    return (x, y)
            return None
        else:
            return None
    def get_words_from_info(self,imginfo):
        wdnum = self.getDicValueByKey(imginfo, "words_result_num")
        if wdnum > 0:
            for dic in imginfo["words_result"]:
                print dic.get("words")

#image = get_file_content("screen.png")

#print(client.basicGeneral(image))
