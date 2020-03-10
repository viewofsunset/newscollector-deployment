import numpy as np
import pandas as pd
import requests
import datetime
import random
import time
import re
import lxml
from tqdm import tqdm, trange
from requests.compat import quote_plus
from django.shortcuts import render
from django.urls import path
from bs4 import BeautifulSoup as bs4
from . import views
from . import models
# from models import Product

# Create your views here.


def index(request):
    data1 = {
        'insert_me': "hello this is from views.py page"
    }
    return render(request, 'index.html', context=data1)


def search(request):

    search_input_get = request.POST.get('search_input')
    query_day0 = search_input_get
    query_day = int(query_day0)
    query_day_str = str(query_day)

    datetime.date.today()
    t0 = datetime.date.today()
    t1 = str(t0)
    t2 = t1.split("-")
    t3 = "".join(t2)
    date_today = t3
    date_today_str = str(date_today)

    a_urls = []
    a_titles = []
    a_contents = []
    a_dates = []
    a_medias = []

    final_postings = []

    media_name_0 = "The_Bell"
    media_name_1 = "NewsMP"
    media_name_2 = "DailyPharm"
    media_name_3 = "BioSpectator"

    media_name_0_page_num = 1
    media_name_1_a_page_num = 1
    media_name_1_b_page_num = 1
    media_name_1_c_page_num = 1
    media_name_1_d_page_num = 1
    media_name_1_e_page_num = 1
    media_name_1_f_page_num = 1
    media_name_2_page_num = 0
    media_name_3_page_num = 1

    def get_article_0(media_name_0_page_num):
        base_url = (
            f"http://www.thebell.co.kr/free/content/article.asp?page={media_name_0_page_num}&svccode=00"
        )
        print(base_url)
        response = requests.get(base_url)
        article_base_url = "http://www.thebell.co.kr/free/content/"

        if response.status_code == 200:
            a_num = 1
            print("Page :", a_num)
            while a_num < 11:

                article_url = f"#contents > div.contentSection > div > div.newsBox > div.newsList > div.listBox > ul > li:nth-child({a_num}) > dl > a"
                article_title_url = f"#contents > div.contentSection > div > div.newsBox > div.newsList > div.listBox > ul > li:nth-child({a_num}) > dl > a > dt"
                article_contents_url = f"#contents > div.contentSection > div > div.newsBox > div.newsList > div.listBox > ul > li:nth-child({a_num}) > dl > a > dd"
                article_date_url = f"#contents > div.contentSection > div > div.newsBox > div.newsList > div.listBox > ul > li:nth-child({a_num}) > dl > dd > span.date"
                a_num += 1

                soup1 = bs4(response.content, "html.parser",
                            from_encoding="utf-8")
                # soup2 = bs4(response.text, "lxml")
                # soup3 = bs4(response.text, "html5lib")

                tag_url_0 = soup1.select(article_url)[0]
                tag_url_1 = tag_url_0["href"]
                tag_url_3 = article_base_url + tag_url_1

                tag_title_0 = soup1.select(article_title_url)[0]
                tag_title_1 = tag_title_0.get_text().strip()
                # print(tag_title_1)

                tag_contents_0 = soup1.select(article_contents_url)[0]
                tag_contents_1 = tag_contents_0.get_text().strip()
                # print(tag_contents_1)

                tag_date_0 = soup1.select(article_date_url)[0]
                tag_date_1 = str(tag_date_0)
                tag_date_2 = tag_date_1.split('">')[1].strip()
                tag_date_3 = tag_date_2.split(" ")[0].strip()
                tag_date_4 = tag_date_3.split("-")
                tag_date_5 = "".join(tag_date_4)
                article_date = int(tag_date_5)
                print(article_date)

                urls = tag_url_3
                dates = tag_date_5
                medias = "더벨"
                titles = tag_title_1
                contents = tag_contents_1

                final_postings.append((urls, dates, medias, titles, contents))

                a_urls.append(tag_url_3)
                a_dates.append(tag_date_5)
                a_medias.append("더벨")
                a_titles.append(tag_title_1)
                a_contents.append(tag_contents_1)

            if query_day < article_date:
                time.sleep(random.randint(1, 2))
                media_name_0_page_num += 1
                get_article_0(media_name_0_page_num)
            else:
                print("if inside else")
            # print(first_page_count)
        else:
            total_page += 1

    get_article_0(media_name_0_page_num)
    print(
        "*************************** Finished The Bell  ***************************"
    )

    media_name_1_a_page_num = 1

    def get_article_1_a(media_name_1_a_page_num=1):
        total_page = 10004
        base_url = f"http://www.newsmp.com/news/articleList.html?page={media_name_1_a_page_num}&total={total_page}&box_idxno=&sc_section_code=S1N6&view_type=sm"
        print(base_url)
        response = requests.get(base_url)
        print(response)
        article_base_url = "http://www.newsmp.com"

        if response.status_code == 200:
            a_num = 1
            print("Page :", a_num)
            while a_num < 21:

                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > div.list-titles > a > strong
                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > p > a
                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > div.list-dated

                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(20) > div.list-titles > a > strong

                article_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-titles > a"
                article_title_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-titles > a > strong"
                article_contents_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > p > a"
                article_date_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-dated"
                a_num += 1

                soup1 = bs4(response.text, "html.parser")
                # soup2 = bs4(response.text, "lxml")
                # soup3 = bs4(response.text, "html5lib")

                tag_url_0 = soup1.select(article_url)[0]
                tag_url_1 = str(tag_url_0)
                tag_url_2 = tag_url_1.split('"')[1]
                tag_url_3 = article_base_url + tag_url_2
                # print(tag_url_3)

                tag_title_0 = soup1.select(article_title_url)[0]
                tag_title_1 = tag_title_0.get_text().strip()
                # print(tag_title_1)

                tag_contents_0 = soup1.select(article_contents_url)[0]
                tag_contents_1 = tag_contents_0.get_text().strip()
                # print(tag_contents_1)

                tag_date_0 = soup1.select(article_date_url)[0]
                tag_date_1 = str(tag_date_0)
                tag_date_2 = tag_date_1.split("|")[2].strip()
                tag_date_3 = tag_date_2.split("</div")[0].strip()
                tag_date_4 = tag_date_3.split(" ")[0]
                tag_date_5 = tag_date_4.split("-")
                tag_date_6 = "".join(tag_date_5)
                # print(tag_date_6)
                article_date = int(tag_date_6)
                print(article_date)

                a_urls.append(tag_url_3)
                a_dates.append(tag_date_6)
                a_medias.append("의약뉴스-의약정책")
                a_titles.append(tag_title_1)
                a_contents.append(tag_contents_1)

            if query_day < article_date:
                time.sleep(random.randint(1, 2))
                media_name_1_a_page_num += 1
                get_article_1_a(media_name_1_a_page_num)
            else:
                print("if inside else")
            # print(first_page_count)
        else:
            total_page += 1

    get_article_1_a(media_name_1_a_page_num)

    print(
        "*************************** Finished NewsMP-A ***************************"
    )
    time.sleep(random.randint(1, 2))

    def get_article_1_b(media_name_1_b_page_num):
        total_page = 37479
        base_url = f"http://www.newsmp.com/news/articleList.html?page={media_name_1_b_page_num}&total={total_page}&box_idxno=&sc_section_code=S1N2&view_type=sm"
        print(base_url)
        response = requests.get(base_url)
        print(response)
        article_base_url = "http://www.newsmp.com"

        if response.status_code == 200:
            a_num = 1
            print("Page :", a_num)
            while a_num < 21:

                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > div.list-titles > a > strong
                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > p > a
                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > div.list-dated

                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(20) > div.list-titles > a > strong

                article_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-titles > a"
                article_title_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-titles > a > strong"
                article_contents_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > p > a"
                article_date_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-dated"
                a_num += 1

                soup1 = bs4(response.text, "html.parser")
                # soup2 = bs4(response.text, "lxml")
                # soup3 = bs4(response.text, "html5lib")

                tag_url_0 = soup1.select(article_url)[0]
                tag_url_1 = str(tag_url_0)
                tag_url_2 = tag_url_1.split('"')[1]
                tag_url_3 = article_base_url + tag_url_2
                # print(tag_url_3)

                tag_title_0 = soup1.select(article_title_url)[0]
                tag_title_1 = tag_title_0.get_text().strip()
                # print(tag_title_1)

                tag_contents_0 = soup1.select(article_contents_url)[0]
                tag_contents_1 = tag_contents_0.get_text().strip()
                # print(tag_contents_1)

                tag_date_0 = soup1.select(article_date_url)[0]
                tag_date_1 = str(tag_date_0)
                tag_date_2 = tag_date_1.split("|")[2].strip()
                tag_date_3 = tag_date_2.split("</div")[0].strip()
                tag_date_4 = tag_date_3.split(" ")[0]
                tag_date_5 = tag_date_4.split("-")
                tag_date_6 = "".join(tag_date_5)

                article_date = int(tag_date_6)
                print(article_date)

                a_urls.append(tag_url_3)
                a_dates.append(tag_date_6)
                a_medias.append("의약뉴스-제약산업")
                a_titles.append(tag_title_1)
                a_contents.append(tag_contents_1)

            if query_day < article_date:
                time.sleep(random.randint(1, 2))
                media_name_1_b_page_num += 1
                get_article_1_b(media_name_1_b_page_num)
            else:
                print("if inside else")

        else:
            total_page += 1

    get_article_1_b(media_name_1_b_page_num)

    print(
        "*************************** Finished NewsMP_B ***************************"
    )
    time.sleep(random.randint(1, 2))

    def get_article_1_c(media_name_1_c_page_num):
        total_page = 45980
        base_url = f"http://www.newsmp.com/news/articleList.html?page={media_name_1_c_page_num}&total={total_page}&box_idxno=&sc_section_code=S1N3&view_type=sm"

        print(base_url)
        response = requests.get(base_url)
        print(response)
        article_base_url = "http://www.newsmp.com"

        if response.status_code == 200:
            a_num = 1
            print("Page :", a_num)
            while a_num < 21:

                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > div.list-titles > a > strong
                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > p > a
                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > div.list-dated

                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(20) > div.list-titles > a > strong

                article_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-titles > a"
                article_title_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-titles > a > strong"
                article_contents_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > p > a"
                article_date_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-dated"
                a_num += 1

                soup1 = bs4(response.text, "html.parser")
                # soup2 = bs4(response.text, "lxml")
                # soup3 = bs4(response.text, "html5lib")

                tag_url_0 = soup1.select(article_url)[0]
                tag_url_1 = str(tag_url_0)
                tag_url_2 = tag_url_1.split('"')[1]
                tag_url_3 = article_base_url + tag_url_2
                # print(tag_url_3)

                tag_title_0 = soup1.select(article_title_url)[0]
                tag_title_1 = tag_title_0.get_text().strip()
                # print(tag_title_1)

                tag_contents_0 = soup1.select(article_contents_url)[0]
                tag_contents_1 = tag_contents_0.get_text().strip()
                # print(tag_contents_1)

                tag_date_0 = soup1.select(article_date_url)[0]
                tag_date_1 = str(tag_date_0)
                tag_date_2 = tag_date_1.split("|")[2].strip()
                tag_date_3 = tag_date_2.split("</div")[0].strip()
                tag_date_4 = tag_date_3.split(" ")[0]
                tag_date_5 = tag_date_4.split("-")
                tag_date_6 = "".join(tag_date_5)
                # print(tag_date_6)
                article_date = int(tag_date_6)
                print(article_date)

                a_urls.append(tag_url_3)
                a_dates.append(tag_date_6)
                a_medias.append("의약뉴스-의사병원")
                a_titles.append(tag_title_1)
                a_contents.append(tag_contents_1)

                # first_page_count = len(urls)
                # time.sleep(random.randint(1, 2))
            if query_day < article_date:
                time.sleep(random.randint(1, 2))
                media_name_1_c_page_num += 1
                get_article_1_c(media_name_1_c_page_num)
            else:
                print("if inside else")
            # print(first_page_count)
        else:
            total_page += 1

    get_article_1_c(media_name_1_c_page_num)

    print(
        "*************************** Finished NewsMP_C ***************************"
    )
    time.sleep(random.randint(1, 2))

    def get_article_1_d(media_name_1_d_page_num):
        total_page = 22685
        base_url = f"http://www.newsmp.com/news/articleList.html?page={media_name_1_d_page_num}&total={total_page}&box_idxno=&sc_section_code=S1N4&view_type=sm"

        print(base_url)
        response = requests.get(base_url)
        print(response)
        article_base_url = "http://www.newsmp.com"

        if response.status_code == 200:
            a_num = 1
            print("Page :", a_num)
            while a_num < 21:

                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > div.list-titles > a > strong
                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > p > a
                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > div.list-dated

                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(20) > div.list-titles > a > strong

                article_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-titles > a"
                article_title_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-titles > a > strong"
                article_contents_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > p > a"
                article_date_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-dated"
                a_num += 1

                soup1 = bs4(response.text, "html.parser")
                # soup2 = bs4(response.text, "lxml")
                # soup3 = bs4(response.text, "html5lib")

                tag_url_0 = soup1.select(article_url)[0]
                tag_url_1 = str(tag_url_0)
                tag_url_2 = tag_url_1.split('"')[1]
                tag_url_3 = article_base_url + tag_url_2
                # print(tag_url_3)

                tag_title_0 = soup1.select(article_title_url)[0]
                tag_title_1 = tag_title_0.get_text().strip()
                # print(tag_title_1)

                tag_contents_0 = soup1.select(article_contents_url)[0]
                tag_contents_1 = tag_contents_0.get_text().strip()
                # print(tag_contents_1)

                tag_date_0 = soup1.select(article_date_url)[0]
                tag_date_1 = str(tag_date_0)
                tag_date_2 = tag_date_1.split("|")[2].strip()
                tag_date_3 = tag_date_2.split("</div")[0].strip()
                tag_date_4 = tag_date_3.split(" ")[0]
                tag_date_5 = tag_date_4.split("-")
                tag_date_6 = "".join(tag_date_5)
                # print(tag_date_6)
                article_date = int(tag_date_6)
                print(article_date)

                a_urls.append(tag_url_3)
                a_dates.append(tag_date_6)
                a_medias.append("의약뉴스-약사유통")
                a_titles.append(tag_title_1)
                a_contents.append(tag_contents_1)

                # first_page_count = len(urls)
                # time.sleep(random.randint(1, 2))
            if query_day < article_date:
                time.sleep(random.randint(1, 2))
                media_name_1_d_page_num += 1
                get_article_1_d(media_name_1_d_page_num)
            else:
                print("if inside else")
            # print(first_page_count)
        else:
            total_page += 1

    get_article_1_d(media_name_1_d_page_num)

    print(
        "*************************** Finished NewsMP_D ***************************"
    )
    time.sleep(random.randint(1, 2))

    def get_article_1_e(media_name_1_e_page_num):
        total_page = 7124
        base_url = f"http://www.newsmp.com/news/articleList.html?page={media_name_1_e_page_num}&total={total_page}&box_idxno=&sc_section_code=S1N5&view_type=sm"

        print(base_url)
        response = requests.get(base_url)
        print(response)
        article_base_url = "http://www.newsmp.com"

        if response.status_code == 200:
            a_num = 1
            print("Page :", a_num)
            while a_num < 21:

                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > div.list-titles > a > strong
                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > p > a
                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > div.list-dated

                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(20) > div.list-titles > a > strong

                article_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-titles > a"
                article_title_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-titles > a > strong"
                article_contents_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > p > a"
                article_date_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-dated"
                a_num += 1

                soup1 = bs4(response.text, "html.parser")
                # soup2 = bs4(response.text, "lxml")
                # soup3 = bs4(response.text, "html5lib")

                tag_url_0 = soup1.select(article_url)[0]
                tag_url_1 = str(tag_url_0)
                tag_url_2 = tag_url_1.split('"')[1]
                tag_url_3 = article_base_url + tag_url_2
                # print(tag_url_3)

                tag_title_0 = soup1.select(article_title_url)[0]
                tag_title_1 = tag_title_0.get_text().strip()
                # print(tag_title_1)

                tag_contents_0 = soup1.select(article_contents_url)[0]
                tag_contents_1 = tag_contents_0.get_text().strip()
                # print(tag_contents_1)

                tag_date_0 = soup1.select(article_date_url)[0]
                tag_date_1 = str(tag_date_0)
                tag_date_2 = tag_date_1.split("|")[2].strip()
                tag_date_3 = tag_date_2.split("</div")[0].strip()
                tag_date_4 = tag_date_3.split(" ")[0]
                tag_date_5 = tag_date_4.split("-")
                tag_date_6 = "".join(tag_date_5)
                # print(tag_date_6)
                article_date = int(tag_date_6)
                print(article_date)

                a_urls.append(tag_url_3)
                a_dates.append(tag_date_6)
                a_medias.append("의약뉴스-간호기타")
                a_titles.append(tag_title_1)
                a_contents.append(tag_contents_1)

                # first_page_count = len(urls)
                # time.sleep(random.randint(1, 2))
            if query_day < article_date:
                time.sleep(random.randint(1, 2))
                media_name_1_e_page_num += 1
                get_article_1_e(media_name_1_e_page_num)
            else:
                print("if inside else")
            # print(first_page_count)
        else:
            total_page += 1

    get_article_1_e(media_name_1_e_page_num)

    print(
        "*************************** Finished collecting article_2 ***************************"
    )
    time.sleep(random.randint(1, 2))

    def get_article_1_f(media_name_1_f_page_num):
        total_page = 10005
        base_url = f"http://www.newsmp.com/news/articleList.html?page={media_name_1_f_page_num}&total={total_page}&box_idxno=&sc_section_code=S1N6&view_type=sm"

        print(base_url)
        response = requests.get(base_url)
        print(response)
        article_base_url = "http://www.newsmp.com"

        if response.status_code == 200:
            a_num = 1
            print("Page :", a_num)
            while a_num < 21:

                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > div.list-titles > a > strong
                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > p > a
                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(1) > div.list-dated

                # user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child(20) > div.list-titles > a > strong

                article_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-titles > a"
                article_title_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-titles > a > strong"
                article_contents_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > p > a"
                article_date_url = f"#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div:nth-child({a_num}) > div.list-dated"
                a_num += 1

                soup1 = bs4(response.text, "html.parser")
                # soup2 = bs4(response.text, "lxml")
                # soup3 = bs4(response.text, "html5lib")

                tag_url_0 = soup1.select(article_url)[0]
                tag_url_1 = str(tag_url_0)
                tag_url_2 = tag_url_1.split('"')[1]
                tag_url_3 = article_base_url + tag_url_2
                # print(tag_url_3)

                tag_title_0 = soup1.select(article_title_url)[0]
                tag_title_1 = tag_title_0.get_text().strip()
                # print(tag_title_1)

                tag_contents_0 = soup1.select(article_contents_url)[0]
                tag_contents_1 = tag_contents_0.get_text().strip()
                # print(tag_contents_1)

                tag_date_0 = soup1.select(article_date_url)[0]
                tag_date_1 = str(tag_date_0)
                tag_date_2 = tag_date_1.split("|")[2].strip()
                tag_date_3 = tag_date_2.split("</div")[0].strip()
                tag_date_4 = tag_date_3.split(" ")[0]
                tag_date_5 = tag_date_4.split("-")
                tag_date_6 = "".join(tag_date_5)
                # print(tag_date_6)
                article_date = int(tag_date_6)
                print(article_date)

                a_urls.append(tag_url_3)
                a_dates.append(tag_date_6)
                a_medias.append("의약뉴스-해외")
                a_titles.append(tag_title_1)
                a_contents.append(tag_contents_1)

                # first_page_count = len(urls)
                # time.sleep(random.randint(1, 2))
            if query_day < article_date:
                time.sleep(random.randint(1, 2))
                media_name_1_f_page_num += 1
                get_article_1_f(media_name_1_f_page_num)
            else:
                print("if inside else")
            # print(first_page_count)
        else:
            total_page += 1

    get_article_1_f(media_name_1_f_page_num)

    print(
        "*************************** Finished NewsMP_F ***************************"
    )

    def get_article_2(media_name_2_page_num):
        base_url = f"http://www.dailypharm.com/Users/News/NewsList.html?nPage={media_name_2_page_num}&dpsearch=&date="
        print(base_url)
        response = requests.get(base_url)
        article_base_url = "http://www.dailypharm.com/Users/News/"

        if response.status_code == 200:
            a_num = 1
            print("Page :", a_num)
            while a_num < 11:

                # body > div.wrap > div.NewsCenterSide > div > ul > li:nth-child(1) > a
                # body > div.wrap > div.NewsCenterSide > div > ul > li:nth-child(1) > a > div.listHead
                # body > div.wrap > div.NewsCenterSide > div > ul > li:nth-child(1) > a > div.listContent
                # body > div.wrap > div.NewsCenterSide > div > ul > li:nth-child(1) > a > div.listHead > span

                article_url = f"body > div.wrap > div.NewsCenterSide > div > ul > li:nth-child({a_num}) > a"
                article_title_url = f"body > div.wrap > div.NewsCenterSide > div > ul > li:nth-child({a_num}) > a > div.listHead"
                article_contents_url = f"body > div.wrap > div.NewsCenterSide > div > ul > li:nth-child({a_num}) > a > div.listContent"
                article_date_url = f"body > div.wrap > div.NewsCenterSide > div > ul > li:nth-child({a_num}) > a > div.listHead > span"
                a_num += 1

                soup1 = bs4(
                    response.content, "html.parser", from_encoding="utf-8"
                )  # response.text
                # soup2 = bs4(response.text, "lxml")
                # soup3 = bs4(response.text, "html5lib")
                # print(soup1)

                tag_url_0 = soup1.select(article_url)[0]
                tag_url_1 = tag_url_0["href"]
                tag_url_3 = article_base_url + tag_url_1
                # print(tag_url_3)
                # print(tag_url_1)
                # print(tag_url_3)

                tag_title_0 = soup1.select(article_title_url)[0]
                tag_title_1 = tag_title_0.get_text().strip()
                # print(tag_title_1)

                tag_contents_0 = soup1.select(article_contents_url)[0]
                tag_contents_1 = tag_contents_0.get_text().strip()
                # print(tag_contents_1)

                tag_date_0 = soup1.select(article_date_url)[0]
                tag_date_1 = tag_date_0.get_text().strip()
                # print(tag_date_1)
                # print(type(tag_date_1))
                tag_date_2 = tag_date_1.split(" ")[0].strip()
                tag_date_4 = tag_date_2.split("-")
                tag_date_5 = "".join(tag_date_4)
                article_date = int(tag_date_5)
                print(article_date)

                a_urls.append(tag_url_3)
                a_dates.append(tag_date_5)
                a_medias.append("데일리팜")
                a_titles.append(tag_title_1)
                a_contents.append(tag_contents_1)
            # print(article_date)
            # print(query_day)
            if query_day < article_date:
                time.sleep(random.randint(1, 2))
                media_name_2_page_num += 1
                get_article_2(media_name_2_page_num)
            else:
                print("if inside else")

        else:
            total_page += 1

    get_article_2(media_name_2_page_num)
    print(
        "*************************** Finished DailyPharm ***************************"
    )

    def get_article_3(media_name_3_page_num):
        urls_init = []

        base_url = f"http://www.biospectator.com/section/section_list.php?MID=10000&page={media_name_3_page_num}"
        print(base_url)
        response = requests.get(base_url)
        article_base_url = "http://www.biospectator.com"

        if response.status_code == 200:
            soup1 = bs4(response.content, "html.parser", from_encoding="utf-8")
            # soup2 = bs4(response.text, "lxml")
            # soup3 = bs4(response.text, "html5lib")
            # print(soup1)

            # tags_sub = html_sub.find(id="articleTitle")
            # span = a_tag.find("span", {"class": "an_txt"})
            # d1 = soup1.find_all("p", {"class": "article_tit"})[a_num]

            d1 = soup1.find_all(id="container")[0]
            d2 = str(d1)

            a_num_url = 1
            while a_num_url < 64:
                d3 = re.split('a href="|">\n<img', d2)[a_num_url]
                a_num_url += 4
                tag_url_3 = article_base_url + d3
                a_urls.append(tag_url_3)
                urls_init.append(tag_url_3)

            a_num_tit = 0
            while a_num_tit < 16:
                article_title_url = f"#container > div > div > div.subtit > h3"
                tit_url = urls_init[a_num_tit]
                a_num_tit += 1
                response_tit = requests.get(tit_url)
                soup_tit = bs4(response_tit.content,
                               "html.parser", from_encoding="utf-8")
                tag_title_0 = soup_tit.select(article_title_url)[
                    0].get_text().strip()
                a_titles.append(tag_title_0)

            a_num_cont = 0
            while a_num_cont < 16:
                article_contents_url = (
                    f"#container > div > div > div.contents > div.article_view > h4"
                )
                cont_url = urls_init[a_num_cont]
                a_num_cont += 1
                response_cont = requests.get(cont_url)
                soup_cont = bs4(response_cont.content,
                                "html.parser", from_encoding="utf-8")
                tag_contents_0 = (
                    soup_cont.select(article_contents_url)[
                        0].get_text().strip()
                )
                a_contents.append(tag_contents_0)

            a_num_date = 0
            while a_num_date < 16:
                article_date_url = f"#container > div > div > div.subtit > div.datetime"
                date_url = urls_init[a_num_date]
                a_num_date += 1
                response_date = requests.get(date_url)
                soup_date = bs4(response_date.content,
                                "html.parser", from_encoding="utf-8")
                tag_date_0 = soup_date.select(article_date_url)[
                    0].get_text().strip()
                tag_date_1 = tag_date_0.split(" ")[2]
                tag_date_2 = tag_date_1.split("-")
                tag_date_3 = "".join(tag_date_2)
                article_date = int(tag_date_3)
                a_dates.append(tag_date_3)
                a_medias.append("BioSpectator")

            if query_day < article_date:
                time.sleep(random.randint(1, 2))
                media_name_3_page_num += 1
                # print("page_num = ", page_num)
                # print(query_day, article_date)
                get_article_3(media_name_3_page_num)
            else:
                print("if inside else")
        else:
            total_page += 1

        # return article_date

    get_article_3(media_name_3_page_num)

    print(
        "*************************** Finished BioSpectator ***************************"
    )

    dict_data = {
        "Date": a_dates,
        "Media": a_medias,
        "Article_Title": a_titles,
        "Article_Contents": a_contents,
        "Site_URL": a_urls,
    }
    df_data = pd.DataFrame(dict_data)

    ##### Keywords #####
    p = r'.*(보로노이|로슈|다케다|길리어드|노바티스|사노피|제넨텍|GSK|화이자|머크|얀센|임상|FDA|허가|항암제|라이센싱|승인|기술이전|IPO|신약|AI|AbbVie|스탠다임).*'
    df_data_filtered = df_data[df_data['Article_Title'].str.match(
        p) | df_data['Article_Contents'].str.match(p, flags=re.MULTILINE)]
    ####################

    df_data.to_csv(date_today_str + 'to' + query_day_str + ".csv", index=False)
    df_data_filtered.to_csv(date_today_str + 'to' +
                            query_day_str + "filtered" + ".csv", index=False)

    #### display DataFrame format to HTML #####
    df_data_filtered_html = df_data_filtered.to_html

    stuff_for_frontend = {
        'serch_input_post': search_input_get,
        'final_postings_post': df_data_filtered_html
    }
    return render(request, 'app1/search.html', context=stuff_for_frontend)
