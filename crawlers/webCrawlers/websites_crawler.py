import os
import time

from crawlers.urlCrawlers.websites_urls_crawler import SectorWebsiteManager
from crawlers.webCrawlers.website_data_manager import WebsiteDataManager
from crawlers.utils import html_utils, thread_pool
from crawlers.utils.progress_visualizer import ProgressVisualizer
from tools.loggers import ErrorLogger


def crawl_websites(website_data_manager, error_logger):
    my_thread_pool = thread_pool.ThreadPool(9)

    with open(SectorWebsiteManager.FILE_NAME, 'r') as f:
        sector_websites = f.readlines()

    progress_visualizer = iter(ProgressVisualizer(data=sector_websites))

    def next_progress():
        next(progress_visualizer)

    for sector_website in sector_websites:
        info = sector_website.split('\t')
        if len(info) != 2:
            error_logger.log(sector_website)
            next_progress()
            continue
        sector_id, url = info[0], info[1]

        def get_html_job(_sector_id, _url):
            html_text = html_utils.get_website_text(_url, fetch_related=True)
            if not html_text or len(html_text) < 50:
                error_logger.log(_url)
                return

            website_data_manager.append(
                sector_id=_sector_id,
                text_data=html_text,
                website_url=''.join(_url.split())
            )

        my_thread_pool.enqueue(job=get_html_job, call_back=next_progress, _sector_id=sector_id, _url=url)

    time.sleep(10)
    os.system('kill -9 {}'.format(os.getpid()))


if __name__ == '__main__':
    with WebsiteDataManager() as manager:
        with ErrorLogger() as err_logger:
            crawl_websites(website_data_manager=manager, error_logger=err_logger)
