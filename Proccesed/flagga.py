from PIL import Image, ImageDraw 

red=(218,37,29)
yellow = (255,255,0)
blue = 	(51, 153, 255)

star = Image.open("Images/star.png")

im = Image.new("RGB",(160,100),red)

imd = ImageDraw.Draw(im)

imd.rectangle([(0,50),(160,50)],blue)
imd.rectangle([(50, 0), (70, 100)], blue)


im.save("flag.png")

