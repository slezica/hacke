from PIL import Image, ImageDraw, ImageFont

def generate_image(text, output_file='out.png'):
    # til = Image.open("grey-background.jpg")
    size = (800,400)
    bgcolor = (127, 219, 182, 1)
    til = Image.new('RGBA', size, bgcolor)
    im = Image.open("sherk.png")
    til.paste(im, (1050,830), im)

    draw = ImageDraw.Draw(til)
    tcolor = (100,130,110)
    text_pos = (200,500)
    font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 81)
    draw.text(text_pos, text, fill=tcolor, font=font)

    til.save(output_file)

generate_image("nisman did nothing wrong")