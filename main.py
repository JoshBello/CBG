import random
import time
from PIL import Image, ImageDraw, ImageFont
import textwrap

parts_dict = {}
# parts = ['adverbs', 'verbs', 'adjectives', 'nouns']
# parts = ['verbs', 'adjectives', 'nouns']
parts = ['adjectives1', 'adjectives2', 'nouns1']
font_path = '/Library/Fonts/Assistant-VariableFont_wght.ttf'
weight = [b'ExtraLight', b'Light', b'Regular', b'SemiBold', b'Bold', b'ExtraBold']

def dict_generator(parts):

    for part in parts:
        with open(f'{part}.txt') as f:
            words = f.read().splitlines()

        parts_dict[part] = words

    return parts_dict


def pick_random_words(parts_dict, parts):

    sentence = []

    for part in parts:
        sentence.append(random.choice(parts_dict[part]))

    sentence_str = ' '.join(sentence)

    return sentence_str


def generate_img(sentence_str: str, session_id):


    base_heights = {1 : 220,
                    2 : 190,
                    3 : 155,
                    4 : 125,
                    5 : 90}

    para = textwrap.wrap(sentence_str, width=25)
    base_height = base_heights[len(para)]
    padding = 18
    width, height = 500, 500

    img = Image.new('RGB', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, 38)
    font.set_variation_by_name('Regular')

    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((width - w) / 2, base_height), line, font=font)
        base_height += h + padding

    file_type = '.png'
    filename = f'{session_id}.{file_type}'

    img.save(filename)

    return filename

def upload_image(filename):

    return url

session_id = '32'

parts_dict = dict_generator(parts)
sentence_str = pick_random_words(parts_dict, parts)
filename = generate_img(sentence_str, session_id)


# url = upload_image(filename)

# @app.get('/')
# async def main(adverb    : str,
#                verb      : str,
#                adjective : str,
#                noun      : str):
#
#
#     url =
#
#
# return f'<img href={url} img>'
