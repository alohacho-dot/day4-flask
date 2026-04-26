import sys
import requests
from bs4 import BeautifulSoup

GOOGLE_NEWS_KO_RSS = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"
YONHAP_RSS = "https://www.yna.co.kr/rss/all.xml"


def clean_html_text(html_text: str) -> str:
    if not html_text:
        return "(요약 없음)"
    text = BeautifulSoup(html_text, "html.parser").get_text(" ", strip=True)
    return text or "(요약 없음)"


def parse_rss_items(xml_text: str, limit: int = 10):
    soup = BeautifulSoup(xml_text, "xml")
    items = soup.find_all("item")[:limit]

    parsed = []
    for item in items:
        title = item.find("title")
        description = item.find("description")
        link = item.find("link")
        pub_date = item.find("pubDate") or item.find("published")

        parsed.append(
            {
                "title": title.get_text(strip=True) if title else "(제목 없음)",
                "summary": clean_html_text(description.get_text()) if description else "(요약 없음)",
                "link": link.get_text(strip=True) if link else "(링크 없음)",
                "published_at": pub_date.get_text(strip=True) if pub_date else "(발행시간 없음)",
            }
        )

    return parsed


def fetch_rss(url: str):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


def print_items(items):
    if not items:
        print("가져온 뉴스가 없습니다.")
        return

    print(f"총 {len(items)}건\n")
    for i, item in enumerate(items, start=1):
        print(f"[{i}] {item['title']}")
        print(f"- 요약: {item['summary']}")
        print(f"- 링크: {item['link']}")
        print(f"- 발행시간: {item['published_at']}")
        print("-" * 80)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    feed_url = GOOGLE_NEWS_KO_RSS

    try:
        xml_text = fetch_rss(feed_url)
        items = parse_rss_items(xml_text, limit=10)
        print_items(items)
    except requests.RequestException as e:
        print(f"RSS 요청 실패: {e}")


if __name__ == "__main__":
    main()
