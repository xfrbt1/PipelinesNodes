def bbc_news_parser(soup, **kwargs):
    text_and_links = soup.find_all("a", {"class": "media__link"})
    print("FROM BBC: ", text_and_links, "\n\n\n")
    final_data = [[block.text.strip(), block.get("href")] for block in text_and_links]
    print("FROM BBC: ", final_data, "\n\n\n")
    dict_content = {
        i[0]: i[1] if kwargs.get("url") in i[1] else f"{kwargs.get('url')}{i[1]}"
        for i in final_data
    }
    print("FROM BBC: ", dict_content, "\n\n\n")
    final_data = [[k, v] for k, v in dict_content.items()]
    print("FROM BBC: ", final_data, "\n\n\n")
    return final_data


def habr_news_parser(soup, **kwargs):
    titles = soup.find_all("a", class_="tm-title__link")
    final_data = [
        [block.text, f'https://habr.com{block.get("href")}'] for block in titles
    ]
    return final_data


def chess_news_parser(soup, **kwargs):
    titles = soup.find_all("a", class_="post-preview-title")
    final_data = [[block.text.strip(), block.get("href")] for block in titles]
    return final_data


def onliner_news_parser(soup, **kwargs):
    titles = soup.find_all("div", class_="b-main-navigation__dropdown-news-description")
    final_data = [[block.text.strip(), block.find("a").get("href")] for block in titles]
    return final_data
