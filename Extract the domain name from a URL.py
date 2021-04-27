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


def domain_name(url):
    result = re.findall(r'^[wWHhTtPpSs:/.]+([a-z0-9A-Z-]+)', url)
    # result = re.findall(r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*", url)
    # re.match(result, "hyphen-site.ru")
    return result[0]

print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))
print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("https://youtube.com"))
print(domain_name("https://123.com"))
print(domain_name("hyphen-site.ru"))