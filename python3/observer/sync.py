import os, sys
sys.path.append(os.getcwd())

from datetime import datetime

from process import (read_config, write_config, yqj_article_total,
                    yqj_categories_to_observer_categories, yqj_articles, 
                    yqj_area, yqj_publisher, yqj_categories, observer_area, 
                    observer_article_save, observer_article_area_save, 
                    observer_article_category_save, yqj_inspection_total, 
                    yqj2_risknews, yqj2_risknews_total, yqj2_area, 
                    yqj2_publisher, 
                    )
from utils.string.format import (str_to_md5str, )


class Sync:

    def __init__(self):
        config = read_config()
        self.mysql_conf = config['mysql']
        self.sync_conf = config['sync']

    # sync yqj -> observer
    def yqj(self):
        # yqj.article -> observer.article
        index = self.sync_conf['yqj.article']
        total = yqj_article_total(self.mysql_conf)

        while index <= total:
            # process data
            articles = yqj_articles(index, 100, self.mysql_conf)

            for article in articles:
                title = article[0]
                url = article[1]
                if not url:
                    continue
                
                pubtime = article[2]
                if pubtime > datetime.now():
                    continue

                area = yqj_area(article[3], self.mysql_conf)
                publisher = yqj_publisher(article[4], self.mysql_conf)
                categories = yqj_categories_to_observer_categories(yqj_categories(article[5], self.mysql_conf))
                area_id = observer_area(area, self.mysql_conf)
                guid = str_to_md5str(url)

                # save
                observer_article_save(guid, title, url, pubtime, publisher, mysql_conf=self.mysql_conf)
                observer_article_area_save(guid, area_id, self.mysql_conf)
                for category_id in categories:
                    observer_article_category_save(guid, category_id, self.mysql_conf)

            index += 100
            # record point
            write_config('sync', 'yqj.article', index)

        # yqj.inspection -> observer.inspection
        # TODO

    # sync yqj -> observer
    def yqj2(self):
        # yqj.risk_news -> observer.article
        index = self.sync_conf['yqj2.risk_news']
        total = yqj2_risknews_total(self.mysql_conf)

        while index <= total:
            # process data
            risknews = yqj2_risknews(index, 100, self.mysql_conf)

            for r in risknews:
                r_id = r[0]
                title = r[1]
                url = r[2]
                if not url:
                    continue

                pubtime = r[3]
                if pubtime > datetime.now():
                    continue

                area_id = r[4]
                publisher_id = r[5]
                is_delete = r[6]
                status = 1 if is_delete == 2 else -1

                risk_keyword = r[7]
                invalid_keyword = r[8]

                area = yqj2_area(r_id, self.mysql_conf)
                publisher = yqj2_publisher(r_id, self.mysql_conf)
                area_id = observer_area(area, self.mysql_conf)
                guid = str_to_md5str(url)

                # save
                observer_article_save(guid, title, url, pubtime, publisher, risk_keyword=risk_keyword, invalid_keyword=invalid_keyword, status=status, mysql_conf=self.mysql_conf)
                observer_article_area_save(guid, area_id, self.mysql_conf)
                observer_article_category_save(guid, '0002', self.mysql_conf)

            index += 100
            # record point
            write_config('sync', 'yqj2.risk_news', index)



if __name__ == '__main__':
    sync = Sync()
    sync.yqj()
    # sync.yqj2()
