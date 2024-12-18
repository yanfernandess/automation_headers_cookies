import requests
from colorama import Fore, Back, Style

requests.packages.urllib3.\
disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
def format_text(title, item):
    cr = '\r\n'
    section_break = cr
    item = str(item)
    text = Style.BRIGHT + Fore.RED + title + Fore.RESET + section_break + item + section_break
    return text
    
def format_headers(headers):
    return "\n".join([f"{Fore.GREEN}{key}{Fore.RESET}: {value}" for key, value in headers.items()])

def format_cookies(cookies):
    return "\n".join([f"{Fore.GREEN}{cookie.name}{Fore.RESET}: {cookie.value}" for cookie in cookies])
    
url = input('URL: ')

r = requests.get(url, verify=False)
print(format_text('r.status_code is: ', r.status_code))
print(format_text('r.headers is: ', format_headers(r.headers)))
print(format_text('r.cookies is: ', format_cookies(r.cookies)))
print(format_text('r.json is: ', r.json))
