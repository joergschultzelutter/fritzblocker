import requests
import re
from bs4 import BeautifulSoup


def get_tellows_data(phone_number: str):
    caller_name = caller_score = caller_city = caller_international_phone_number = None

    url = f"https://www.tellows.de/num/{phone_number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    details = soup.select_one("#details")
    contents = str(details.contents[1])
    matches = re.search(
        pattern=r"<b>Anrufername:<\/b>\n\s+(.*)<br\/>",
        string=contents,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    if matches:
        caller_name = matches[1].strip()
    contents = str(soup.select_one("div > div > div > section > div"))
    matches = re.search(
        pattern=r"<strong>Stadt: <\/strong>(.*)<br\/>",
        string=contents,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    if matches:
        caller_city = matches[1].strip()
    matches = re.search(
        pattern=r"data-bs-toggle=\"collapse\" href=\"#klappenIntNumber\" role=\"button\">(.*)<\/a>",
        string=contents,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    if matches:
        caller_international_phone_number = matches[1].strip()

    score = soup.select_one("#tellowsscore > div > a > img")
    score_nr = score.attrs["alt"].split(":")[-1].strip()
    caller_score = int(score_nr.split()[1])
    return caller_name, caller_score, caller_city, caller_international_phone_number


if __name__ == "__main__":
    pass
