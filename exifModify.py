from PIL import Image
import piexif
#https://pypi.org/project/piexif/1.0.8/
#https://piexif.readthedocs.io/en/latest/functions.html
#全部清除
#piexif.remove("foo.jpg")
im = Image.open("./lala.jpg")
exif_dict = piexif.load(im.info["exif"])
 
print(type(exif_dict), exif_dict)
 
for ifd in ("0th", "Exif", "GPS", "1st"):
    for tag in exif_dict[ifd]:
        print(piexif.TAGS[ifd][tag], exif_dict[ifd][tag])
exif_dict["0th"][piexif.ImageIFD.Artist] = "这是作者".encode()
exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = '9999:09:09 09:09:09'.encode()
exif_dict["Exif"][piexif.ExifIFD.LensModel] = 'here'.encode()
exif_dict["Exif"][piexif.ExifIFD.LensMake] = 'wow'.encode()
exif_bytes = piexif.dump(exif_dict)
im.save("lala2.jpg", exif=exif_bytes)
 
print('------------------------------修改后-----------------------------------')
for ifd in ("0th", "Exif", "GPS", "1st"):
    if ifd is "0th":
	    print('------------------------------0th-----------------------------------')
    if ifd is "Exif":
	    print('------------------------------Exif-----------------------------------')
    if ifd is "GPS":
	    print('------------------------------GPS-----------------------------------')
    if ifd is "1st":
	    print('------------------------------1st-----------------------------------')
    for tag in exif_dict[ifd]:
        print(piexif.TAGS[ifd][tag], exif_dict[ifd][tag])