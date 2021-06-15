"""
Build a Python-based web crawler, which will recursively walk over the website and download all images from its pages and then convert it all into one single format. Which format? Pick it yourself, it might be jpg, png, etc. But make sure all the images from the website are converted to a single format.

You can use almost any python library.

Take into account that the website might also keep images in .svg format or ‘picture’ format and in that case, these images should also be converted single selected format (png or jpeg).

You can pick whatever small website you want to test your project code.

We’ll test it using a random website URL.

"""
import os

import img2pdf as img2pdf
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
from PIL import Image
import pyvips

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}
url = 'https://dou.ua/'


# Getting a list of links to all pictures from the page
def get_images_links():
    image_links_list = []

    resp = requests.get(url=url, headers=headers)
    http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(resp.content, from_encoding=encoding, features="html.parser")

    for link in soup.find_all('img'):
        link_start = link['src'].split('/')[0]
        if link_start == 'https:':
            image_links_list.append(link['src'])

    get_all_images(image_links_list)


def get_all_images(data):
    for img_url in data:
        save_image(get_name(img_url), get_image(img_url))


# Get image name
def get_name(url):
    name = url.split('/')[-1]
    return name


# Load images from site
def get_image(url):
    response = requests.get(url=url, headers=headers, stream=True)
    return response


# Write the image in blocks of 4096 kilobytes
def save_image(name, image_data):
    file = open(f'media/{name}', 'bw')
    for chunk in image_data.iter_content(4096):
        file.write(chunk)
    print(f'image {name} loaded')


# convert all images to .jpg inside a directory
def convert_to_jpg():
    count = 0
    for fname in os.listdir("media"):
        if not fname.endswith(".jpg") and not fname.endswith(".svg"):
            im = Image.open(f'media/{fname}')
            rgb_im = im.convert('RGB')
            rgb_im.save(f'media/{fname}.jpg')
            count += 1
    print(f'{count} images converted to .jpg')


# convert all .svg graphics to .jpg inside a directory
def convert_svg_to_jpg():
    count = 0
    for fname in os.listdir("media"):
        if fname.endswith(".svg"):
            image = pyvips.Image.new_from_file(f'media/{fname}', dpi=300)
            image.write_to_file(f'media/{fname}.jpg')
            count += 1
    print(f'{count} .svg converted to .jpg')


# save all .jpg to one .pdf file
def convert_to_pdf():
    dirname = "media"
    imgs = []
    counter = 0
    for fname in os.listdir(dirname):
        if not fname.endswith(".jpg"):
            continue
        path = os.path.join(dirname, fname)
        if os.path.isdir(path):
            continue
        imgs.append(path)
        counter += 1
    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(imgs))
    print(f'{counter} .jpg images save to result.pdf')


if __name__ == '__main__':
    get_images_links()
    convert_to_jpg()
    convert_svg_to_jpg()  # may not work in Windows operating system
    convert_to_pdf()
