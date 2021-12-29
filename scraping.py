from bs4 import BeautifulSoup
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
}


def collect_products(url="https://rozetka.com.ua/ua/utsenennye-noutbuki/c83853/sort=novelty/"):
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    page_count = int(soup.find('div', class_="pagination ng-star-inserted").find_all(
        'li', class_="pagination__item ng-star-inserted")[-1].text.strip())
    print(f"[INFO] Всего страниц: {page_count}...")
    products = ()
    for page in range(1, page_count + 1):
        print(f"[INFO] Обработка {page} страницы...")
        url = f"https://rozetka.com.ua/ua/utsenennye-noutbuki/c83853/page={page};sort=novelty/"
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find_all(
            'li', class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
        for item in items:
            title = item.find(
                'a', class_="goods-tile__heading ng-star-inserted").text.strip()
            link = item.find(
                'a', class_="goods-tile__heading ng-star-inserted").get('href').strip()
            try:
                price = item.find(
                    'div', class_="goods-tile__prices").find('p', class_="ng-star-inserted").text.strip()
            except:
                price = "нету"
            status = item.find(
                'div', class_="goods-tile__availability").text.strip()
            defect = item.find('div', class_="goods-tile__hidden-holder").find(
                'p', class_="goods-tile__description goods-tile__description_type_text ng-star-inserted").text.strip()
            products += ({
                "title": title,
                "link": link,
                "price": price,
                "status": status,
                "defect": defect
            },)
    return products
