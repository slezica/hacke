from PIL import Image, ImageDraw, ImageFont
import textwrap

def generate_image(text_lines, output_file='out.png'):
    # settings
    size=(1200, 800)
    bgcolor = (254, 240, 53, 255)
    badge = Image.open("badge.png")
    font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 54)
    margin = offset = 100
    text_color = (100,130,110)

    # prepare assets
    badge.thumbnail(size, Image.ANTIALIAS)
    new = Image.new('RGBA', size, bgcolor)

    # draw text
    draw = ImageDraw.Draw(new)

    for line in text_lines:
        draw.text((margin, offset), line, font=font, fill=text_color)
        offset += font.getsize(line)[1]

    # paste badge
    new.paste(badge,(0, size[1] - badge.size[1]), badge)

    new.save(output_file)

generate_image(["nisman did nothing wrong", "because he's a great man and ", "husband and lover and prosecutor"])