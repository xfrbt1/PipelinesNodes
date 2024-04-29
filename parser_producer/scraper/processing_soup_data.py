def habr_news_scraper(soup, **kwargs):
    titles = soup.find_all("a", class_="tm-title__link")
    final_data = [
        [block.text, f'https://habr.com{block.get("href")}'] for block in titles
    ]
    return final_data


def chess_news_scraper(soup, **kwargs):
    titles = soup.find_all("a", class_="post-preview-title")
    final_data = [[block.text.strip(), block.get("href")] for block in titles]
    return final_data


def onliner_news_scraper(soup, **kwargs):
    titles = soup.find_all("div", class_="b-main-navigation__dropdown-news-description")
    final_data = [[block.text.strip(), block.find("a").get("href")] for block in titles]
    return final_data
