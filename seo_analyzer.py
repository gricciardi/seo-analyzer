import requests
from bs4 import BeautifulSoup
import sys

def analyze_seo(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Error fetching URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.string.strip() if soup.title else "Not found"
    description = soup.find("meta", attrs={"name": "description"})
    h1 = soup.find("h1")
    robots = soup.find("meta", attrs={"name": "robots"})

    text = soup.get_text(separator=' ', strip=True)
    word_count = len(text.split())
    images = soup.find_all("img")

    print(f"✅ URL: {url}")
    print(f"🔤 Title: {title}")
    print(f"📄 Meta Description: {description['content'].strip() if description and description.get('content') else 'Not found'}")
    print(f"🏷️ H1: {h1.text.strip() if h1 else 'Not found'}")
    print(f"📝 Word Count: {word_count}")
    print(f"🖼️ Images: {len(images)}")
    print(f"🤖 Robots Meta Tag: {'Present' if robots else 'Missing'}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python seo_analyzer.py https://example.com")
    else:
        analyze_seo(sys.argv[1])
