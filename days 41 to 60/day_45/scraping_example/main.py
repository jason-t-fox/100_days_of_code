import bs4
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = bs4.BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all("span", class_="titleline")

article_text = []
article_link = []

for article_tag in articles:
    article_text.append(article_tag.a.text)
    article_link.append(article_tag.a["href"])
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_upvote = max(article_upvotes)
largest_upvote_index = article_upvotes.index(largest_upvote)

print(f"""
    {article_text[largest_upvote_index + 1]}
    {article_link[largest_upvote_index + 1]}
    {article_upvotes[largest_upvote_index]}
    """)  # there is an article that doesn't have a score, this will eventually not work
