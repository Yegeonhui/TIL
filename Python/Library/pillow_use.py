from PIL import Image
from PIL.ExifTags import TAGS


def getEXIF(self, JPGName):
    img = Image.open(JPGName)
    info = img._getexif()
    img.close()

    taglabel = {}
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        taglabel[decoded] = value

    # Latitude
    latDeg = float(taglabel['GPSInfo'][2][0])
    latMin = float(taglabel['GPSInfo'][2][1])
    latSec = float(taglabel['GPSInfo'][2][2])
    lat = latDeg + (latMin / 60) + (latSec / 3600)

    # Longitude
    lonDeg = float(taglabel['GPSInfo'][4][0])
    lonMin = float(taglabel['GPSInfo'][4][1])
    lonSec = float(taglabel['GPSInfo'][4][2])
    lon = lonDeg + (lonMin / 60) + (lonSec / 3600)