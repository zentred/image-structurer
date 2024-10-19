import os, math
from PIL import Image

max_images_per_line = 8

def sort_images():

    def sort_key(n):
        return int(n.split('_')[1].split('.')[0])

    for a, b, c in os.walk('./images'):
        #c.sort(key=sort_key) only needed if your file names contain numbers and are sorted by the numbers
        return c

images = [Image.open(f'images/{filename}') for filename in sort_images()]
image_batches = [
    images[max_images_per_line*i : max_images_per_line*(i+1)]
    for i in range(math.ceil(len(images)/max_images_per_line))
]

total_height, max_width, new_images = 0, 0, []
for image_list in image_batches:
    widths, heights = zip(*(i.size for i in image_list))

    total_width = sum(widths)
    max_height = max(heights)
    total_height += max_height
    if total_width > max_width:
        max_width = total_width

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in image_list:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_images.append(new_im)

final_image = Image.new('RGB', (max_width, total_height))

y_offset = 0
for new_im in new_images:
    final_image.paste(new_im, (0, y_offset))
    y_offset += new_im.height

final_image.save('output.jpg')
