from bs4 import BeautifulSoup
from requests import get
from openpyxl import Workbook

'''
Данный парсер вытаскивает информацию по интересовавшей меня на тот момент поисковой выдаче с Авито, и сохраняет результат в Exel файл.
'''

wb = Workbook()
ws = wb.active

url = 'https://www.avito.ru/sankt-peterburg/kvartiry/sdam/na_dlitelnyy_srok/do-30-tis-rubley-ASgBAgECAkSSA8gQ8AeQUgFFxpoMFXsiZnJvbSI6MCwidG8iOjMwMDAwfQ?cd=1&f=ASgBAQECAkSSA8gQ8AeQUgJAzAgUjlnm8A4U8qXjAgFFxpoMFXsiZnJvbSI6MCwidG8iOjMwMDAwfQ&user=1'
print(url)

response = get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

blocks = soup.find('div', class_='items-items-kAJAg').find_all('div',
                                                               class_="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum")



for b in blocks:
    ws.append({
        'A': b.find('a', {'class': 'styles-module-root-QmppR styles-module-root_noVisited-aFA10'}).get_text(
            strip=True).replace('\xa0', ''),
        'B': b.find('span', {'class': 'price-root-RA1pj'}).get_text(strip=True).replace('\xa0', ''),
        # 'Adress': b.find('span', {'class': "geo-root-zPwRk"}).get_text(strip=True).replace('\xa0', ''),
        'C': 'https://www.avito.ru/' + b.find('div', class_='iva-item-title-py3i_').find('a').get('href')
    })


wb.save('Avito.xlsx')
