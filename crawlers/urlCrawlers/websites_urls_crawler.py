
from crawlers.utils import html_utils, request_utils
from crawlers.utils.progress_visualizer import ProgressVisualizer
from crawlers.urlCrawlers.sectors_websites_manager import SectorWebsiteManager
from crawlers.urlCrawlers.industry_sector_crawler import UrlSectorManager


WEBSITE_ORIGIN = 'yellowpages'
WEBSITE_ALTERNATIVE = 'sachtrangvang'


def fetch_sector_urls(sector_website_manager):
    with open(UrlSectorManager.FILE_NAME, 'r') as f:
        all_sector_urls = f.readlines()

    progress_visualizer = iter(ProgressVisualizer(data=all_sector_urls))

    for sector_url in all_sector_urls:
        sector_id, sector_url = sector_url.split('\t')

        next(progress_visualizer)

        raw_html = request_utils.get_raw_html(url=sector_url)
        html_parser = html_utils.HTMLParser(raw_html)
        website_a_tags = html_parser.get_all_tag_with('a', criteria={
            'target': '_blank',
            'rel': 'nofollow'
        })
        website_a_tags = [website_a_tag for website_a_tag in website_a_tags
                          if WEBSITE_ORIGIN not in str(website_a_tag)
                          and WEBSITE_ALTERNATIVE not in str(website_a_tag)]
        for website_a_tag in website_a_tags:
            website_url = website_a_tag.get('href')
            sector_website_manager.append(sector_id=sector_id,
                                          website_url=website_url)


def crawl_urls():
    sector_website_manager = SectorWebsiteManager()
    fetch_sector_urls(sector_website_manager=sector_website_manager)
    sector_website_manager.list_to_file()


if __name__ == '__main__':
    crawl_urls()
