from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def turn_images_to_url():
    html = urlopen('https://www.uhd.edu/Pages/home.aspx')
    bs = BeautifulSoup(html, 'html.parser')
    images = bs.find_all('img', {'src': re.compile('jpg')})

    # Add links to text file
    f = open('urls.txt', "w")

    for image in images:
        print(image['src']+'\n')  # print to terminal
        f.write(image['src']+'\n')  # write to text file

    f.close()
    print('Done!')


turn_images_to_url()


# This script will scan sites and output image urls in text file/terminal
