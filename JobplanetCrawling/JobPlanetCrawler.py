import lxml.html
import requests
import MySQLdb
from robobrowser import RoboBrowser

conn = MySQLdb.connect(db='Crawler', user='cloud', passwd='1111', charset='utf8mb4')

c=conn.cursor()

select_sql = 'SELECT company FROM re_info'

c.execute(select_sql)

browser = RoboBrowser(parser='html.parser')

browser.open('https://www.jobplanet.co.kr/welcome/index_new')

for row in c.fetchall():
    for i in range(len(row)):

        form = browser.get_form(action='/search')
        form['query'] = row[i]
        browser.submit_form(form, list(form.submit_fields.values()))

        link = browser.select('.is_company_card div > a')
        if not link:
            print('해당 결과 없음')
        if link:
            detail_company = link[0].text
            detail_link = link[0].get('href')
            detail_link = 'https://www.jobplanet.co.kr' + detail_link
            print(detail_company)
            
            detail_page = request.get(detail_link)
            page = lxml.html.fromstring(detail_page.content)
            keyword = page.cssselect('.review_graph_box')
            if not keyword:
                strength = keyword.cssselect('.highcharts-series.highcharts-series-0.highcharts-wordcloud-series.hightcharts-tracker')



        print()
        print()
