
class SectorWebsite:
    def __init__(self, sector_id, website):
        self.sector_id = sector_id
        self.website = website

    def __str__(self):
        return '{}\t{}\n'.format(self.sector_id, self.website)

    def __repr__(self):
        return self.__str__()


class SectorWebsiteManager:
    FILE_NAME = 'sector_website.txt'

    def __init__(self):
        self._sector_website = []

    def append(self, sector_id, website_url):
        self._sector_website.append(
            SectorWebsite(
                sector_id=sector_id,
                website=website_url)
        )

    def list_to_file(self):
        print(len(self._sector_website))
        with open(SectorWebsiteManager.FILE_NAME, 'w') as f:
            f.writelines([str(info) for info in self._sector_website])
