# -*- coding: utf-8 -*-
import sys

from collections import Counter

from mysql import query, query_one, save


def get_id_by_url():
    risk_news_data = query("SELECT id , url , title FROM risk_news")
    return risk_news_data


def main():
    risk_news_data = get_id_by_url()

    all_risk_news_title = []

    for risk_news in risk_news_data:
        all_risk_news_title.append(risk_news.get('title'))

    data =  Counter(all_risk_news_title)

    for risk_news in risk_news_data:
        risk_news_id = risk_news.get('id')
        risk_news_url = risk_news.get('url')
        risk_news_title = risk_news.get('title')

        title_number = data.get(risk_news_title)

        if title_number > 1:
            print risk_news_title, risk_news_url, title_number
            # save(sql = "DELETE FROM risk_news WHERE id = %s ", list1=(risk_news_id))
            # main()


if __name__ == '__main__':
    main()
