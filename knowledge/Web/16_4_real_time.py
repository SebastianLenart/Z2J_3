import mechanicalsoup
import time

browser = mechanicalsoup.Browser()
page = browser.get("http://olympus.realpython.org/dice")
tag = page.soup.select("#result")[0]
# print(page.soup.select("#result"))
# print(page.soup.select("#result")[0])
result = tag.text
print(f"The result of your dice roll is: {result}")
print("*" * 10)
for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")
    if i < 3:
        time.sleep(2)
# zbyt wiele zapytan moze wywalic serwer i moga nas znalezc po adresie IP, takze be careful