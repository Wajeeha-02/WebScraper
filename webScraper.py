from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'WebScraper'
sheet.append(['Index', 'Model', 'Price'])

try:
    source = requests.get('https://www.whatmobile.com.pk/')
    # crash if website not reachable
    source.raise_for_status()

    # .text to access the HTML text
    soup = BeautifulSoup(source.text, 'html.parser')
    mobiles = soup.find('div', id="container").find_all('li', class_="product")

    for count, mobile in enumerate(mobiles, 1):
        model = mobile.find('h4', class_="p4").a.get_text(
            separator=' ').strip()
        price = mobile.span.text
        sheet.append([count, model, price])

except Exception as e:
    print(e)


excel.save('Web Scraper.xlsx')
