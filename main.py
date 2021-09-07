import random
import pprint as pp
from PIL import Image, ImageDraw, ImageFont
import textwrap


parts_dict = {}
parts = ['adverbs', 'verbs', 'adjectives', 'nouns']

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

para = textwrap.wrap(sentence_str, width=25)

base_heights = {2 : 200,
                3 : 175,
                4 : 145}

width, height = 500, 500
img = Image.new('RGB', (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 34)

base_height = base_heights[len(para)]
padding = 18

for line in para:
    w, h = draw.textsize(line, font=font)
    draw.text(((width - w) / 2, base_height), line, font=font)
    base_height += h + padding

img.save('test.png')
