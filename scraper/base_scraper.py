import requests
from bs4 import BeautifulSoup

def scrape_website(url: str, max_text_len=5000) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    text = soup.get_text(separator="\n", strip=True)
    images = [img['src'] for img in soup.find_all('img') if img.get('src')]

    text = text[:max_text_len] if len(text) > max_text_len else text
    image_text = "\n".join(images[:5])

    return f"{text}\n\nImages:\n{image_text}"
