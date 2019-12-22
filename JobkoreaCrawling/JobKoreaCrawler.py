import requests
import re
import lxml.html
#import datetime
import MySQLdb

conn = MySQLdb.connect(db='Crawler', user='cloud', passwd='1111', charset='utf8mb4')

c=conn.cursor()

delete_sql = 'DELETE from re_info where site_name = "잡코리아"'

c.execute(delete_sql)


def crawling(page_count):
    front_url="http://www.jobkorea.co.kr/Starter/?JoinPossible_Stat=0&schOrderBy=0&LinkGubun=0&LinkNo=0&schType=0&schGid=0&Page="

    for i in range(1, page_count+1):
        url = front_url+str(i)

        list_page=requests.get(url)
        root=lxml.html.fromstring(list_page.content)
        for everything in root.cssselect('.filterList'):
            for thing in everything.cssselect('li'):
                t = 0

                companies = thing.cssselect('.co .coTit a')
                company = companies[0].text.strip()

                titles = thing.cssselect('.info .tit a')
                title = titles[0].text_content().strip()
                title_url = titles[0].get('href')
                
                site_name = '잡코리아'

                field1 = thing.cssselect('.info .sTit span:nth-child(1)')
                field1 = field1[0].text

                field2 = thing.cssselect('.info .sTit span:nth-child(2)')
                if not field2:
                    field2 = 'NULL'
                elif field2:
                    field2 = field2[0].text

                field3 = thing.cssselect('.info .sTit span:nth-child(3)')
                if not field3:
                    field3 = 'NULL'
                elif field3:
                    field3 = field3[0].text

                careers = thing.cssselect('.sDesc strong')
                career = careers[0].text

                academics = thing.cssselect('.sDesc span:nth-child(2)')
                academic = academics[0].text
                
                title_url = 'http://www.jobkorea.co.kr'+title_url
                detail_page = requests.get(title_url)
                work = lxml.html.fromstring(detail_page.content)
                working = work.cssselect('.tbRow.clear div:nth-child(2) dd:nth-child(2) .addList .col_1')
                if not working:
                    workingcondition = ''

                elif working:
                    workingcondition = working[0].text

                areas = thing.cssselect('.sDesc span:nth-child(3)')
                area = areas[0].text
                area = area.split(', ')[0]

                deadlines = thing.cssselect('.side .day')
                deadline = deadlines[0].text
#                if deadline == "내일마감":
#                    deadline = datetime.datetime.now()+1
#                elif deadline == "오늘마감":
#                    deadline == datetime.datetime.now()                 
#                elif deadline == "채용시":
#                    deadline == datetime.datetime.now()
#                else:
#                    tmp = deadline.split('(')[0]
#                    deadline = datetime.datetime.strptime(tmp, "~%Y.%m.%d").date()

                insert_sql = 'INSERT INTO re_info(company, title, title_url, site_name, field1, field2, field3, career, academic, area, workingcondition, deadline) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                    
                insert_val = company, title, title_url, site_name, field1, field2, field3, career, academic, area, workingcondition, deadline
                    
                c.execute(insert_sql, insert_val)
                    
                conn.commit()

def main():
    page_count = 4
    crawling(page_count)

    conn.close()

main()
