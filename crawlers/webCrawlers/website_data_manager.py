import threading
from crawlers.webCrawlers.website_data import WebsiteData


data_list_lock = threading.Lock()


class WebsiteDataManager:
    FILE_NAME = 'data_level_1.csv'
    SECOND_FILE_NAME = 'data_level_2.csv'
    BUFFER_SIZE = 10

    def __init__(self, switch_file=False):
        self._website_data = []
        if switch_file:
            self.file_name = WebsiteDataManager.SECOND_FILE_NAME
        else:
            self.file_name = WebsiteDataManager.FILE_NAME

        with open(self.file_name, 'w') as f:
            f.write('{}{}{}{}{}\n'.format('sector_id', WebsiteData.CSV_SEPARATOR,
                                          'website', WebsiteData.CSV_SEPARATOR,
                                          'text'))

    def __enter__(self):
        return self

    def append(self, sector_id, text_data, website_url):
        with data_list_lock:
            self._website_data.append(
                WebsiteData(
                    sector_id=sector_id,
                    text_data=text_data,
                    data_source=website_url
                )
            )
            if len(self._website_data) >= WebsiteDataManager.BUFFER_SIZE:
                self.flush()

    def flush(self):
        with open(self.file_name, 'a') as f:
            f.writelines([str(website_data) for website_data in self._website_data])
        self._website_data.clear()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()
