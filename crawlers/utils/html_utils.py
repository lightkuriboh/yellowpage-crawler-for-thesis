
from bs4 import BeautifulSoup

from crawlers.utils import request_utils


class HTMLParser:
    def __init__(self, html_doc):
        self.soup = BeautifulSoup(html_doc, 'html5lib')

    def get_all_tag_with(self, tag_name, contained_substring=None, criteria=None):
        if criteria is None:
            criteria = {}
        tags = self.soup.find_all(tag_name, attrs=criteria)
        return tags if contained_substring is None \
            else [tag for tag in tags if contained_substring in str(tag)]

    def get_all_raw_text(self):
        self._remove_scripts()
        return self.soup.get_text(separator=' ')

    def _remove_scripts(self):
        for script in self.soup(["script", "style"]):
            script.extract()

    def get_related_websites(self, origin_domain):
        origin_domain = request_utils.remove_trailing_new_lines(origin_domain)
        related_pages = self.get_all_tag_with('a', contained_substring=origin_domain)

        websites_set = []

        if not related_pages:
            return {}

        for page in related_pages:
            url = page.get('href')
            related_url = ''

            slash_counter = 0
            if not url:
                continue
            for character in url:
                if character == '/':
                    slash_counter += 1
                related_url += character

                if slash_counter == 4:
                    break
            if related_url != origin_domain and related_url != origin_domain + '/'\
                    and len(related_url) > 4 and origin_domain in related_url:
                websites_set.append(related_url)

        websites_set = set(websites_set)
        while len(websites_set) > 4:
            websites_set.pop()
        return websites_set

    @staticmethod
    def get_attr_in_tag(attr, tags_list):
        return [str(tag.get(attr)) for tag in tags_list]

    @staticmethod
    def get_children_tag(child_tag, tags_list):
        return [tag.find(child_tag) for tag in tags_list]


def get_website_text(url, fetch_related=False):
    raw_html = request_utils.get_raw_html(url=url)
    if not raw_html:
        return ''
    html_parser = HTMLParser(
        html_doc=raw_html
    )
    html_text = html_parser.get_all_raw_text()

    if fetch_related:
        for related_website in html_parser.get_related_websites(url):
            html_text += get_website_text(related_website)
    return html_text
