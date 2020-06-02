from bs4 import BeautifulSoup
from typing import Callable
from atlassian import Confluence


class WikiBot(Confluence):

    def __init__(self, url, username, password):
        super().__init__(url=url, username=username, password=password)

    def modify_content_with_bs4(self, space: str, title: str, modification_callback: Callable):
        ret = self.get_page_by_title(space=space, title=title, expand='body.storage')
        previous_html = ret['body']['storage']['value']
        soup = BeautifulSoup(previous_html, "html.parser")
        modification_callback(soup)
        return self.update_page(page_id=ret['id'], title=ret['title'], body=str(soup))
