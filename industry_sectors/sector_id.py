
class SectorId:
    INITIAL_ID = 0

    def __init__(self, sector_id=-1):
        self.sector_id = SectorId.INITIAL_ID if sector_id == -1 else sector_id

    def __iter__(self):
        return self

    def __next__(self):
        self._next_sector_id()
        return self.sector_id

    def __str__(self):
        return str(self.sector_id)

    def __eq__(self, other):
        return self.sector_id == other.sector_id

    def _next_sector_id(self):
        self.sector_id += 1
