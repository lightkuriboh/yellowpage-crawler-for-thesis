
from crawlers.urlCrawlers.websites_urls_crawler import SectorWebsiteManager

websites_to_remove = ['trangvang']

with open(SectorWebsiteManager.FILE_NAME, 'r') as f:
    all_lines = f.readlines()

new_lines = []
for line in all_lines:
    needs_to_be_removed = any([website in line for website in websites_to_remove])
    if not needs_to_be_removed:
        new_lines.append(line)

with open(''.join([SectorWebsiteManager.FILE_NAME, '_changed']), 'w') as f:
    f.writelines(new_lines)
