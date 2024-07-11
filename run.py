import os
import shutil
import img2pdf
import requests
from PIL import Image

BASE_URL = '문자로 안내받은 수료앨범 링크주소'
ENDPOINT = 'assets/page-images/page-hashcode-hashcode'
FILENAME = '20XX 삼성 청년 SW 아카데미 N기 PHOTO ALBUM'
SAVE_DIR = os.path.join(os.getcwd(), 'downloads')
TEMP_DIR = os.path.join(os.getcwd(), 'temp')
END_PAGE = 300


def download_image(page):
    url = f'{BASE_URL}/{ENDPOINT}-{page:04d}.jpg'
    response = requests.get(url)
    response.raise_for_status()

    print(f'Downloading... {url}')
    filepath = os.path.join(SAVE_DIR, f'{page:04d}.jpg')
    with open(filepath, 'wb') as file:
        file.write(response.content)


def create_combined_image(page1, page2):
    print(f'Creating Combined Image... {page1:04d}.jpg, {page2:04d}.jpg')
    image1 = Image.open(os.path.join(SAVE_DIR, f'{page1:04d}.jpg'))
    image2 = Image.open(os.path.join(SAVE_DIR, f'{page2:04d}.jpg'))

    new_width = image1.width + image2.width
    new_height = max(image1.height, image2.height)

    new_image = Image.new('RGB', (new_width, new_height))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (image1.width, 0))
    new_image.save(os.path.join(TEMP_DIR, f'{page1:04d}.jpg'))


def create_album_images():
    print(f'Creating Album Images...')
    for page in range(1, END_PAGE + 1):
        if page == 1 or page == END_PAGE:
            src = os.path.join(SAVE_DIR, f'{page:04d}.jpg')
            dst = os.path.join(TEMP_DIR, f'{page:04d}.jpg')
            shutil.copy(src, dst)
        elif page % 2 == 0:
            create_combined_image(page, page + 1)


def create_album_pdf():
    print(f'Creating Album PDF...')
    files = os.listdir(TEMP_DIR)
    filepaths = [os.path.join(TEMP_DIR, file) for file in files]
    with open(f'{FILENAME}.pdf', 'wb') as file:
        file.write(img2pdf.convert(filepaths))
        shutil.rmtree(TEMP_DIR)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR, exist_ok=True)
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR, exist_ok=True)

    for page in range(1, END_PAGE + 1):
        filepath = os.path.join(SAVE_DIR, f'{page:04d}.jpg')
        if not os.path.exists(filepath):
            download_image(page)

    create_album_images()
    create_album_pdf()
