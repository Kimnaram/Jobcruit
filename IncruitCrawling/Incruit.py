import requests
import re
import lxml.html
import MySQLdb

conn = MySQLdb.connect(db='Crawler', user='cloud', passwd='1111', charset='utf8mb4')

c=conn.cursor()

def crawling(page_count):
    front_url="http://job.incruit.com/entry/searchjob.asp?ct=12&ty=1&cd=1&page="

    for i in range(1, page_count+1):
        url = front_url+str(i)

        list_page=requests.get(url)
        root=lxml.html.fromstring(list_page.content)
        for everything in root.cssselect('tbody'):
            for thing in everything.cssselect('tr'):
                t = 0

                companies = thing.cssselect('.check_list_r a')
                if not companies:
                    company = ' '
                elif companies:
                    company = companies[0].text.strip()

                titles = thing.cssselect('.subjects .accent a')
                if not titles:
                    title = ' '
                    title_url = ' '
                elif titles:
                    title = titles[0].text_content().strip()
                    title_url = titles[0].get('href')

                site_name = '인크루트'

                field1 = thing.cssselect('.subjects .details_txts .firstChild')
                if not field1:
                    field1 = ' '
                elif filed1:
                    field1 = field1[0].text

                detail_page = requests.get(title_url)
                detail = lxml.html.fromstring(detail_page.content)

                careers = detail.cssselect('.jobpost_sider_jbinfo > div:nth-child(3) > dl:nth-child(2) > dd > div > div > em')
                if not careers:
                    career = ' '
                elif careers:
                    career = careers[0].text

                academics = detail.cssselect('.jobpost_sider_jbinfo > div:nth-child(3) > dl:nth-child(3) > dd > div > div > em')
                if not academics:
                    academic = ' '
                elif academics:
                    academic = academics[0].text

                working = detail.cssselect('.jobpost_sider_jbinfo > div.jobpost_sider_jbinfo_inlay.jobpost_sider_jbinfo_inlay_last > dl:nth-child(2) > dd > div > div.tooltip_layer_warp > ul > li')
                if not working:
                    workingcondition = ''

                elif working:
                    workingcondition = working[0].text

                areas = detail.cssselect('.jobpost_sider_jbinfo > div.jobpost_sider_jbinfo_inlay.jobpost_sider_jbinfo_inlay_last > dl:nth-child(3) > dd > div > div.inset_ely_lay')
                area = areas[0].text
                area = area.split('> ')[0]

                deadlines = thing.cssselect('.ddays')
                deadline = deadlines[0].text

                select_sql = 'SELECT title, titlelink FROM re_info'

                c.execute(select_sql)

                for row in c.fetchall():
                    for i in range(len(row)):
                        if row[i] == title or row[i] == title_url:
                            t = 1

                if t == 0:
                    insert_sql = 'INSERT INTO re_info(company, title, titlelink, sitename, field, career, academic, area, workingcondition, deadline) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                    insert_val = company, title, title_url, site_name, field1, career, academic, area, workingcondition, deadline

                    c.execute(insert_sql, insert_val)

                    conn.commit()

def main():
    page_count = 10
    crawling(page_count)

    conn.close()

main()
