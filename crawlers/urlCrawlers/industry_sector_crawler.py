
from crawlers.utils import request_utils, html_utils
from industry_sectors.sectors_manager import SectorManager
from crawlers.urlCrawlers.url_sector_manager import UrlSectorManager


N_SECTOR_PAGES = 27
SECTOR_URL = 'https://www.yellowpages.vn/cate.asp?page={}'
MAIN_SECTOR_DENOTE = 'https://www.yellowpages.vn/images/red_dot.png'
SUB_SECTOR_DENOTE = 'https://www.yellowpages.vn/images/black_dot.png'


def is_main_sector(str_html_tag):
    return MAIN_SECTOR_DENOTE in str_html_tag


def is_sub_sector(str_html_tag):
    return not is_main_sector(str_html_tag)


def fetch_sectors_pages(sector_manager, url_sector_manager):
    for page in range(1, N_SECTOR_PAGES + 1):
        current_sector_page_url = SECTOR_URL.format(page)
        print(current_sector_page_url)
        html_parser = html_utils.HTMLParser(
            request_utils.get_raw_html(
                url=current_sector_page_url
            )
        )
        tags = html_parser.get_all_tag_with('li')
        for tag in tags:
            if not tag.find('a'):
                continue
            sector_title = tag.find('a').get_text()
            sector_href = tag.find('a').get('href')
            if is_main_sector(str(tag)):
                sector_manager.append(sector_title)
                sector_manager.set_recent_main_sector()
            else:
                sector_manager.add_child(sector_manager.get_recent_main_sector(), sector_title)
                url_sector_manager.append(
                    sector_id=sector_manager.get_most_recent_id(),
                    url=sector_href
                )
                # print(sector_title, sector_href)


def crawl_sectors():
    sector_manager = SectorManager()
    url_sector_manager = UrlSectorManager()
    fetch_sectors_pages(
        sector_manager=sector_manager,
        url_sector_manager=url_sector_manager
    )

    sector_manager.list_to_file()
    url_sector_manager.list_to_file()


if __name__ == '__main__':
    crawl_sectors()
