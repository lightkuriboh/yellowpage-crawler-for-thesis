
class Sector:
    def __init__(self, sector_id, sector_name):
        self.sector_id = sector_id
        self.sector_name = sector_name
        self._children_sectors = []

    def __getitem__(self, item):
        return self._children_sectors[item]

    def __len__(self):
        return len(self._children_sectors)

    def __repr__(self):
        return '{}\t{}\n'.format(str(self.sector_id), self.sector_name)

    def __str__(self):
        return self.__repr__()

    def add_child_sector(self, sector_id):
        self._children_sectors.append(sector_id)

    def hierarchy_str(self):
        return '{} {}{}'.format(self.sector_id, ' '.join(self._children_sectors), '\n')
