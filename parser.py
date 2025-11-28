import json
from bs4 import BeautifulSoup

INPUT_FILE = "cases.html"
OUTPUT_FILE = "cases_data.json"


def parse_vk_cases():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        content = file.read()
    soup = BeautifulSoup(content, "html.parser")
    cases_data = []
    cards = soup.find_all("a", class_=lambda x: x and "case-card_wrapper" in x)

    for card in cards:
        title = card.find(
            "div", class_=lambda x: x and "case-card_title" in x
        ).get_text(strip=True)

        raw_link = card.get("href")

        time_tag = card.find("time", itemprop="datePublished")

        published_date = None
        if time_tag and time_tag.has_attr("datetime"):
            published_date = time_tag["datetime"]
        elif time_tag:
            text_date = time_tag.get_text(strip=True)
            day, month, year = text_date.split(".")
            published_date = f"{year}-{month}-{day}"

        case_item = {"title": title, "url": raw_link, "date": published_date}

        cases_data.append(case_item)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(cases_data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    parse_vk_cases()
