# pip3 install MechanicalSoup

import mechanicalsoup
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
page = browser.get(url)
print(page.soup)
# login: zeus
# passowrd: ThunderDude
print("*"*10)
# wypelnianie formularzy i wysylanie tego - submit
#1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup
# 2
form = login_html.select("form")[0]
# print(form)
# print(login_html.select("form"))
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"
# 3
profiles_page = browser.submit(form, login_page.url) # link
print(profiles_page.url) # link
print("*"*10)
links = profiles_page.soup.select("a")

for link in links:
    print(link)
    address = link["href"]
    text = link.text
    print(f"{text}: {address}")

















