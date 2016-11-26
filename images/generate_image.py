from PIL import Image, ImageDraw, ImageFont

# img = Image.open("edu.jpg")
# draw = ImageDraw.Draw(img)

# # font = ImageFont.truetype("sans-serif.ttf", 16)
# # draw.text((0, 0),"Sample Text",(255,255,255),font=font)
# draw.text((10, 10),"Sample Text",(255,255,255))

# img.save('out.jpg')



# font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf",40)
# text = "Sample Text"
# tcolor = (255,0,0)
# text_pos = (100,100)

# img = Image.open("edu.jpg")
# draw = ImageDraw.Draw(img)
# draw.text(text_pos, text, fill=tcolor, font=font)
# del draw

# img.save("out.png")



# from PIL import Image
# back = Image.open('grey-background.jpg')
# img_w, img_h = img.size
# background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
# bg_w, bg_h = background.size
# offset = ((bg_w - img_w) / 2, (bg_h - img_h) / 2)
# background.paste(img, offset)
# background.save('out.png')



# # TRANSPARENCIA
# from PIL import Image

# background = Image.open("grey-background.jpg")
# foreground = Image.open("edu.jpg")

# background.paste(foreground, (0, 0), foreground)
# background.show()



# thumbnail = Image.open('edu.jpg')
# size = (10, 10)
# thumbnail.thumbnail( size , Image.ANTIALIAS) #generating the thumbnail from given size

# offset_x = max((size[0] - thumbnail.size[0]) / 2, 0)
# offset_y = max((size[1] - thumbnail.size[1]) / 2, 0)
# offset_tuple = (offset_x, offset_y) #pack x and y into a tuple

# final_thumb = Image.new(mode='RGBA',size=size,color=(255,255,255,0)) #create the image object to be the final product
# final_thumb.paste(thumbnail, offset_tuple) #paste the thumbnail into the full sized image
# final_thumb.save("out.jpg",'PNG') #save (the PNG format will retain the alpha band unlike JPEG)



til = Image.open("grey-background.jpg")
im = Image.open("edu.jpg") #25x25
til.paste(im, (1050,830))

draw = ImageDraw.Draw(til)
text = "Con ese culo te invito a cagar a casa\n\t @ElOgroMachista"
tcolor = (100,130,110)
text_pos = (200,500)
font = ImageFont.truetype("arial.ttf", 81)
draw.text(text_pos, text, fill=tcolor, font=font)

til.save("out.png")
