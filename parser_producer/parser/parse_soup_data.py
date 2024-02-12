def bbc_news_parser(soup, n: int = 5, **kwargs):
    text_and_links = soup.find_all("a", {"class": "media__link"})
    final_data = [
        [block.text.strip(), block.get("href")] for block in text_and_links[:n]
    ]
    dict_content = {
        i[0]: i[1] if kwargs.get("url") in i[1] else f"{kwargs.get('url')}{i[1]}"
        for i in final_data
    }
    dict_load = [{"title": k, "url": v} for k, v in dict_content.items()]
    return {"BBC NEWS": dict_load}


def habr_news_parser(soup, n: int = 5, **kwargs):
    titles = soup.find_all("a", class_="tm-title__link")
    final_data = [[block.text, block.get("href")] for block in titles]
    dict_load = [
        {"title": block[0], "url": f"https://habr.com{block[1]}"}
        for block in final_data[:n]
    ]
    return {"HABR NEWS": dict_load}


def chess_news_parser(soup, n: int = 5, **kwargs):
    titles = soup.find_all("a", class_="post-preview-title")
    final_data = [[block.text.strip(), block.get("href")] for block in titles]
    dict_load = [{"title": block[0], "url": block[1]} for block in final_data[:n]]
    return {"CHESS NEWS": dict_load}


def onliner_news_parser(soup, n: int = 5, **kwargs):
    titles = soup.find_all("div", class_="b-main-navigation__dropdown-news-description")
    final_data = [[block.text.strip(), block.find("a").get("href")] for block in titles]
    dict_load = [{"title": block[0], "url": block[1]} for block in final_data[:n]]
    return {"ONLINER NEWS": dict_load}
