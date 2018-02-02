import pycurl


def download(url, filename):
    c = pycurl.Curl()
    c.setopt(c.URL, url)

    with open(filename, 'wb') as f:
        c.setopt(c.WRITEDATA, f)
        c.perform()
