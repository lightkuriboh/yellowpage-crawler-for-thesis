from industry_sectors.sector import Sector
from industry_sectors.sector_id import SectorId


class SectorManager:
    SECTORS_FILE = 'sectors_list_level_2.txt'
    SECTORS_HIERARCHY_FILE = 'sectors_hierarchy_level_2.txt'

    @classmethod
    def from_file(cls):
        instance = cls()
        with open(SectorManager.SECTORS_HIERARCHY_FILE, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line:
                    sectors = line.split()
                    for i in range(1, len(sectors)):
                        instance._parent[sectors[i]] = sectors[0]
                    if sectors[0] not in instance._parent:
                        instance._parent[sectors[0]] = sectors[0]
        return instance

    def get_parent(self, sector_id):
        return self._parent[sector_id] if sector_id in self._parent else None

    def __init__(self):
        self._sectors = []
        self.sector_id_manager = iter(SectorId())
        self._recent_main_sector = None
        self._parent = {}

    def set_recent_main_sector(self):
        self._recent_main_sector = self.get_most_recent_id()

    def get_recent_main_sector(self):
        return self._recent_main_sector

    def append(self, sector_name):
        next(self.sector_id_manager)
        self._sectors.append(
            Sector(
                sector_id=str(self.sector_id_manager),
                sector_name=sector_name)
        )

    def add_child(self, parent_id, sector_name):
        for sector in self._sectors:
            if sector.sector_id == parent_id:
                self.append(sector_name=sector_name)
                sector.add_child_sector(str(self.sector_id_manager))
                break

    def get_most_recent_id(self):
        return str(self.sector_id_manager)

    def list_to_file(self):
        with open(SectorManager.SECTORS_FILE, 'w') as f:
            f.writelines([str(sector) for sector in self._sectors])
        self.hierarchy_to_file()

    def hierarchy_to_file(self):
        with open(SectorManager.SECTORS_HIERARCHY_FILE, 'w') as f:
            f.writelines([sector.hierarchy_str() for sector in self._sectors])
