import scraping
import bot


def main():
    products = scraping.collect_products()
    print(f"[INFO] Всего {len(products)} товаров удалось собрать.")
    bot.post_to_telegram(products)


if __name__ == '__main__':
    main()
