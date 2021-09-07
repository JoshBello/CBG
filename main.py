import random
import pprint as pp
from PIL import Image, ImageDraw, ImageFont
import textwrap


parts_dict = {}
parts = ['adverbs', 'verbs', 'adjectives', 'nouns']
font_path = '/Library/Fonts/Assistant-VariableFont_wght.ttf'
weight = [b'ExtraLight', b'Light', b'Regular', b'SemiBold', b'Bold', b'ExtraBold']
# font_path = '/Library/Fonts/Arial.ttf'

def dict_generator(parts):

    for part in parts:
        with open(f'{part}.txt') as f:
            words = f.read().splitlines()

        parts_dict[part] = words


def pick_random_words(parts_dict, parts):

    sentence = []

    for part in parts:
        sentence.append(random.choice(parts_dict[part]))

    sentence_str = ' '.join(sentence)

    return sentence_str

dict_generator(parts)
sentence_str = pick_random_words(parts_dict, parts)

sentence_str = 'You can using You You can using You You can using You You can using You You can using You You can using You'
para = textwrap.wrap(sentence_str, width=25)

base_heights = {1 : 220,
                2 : 190,
                3 : 155,
                4 : 125,
                5 : 90}

width, height = 500, 500
img = Image.new('RGB', (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font_path, 38)
font.set_variation_by_name('Regular')

base_height = base_heights[len(para)]
padding = 18

for line in para:
    w, h = draw.textsize(line, font=font)
    draw.text(((width - w) / 2, base_height), line, font=font)
    base_height += h + padding

img.save('test.png')
