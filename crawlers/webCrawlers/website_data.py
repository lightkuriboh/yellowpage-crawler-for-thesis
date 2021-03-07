
import string


class WebsiteData:
    CSV_SEPARATOR = ';'

    def __init__(self, sector_id, text_data, data_source):
        self.sector_id = WebsiteData.pre_process(sector_id)
        self.text_data = WebsiteData.pre_process(text_data)
        self.data_source = data_source

    def __str__(self):
        return '{}{}{}{}{}\n'.format(self.sector_id, WebsiteData.CSV_SEPARATOR,
                                     self.data_source, WebsiteData.CSV_SEPARATOR,
                                     self.text_data)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def pre_process(input_str):
        translator = str.maketrans('', '', string.punctuation)
        temp = ' '.join(input_str.replace(WebsiteData.CSV_SEPARATOR, '').split())
        return temp.translate(translator)
