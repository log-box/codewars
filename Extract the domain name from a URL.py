# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For
# example:
#
# domain_name("http://git-hub.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"
# (domain_name("http://google.com"), "google")
# (domain_name("http://google.co.jp"), "google")
# (domain_name("www.xakep.ru"), "xakep")
# (domain_name("https://youtube.com"), "youtube")


import re


# def domain_name(url):
#     result = re.findall(r'(http)?(https)?(://)?(www)?([a-zA-Z0-9-]+)\.', url)
#     for i in result:
#         for j in i:
#             if j != '' and j != 'www' and j != 'http' and j != 'https' and j != '://':
#                 return j
#     return None

def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("www.xakep.ru"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))
print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("https://youtube.com"))
print(domain_name("https://123.com"))
print(domain_name("hyphen-site.ru"))