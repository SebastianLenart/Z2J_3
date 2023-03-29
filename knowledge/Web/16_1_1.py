from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/aphrodite"
html_page = urlopen(url)
print("return", html_page)
html_text = html_page.read().decode("utf-8")
print(html_text)

html_page = urlopen(url) # to musi byc
html = html_page.read().decode('utf-8')
start_tag = "<title>"
end_tag = "</title>"
start_index = html.find(start_tag) + len(start_tag)
end_index = html.find(end_tag)
print(html[start_index:end_index])

"""
Our regular expression, ab*c, matches any part of the string that begins
with an “a,” ends with a “c,” and has zero or more of “b” in between
the two

"""
print(re.findall("ab*c", "ac"))
print(re.findall("ab*c", "abcd"))
print(re.findall("ab*c", "ABC", re.IGNORECASE))
print(re.findall("ab*c", "abcac"))
print(re.findall("ab*c", "abdc"))
print("*"*10)

"""
For instance, we could find all the strings that contain the
letters “a” and “c” separated by a single character as follows:

>>> re.findall("a.c", "abc")
['abc']
>>> re.findall("a.c", "abbc")
[]
>>> re.findall("a.c", "ac")
[]
>>> re.findall("a.c", "acc")
['acc']


"""
# ----------------------------------------------------------------------
"""
For instance, "a.*c" can be used
to find every substring that starts with "a" and ends with "c", regardless
of which letter—or letters—are in-between:

>>> re.findall("a.*c", "abc")
['abc']
>>> re.findall("a.*c", "abbc")
['abbc']
>>> re.findall("a.*c", "ac")
['ac']
>>> re.findall("a.*c", "acc")
['acc']

"""

# match
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
print(match_results.group())
print("*"*10)

#substitute / replace
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string) # OR
# string = re.sub("<.*?>", "ELEPHANTS", string)
print(string)
"""
The re.sub() function uses the regular expression "<.*>" to find and
replace everything in between the first < and last >, which is most of
the string.
"""
















