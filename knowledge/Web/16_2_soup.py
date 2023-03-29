# pip3 install beautifulsoup4
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
"""
For example, BeautifulSoup objects have a .get_text() method that can
be used to extract all of the text from the document and remove any
HTML tags automatically.

"""
# print(soup.get_text())
print(soup.get_text().replace("\n", ""))
print(soup.find_all("img"))
print(soup.find_all("img", src="/static/dionysus.jpg"))
print(soup.title)
print(soup.title.string)
print("*"*10)
imagine1, imagine2 = soup.find_all("img") # lista obiektow
print(imagine1.name)
print(imagine1["src"])