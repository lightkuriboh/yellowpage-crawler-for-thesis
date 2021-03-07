
class UrlSector:
    def __init__(self, sector_id, url):
        self.sector_id = sector_id
        self.url = url

    def __repr__(self):
        return '{}\t{}\n'.format(self.sector_id, self.url)

    def __str__(self):
        return self.__repr__()


class UrlSectorManager:
    FILE_NAME = 'sector_urls.txt'

    def __init__(self):
        self._url_sectors = []

    def append(self, sector_id, url):
        self._url_sectors.append(
            UrlSector(
                sector_id=sector_id,
                url=url)
        )

    def list_to_file(self):
        with open(UrlSectorManager.FILE_NAME, 'w') as f:
            f.writelines([str(url_sector) for url_sector in self._url_sectors])
