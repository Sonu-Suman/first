# Do google search using python code

try:
    from googlesearch import search
except ImportError:
    print("This module does not exist in the library")


# to search
query = "Sri-Krisna"

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)