from bs4 import BeautifulSoup
from wikibot import WikiBot


def modification_callback(soup):
    a = soup.find('table').find_all_next('tr')[6].find_all_next('td')[6].div
    a.append(BeautifulSoup('<b>WikiBot is awesome!</b>', 'html.parser'))


wiki_bot = WikiBot(url='https://localhost', username='WikiBot', password='*******')

wiki_bot.modify_content_with_bs4(space='My Space', title='Demo', modification_callback=modification_callback)
