from industry_sectors.sectors_manager import SectorManager, Sector
from crawlers.webCrawlers.website_data_manager import WebsiteDataManager
from crawlers.webCrawlers.website_data import WebsiteData
from crawlers.utils.progress_visualizer import ProgressVisualizer


sector_manager = SectorManager.from_file()


def list_main_sectors():
    with open(SectorManager.SECTORS_FILE, 'r') as sector_list_file:
        sector_lines = sector_list_file.readlines()
        sector_names = {}
        for sector_line in sector_lines:
            print(sector_line)
            sector_id, sector_name = sector_line.split('\t')
            while sector_name and sector_name[-1] == '\n':
                sector_name = sector_name[:-1]
            sector_names[sector_id] = sector_name

    with open(WebsiteDataManager.FILE_NAME, 'r') as f:
        with open('main_sectors_level_2.txt', 'w') as main_sectors_files:
            written = set()
            lines = f.readlines()
            progress_visualizer = iter(ProgressVisualizer(lines))
            first_line = True
            for line in lines:
                if first_line:
                    first_line = False
                    continue
                line = str(line)
                sector_id, data_source, text_data = line.split(WebsiteData.CSV_SEPARATOR)
                sector_id = sector_manager.get_parent(str(sector_id))
                if sector_id not in written:
                    main_sectors_files.write(str(Sector(sector_id=sector_id, sector_name=sector_names[sector_id])))
                    written.add(sector_id)
                next(progress_visualizer)


def level_up_data():
    with WebsiteDataManager(switch_file=True) as website_data_manager:
        with open(WebsiteDataManager.FILE_NAME, 'r') as f:
            lines = f.readlines()
            progress_visualizer = iter(ProgressVisualizer(lines))
            first_line = True
            for line in lines:
                if first_line:
                    first_line = False
                    continue
                line = str(line)
                sector_id, data_source, text_data = line.split(WebsiteData.CSV_SEPARATOR)
                sector_id = sector_manager.get_parent(str(sector_id))
                website_data_manager.append(sector_id, text_data, data_source)
                next(progress_visualizer)


# level_up_data()
# list_main_sectors()
