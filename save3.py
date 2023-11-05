
import openpyxl
from PIL import Image
x=0
workbook = openpyxl.Workbook()
sheet = workbook.active
while x!= 383:
    x += 1




    webp_image = Image.open(f'all_cards\\{x}.png')


    new_size = (60, 18)
    webp_image = webp_image.resize(new_size)


    webp_image.save(f'all_cards\\{x}.png', 'PNG')


    sheet.add_image(openpyxl.drawing.image.Image(f'all_cards\\{x}.png'), f'D{x}')


    workbook.save('cards5.xlsx')

# Закрываем книгу
workbook.close()