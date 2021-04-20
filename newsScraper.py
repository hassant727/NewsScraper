import nltk
from newspaper import Article
import pandas as pd

nltk.download('punkt')

articles = pd.DataFrame()

def news_articles(website):
    news_article = Article(website)
    news_article.download()
    news_article.parse()
    news_article.nlp()
    article = pd.DataFrame(columns=['news_article.title', 'news_article.publish_date', 'news_article.keywords','news_article.summary'])
    return article.to_csv("test123.csv", mode='a', header=True)


news_articles("https://finance.yahoo.com/news/why-oakmark-funds-eliminated-aptiv-173341247.html")

articles.head()

news_articles("https://www.marketwatch.com/story/aptiv-plc-stock-falls-friday-underperforms-market-01618605458-8e96b9a50657")

result = pd.read_csv("test123.csv")
result.head()

def func():
    articles = ["https://finance.yahoo.com/news/why-oakmark-funds-eliminated-aptiv-173341247.html", "https://www.marketwatch.com/story/aptiv-plc-stock-falls-friday-underperforms-market-01618605458-8e96b9a50657"]
    df = pd.DataFrame()
    for article in articles:
        x = pd.DataFrame(columns=['news_article.title', 'news_article.publish_date', 'news_article.keywords','news_article.summary'])
        

        