import exifread
import json
import urllib.request

f = open('1.jpg', 'rb')

tags = exifread.process_file(f)
print(tags)
# 打印所有照片信息，会以键值对的方法保存
for tag in tags.keys():
    print("Key: {0}, value {1}".format(tag, tags[tag]))

# 打印照片其中一些信息
print('拍摄时间：', tags['EXIF DateTimeOriginal'])
print('照相机制造商：', tags['Image Make'])
print('照相机型号：', tags['Image Model'])
print('照片尺寸：', tags['EXIF ExifImageWidth'], tags['EXIF ExifImageLength'])


def getLatOrLng(refKey, tudeKey):
	"""
	获取经度或纬度
	"""
    # type: ignore
    if refKey not in tags:
        return None
    ref = tags[refKey].printable # type: ignore
    LatOrLng = tags[tudeKey].printable[1:-1].replace(" ", "").replace("/", ",").split(",") # type: ignore
    print(LatOrLng)
    LatOrLng = float(LatOrLng[0]) + float(LatOrLng[1]) / 60 + float(LatOrLng[2]) / 3600

    if refKey == 'GPS GPSLatitudeRef' and tags[refKey].printable != "N":
        LatOrLng = LatOrLng * (-1)
    if refKey == 'GPS GPSLongitudeRef' and tags[refKey].printable != "E":
        LatOrLng = LatOrLng * (-1)
    return LatOrLng


# 调用百度地图API通过经纬度获取位置
def getlocation(lat, lng):
    """
    exif里面的经纬度是度分秒形式传入的，需要转换为小数形式，然后根据传入的经纬度,调用百度接口去查询详细地址
    """
    url = "http://api.map.baidu.com/reverse_geocoding/v3/?ak=百度API的AK信息，需要自己去申请&output=json&coordtype=wgs84ll&language_auto=1&extensions_town=true&location=" + lat + "," + lng
    req = urllib.request.urlopen(url)
    res = req.read().decode("utf-8")
    print(res)
    str1 = json.loads(res)
    jsonResult = str1.get('result')
    formatted_address = jsonResult.get('formatted_address')
return formatted_address



lat = getLatOrLng('GPS GPSLatitudeRef', 'GPS GPSLatitude')  # 纬度
lng = getLatOrLng('GPS GPSLongitudeRef', 'GPS GPSLongitude')  # 经度
print('纬度:{0} 经度：{1}'.format(lat, lng))

location = getlocation(str(lat), str(lng))
print('位置：{0}'.format(location))

