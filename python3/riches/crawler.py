import re
import urllib.request
import collections
import time
from textblob import TextBlob

class News:
    def __init__(self, link, source, title, time, sentiment) -> None:
        self.link = link
        self.source = source
        self.title = title
        self.time = time
        self.sentiment = sentiment

    def __str__(self) -> str:
        return f"{self.source}\t{self.time}\t{self.title}\t{self.link}\t{self.sentiment}\n"

if __name__ == '__main__':


    print("Please input key words: ", end='')
    key_words = input().strip().replace(" ", "+")
    print("Please input result number limit: ", end='')
    limit = int(input().strip())
    if limit % 100 != 0:
        limit = limit // 100 + 1
    else:
        limit = limit // 100
    print("Alright, let's go")

    url = f"https://www.google.com/search?safe=strict&tbs=sbd%3A1&qdr:m&tbm=nws&q={key_words}&hl=en&lr=lang_en&num=100&strip=1"
    # url = 'https://www.google.com/search?safe=strict&tbs=sbd%3A1&qdr:m&tbm=nws&q=Coronavirus+China&hl=en&lr=lang_en&num=100&strip=1'
    headers = {
        'Host': 'www.google.com',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    news_list = []
    i = 0
    print("Wait", end="")
    while i < limit:
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        raw = response.read().decode('utf-8')
        raw_list = raw.split('<div class="bkWMgd">')[1:]
        for r in raw_list:
            link = re.search('href="([^"]+?)"', r).group(1)
            s = re.search('</g-img>([^<]+?)</div><div class="phYMDf nDgy9d" style="-webkit-line-clamp:2">([^<]+?)</div>', r)
            try:
                source = s.group(1)
            except AttributeError as e:
                source = ""
            try:
                title = s.group(2)
            except AttributeError as e:
                title = ""
            news_list.append(News(link, source, title, "", None))

        url = f"https://www.google.com/search?safe=strict&tbs=sbd%3A1&qdr:m&tbm=nws&q=Coronavirus+China&oq=Coronavirus+China&hl=en&lr=lang_en&num=100&strip=1&start={i*100}"
        i += 1
        print("..", end="")

    print(f"\nObtained {len(news_list)} records on Google News.")
    print("Now start further processing...")
    man_links_title = []
    man_links_time = []
    man_links_both = []
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': "Mozilla/5.0",
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    for n in news_list:
        if n.source == "South China Morning Post":
            n.time = "Null1"
            continue
        request = urllib.request.Request(url=n.link, headers = headers)
        reopen = False
        try:
            response = urllib.request.urlopen(request)
        except Exception as e:
            reopen = True
        if reopen:
            time.sleep(5)
            try:
                response = urllib.request.urlopen(request, timeout=10)
            except Exception as e:
                man_links_both.append(n.link)
                n.time = "Null1"
                n.sentiment = TextBlob(n.title).sentiment
                # print(f"Cannot open {n.link} Because {e}")
                continue
        try:
            raw = response.read().decode('utf-8')
        except Exception as e:
            n.time = "Null1"
            n.sentiment = TextBlob(n.title).sentiment
            continue
        try:
            if n.source == 'South China Morning Post' or n.source == 'The New York Times' or n.source == 'CNBC'\
                    or n.source == 'Washington Post' or n.source == 'Wall Street Journal' or n.source == 'BBC News'\
                    or n.source == 'Daily Mail' or n.source == 'USA TODAY' or "abcnews.go.com" in n.link \
                    or n.source == 'CNA' or n.source == 'Globalnews.ca' or n.source == '7NEWS.com.au' or n.source == 'Seeking Alpha' \
                    or n.source == 'Eater NY' or n.source == 'New York Post' :
                n.time = re.search('"datePublished":"([^"]+?)"', raw).group(1)
            elif n.source == 'CNN International' or n.source == 'MarketWatch' or n.source == 'Newshub' or n.source == 'CTV News' \
                    or n.source == 'Richmond News' or n.source == 'The Star Online' :
                n.time = re.search('"datePublished" content="([^"]+?)"', raw).group(1)
            elif n.source == 'Reuters' or n.source == 'Aljazeera.com' or n.source == 'Livemint' or n.source == 'Khaleej Times' \
                    or n.source == '9News' or n.source == 'Sky News' or n.source == 'Fox News' or n.source == 'Economic Times' \
                    or n.source == 'Gulf News' or n.source == 'The Independent' or n.source == 'NEWS.com.au' \
                    or n.source == 'The Standard' or n.source == 'Reuters.com':
                n.time = re.search('"datePublished": "([^"]+?)",', raw).group(1)
            elif n.source == 'The Guardian' or n.source == 'Politico':
                n.time = re.search("datetime='([^']+?)'", raw).group(1)
            elif n.source == 'NPR' or n.source == 'straits times (press release)' or n.source == 'The Straits Times'\
                    or n.source == 'msnNOW' or n.source == 'KRQE News 13' or n.source == 'Bloomberg' or n.source == 'Al Jazeera America':
                n.time = re.search('datetime="([^"]+?)"', raw).group(1)
            elif n.source == 'Anadolu Agency':
                n.time = re.search('<span style="padding-left:0px;" class="tarih">([^<]+?)</span>', raw).group(1)
            elif n.source == 'Business Insider Nordic':
                n.time = re.search('"datePublished":"([^"]+?)","dateModified"', raw).group(1)
            elif n.source == 'Stuff.co.nz':
                n.time = re.search('<span class="sics-component__byline__date">([^<]+?)</span>', raw).group(1)
            elif n.source == 'Stuff.co.nz' or n.source == 'Stuff.co.nz' or "www.abc.net.au" in n.link or n.source == 'EcoWatch'\
                    or n.source == 'Financial Express' or n.source == 'WJTV' or n.source == 'The National Interest Online (blog)' \
                    or n.source == 'EcoWatch' or n.source == 'The Straits Times' or n.source == 'CNN International' or n.source == 'National Geographic':
                n.time = re.search('"article:published_time" content="([^"]+?)"', raw).group(1)
            elif n.source == 'CNN':
                n.time = re.search('content="([^"]+?)" name="pubdate"', raw).group(1)
            elif n.source == 'Forbes':
                n.time = re.search('property="article:published"\s+?content="([^"]+?)"', raw).group(1)
            elif n.source == 'MarketWatch (blog)':
                n.time = re.search('name="parsely-pub-date" content="([^"]+?)"', raw).group(1)
            elif n.source == 'KSL.com':
                n.time = re.search('"pubDate":"([^"]+?)"', raw).group(1)
            elif n.source == 'Nature.com':
                n.time = re.search('name="prism.publicationDate" content="([^"]+?)"', raw).group(1)
            elif n.source == 'ScienceAlert':
                n.time = re.search('class="published_date" type="hidden" value="([^"]+?)"', raw).group(1)
            else:
                n.time = re.search('"datePublished":\s?"([^"]+?)"', raw).group(1)
        except:
            n.time = "Null2"
            # print(f"Cannot find time in {n.link} - {n.source}")
            man_links_time.append(n.link)
        if n.title.endswith(" ..."):
            in_title = n.title[:-4].replace("?", "\?").replace("$", "\$").replace(".", "\.")
            try:
                n_title = re.search(f'({in_title}[^<"\'\[\]/]+?)[<"\'\[\]/]', raw).group(1)
            except Exception as e:
                man_links_title.append(n.link)
                # print(f"Cannot find title in {n.link}")
                # with open(f"{n.title}.txt", mode="w") as f:
                #     f.write(raw)
                n.sentiment = TextBlob(n.title).sentiment
                continue
            end = min(n_title.find(" - "), n_title.find(" | "))
            if end != -1:
                n_title = n_title[:end]
            n_title.replace("&#x27;", "'").replace("&#039;", "'").replace("[\t\n]", " ")
            n.title = n_title
            n.sentiment = TextBlob(n.title).sentiment
        print("\r%-70s" % n.title, end="")

    source_counter = collections.Counter()
    title_counter = collections.Counter()
    for n in news_list:
        source_counter[n.source] += 1
        title_token = n.title.lower().split(" ")
        for token in title_token:
            title_counter[token] += 1

    # f.write("\n==========\nlinks need manual operation:\n")
    # f.write(f'a. {len(man_links_title)} links \n')
    # for link in man_links:
    #     f.write(f'{link}\n')
    print("\n\nDone! Good Result:")
    print(f"Obtained {len(news_list)} records.")
    print("\nBad Result:")
    print(f'{len(man_links_title)} links cannot get title')
    print(f'{len(man_links_time)} links cannot get time')
    print(f'{len(man_links_both)} links cannot get both title and time')

    with open("news.txt", mode="w") as f:
        for n in news_list:
            f.write(str(n))
        f.write("\n==========\nSource Counter:\n")
        f.write(str(source_counter))
        f.write("\n==========\nTitle Key Word counter:\n")
        f.write(str(title_counter))