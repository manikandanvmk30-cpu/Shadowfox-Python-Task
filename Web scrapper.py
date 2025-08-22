import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.codecademy.com/articles/language/python"

def fetch_webpage(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_articles(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = []
    article_tags = soup.find_all("article")
    
    for tag in article_tags:
        title = tag.find("h2").text.strip() if tag.find("h2") else "No Title"
        date = tag.find("time").text.strip() if tag.find("time") else "No Date"
        summary = tag.find("p").text.strip() if tag.find("p") else "No Summary"
        articles.append({
            "title": title,
            "date": date,
            "summary": summary
        })
    return articles

def save_to_csv(data, filename="shadowfox_articles.csv"):
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "date", "summary"])
            writer.writeheader()
            writer.writerows(data)
        print(f"Saved {len(data)} articles to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")

html = fetch_webpage(url)
if html:
    extracted_articles = parse_articles(html)
    if extracted_articles:
        save_to_csv(extracted_articles)
    else:
        print("No articles found.")
