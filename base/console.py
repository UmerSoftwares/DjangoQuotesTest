import requests
from selenium.webdriver import Chrome
from quotes.models import Quote


def init():
    browser = Chrome()
    browser.get("http://quotes.toscrape.com/page/2/")
    quotes = browser.find_elements_by_class_name("quote")
    for quote in quotes:
        text = quote.find_element_by_class_name('text')
        author = quote.find_element_by_class_name('author')
        Quote.objects.create(text=text.text, author=author.text)
