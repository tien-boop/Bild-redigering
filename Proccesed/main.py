from PIL import Image, ImageEnhance
aot = Image.open("Images/aot.jpg")

edit_aot = ImageEnhance.Contrast(aot).enhance(0.5)
edit_aot = ImageEnhance.Brightness(aot).enhance(0.5)

edit_aot.save("edit_aot.jpg")
