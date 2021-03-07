import requests


def get_raw_html(url):
    url = remove_trailing_new_lines(url)
    try:
        resp = requests.get(url, timeout=3)
        resp.encoding = resp.apparent_encoding
        return resp.text
    except Exception as e:
        # print('Error in url: {}'.format(url))
        return ''


def remove_trailing_new_lines(input_url):
    while len(input_url) > 1 and (input_url[-1] == '\n' or input_url[-1] == '\t'):
        input_url = input_url[:-1]
    return input_url
