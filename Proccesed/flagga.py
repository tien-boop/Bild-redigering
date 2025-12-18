from PIL import Image, ImageDraw, ImageOps

red=(218,37,29)
yellow = (255,255,0)
blue = 	(51, 153, 255)

im = Image.new("RGB",(160,100),red)

imd = ImageDraw.Draw(im)

imd.rectangle([(0,50),(160,100)],blue)

star = Image.open("Images/star.png").convert("RGBA")

star = ImageOps.scale(star,0.05)


im.paste(star, (53, 20), star)
im.show()



im.save("flag.png")

