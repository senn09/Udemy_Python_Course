from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.title)

article_tag = [tag for tag in soup.select(".title .titleline a")][::2]

article_text = [tag.getText() for tag in article_tag]
article_link = [tag.get("href") for tag in article_tag]
article_score = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_text)
print(article_link)
print(article_score)

high_score = max(article_score)
high_score_index = article_score.index(high_score)

# print(article_text[high_score_index])
# print(article_link[high_score_index])
# print(article_score[high_score_index])
    
print(len(article_text))
print(len(article_link))
print(len(article_score))






# with open("./website.html", "r") as html_doc:
    
#     soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.title.string)

# company_url = soup.select_one("p a")
# print(company_url)