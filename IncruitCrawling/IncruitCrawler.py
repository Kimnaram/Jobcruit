import requests
import re
import lxml.html
import MySQLdb

conn = MySQLdb.connect(db='Crawler', user='cloud', passwd='1111', charset='utf8mb4')

c=conn.cursor()

delete_sql = 'DELETE FROM re_info WHERE site_name = "인크루트"'
c.execute(delete_sql)

def crawling(page_count):
    front_url="http://job.incruit.com/entry/searchjob.asp?ct=12&ty=1&cd=1&page="

    for i in range(1, page_count+1):
        url = front_url+str(i)

        list_page=requests.get(url)
        root=lxml.html.fromstring(list_page.content)
        for everything in root.cssselect('tbody'):
            for thing in everything.cssselect('tr'):
                t = 0

                companies = thing.cssselect('th > div > .check_list_r > .links > a')
                if not companies:
                    company = ' '
                elif companies:
                    company = companies[0].text.strip()

                titles = thing.cssselect('td > .subjects > .accent > a')
                
                if not titles:
                    title = ' '
                    title_url = ' '
                if titles:
                    title = titles[0].text_content()
                    title_url = titles[0].get('href')
                
                site_name = '인크루트'

                field1 = thing.cssselect('td > .subjects > .details_txts.firstChild > em')
                if not field1:
                    field1 = ' '
                elif field1:
                    field1 = field1[0].text
                
                if title_url != ' ':
                    #title_url = "https://"+title_url
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
                    if not areas:
                        area = ' '
                    if areas:
                        area = areas[0].text
                        area = area.split('> ')[0]

                    deadlines = thing.cssselect('.ddays')
                    if not deadlines:
                        deadline = ' '
                    if deadlines:
                        deadline = deadlines[0].text
                    
                    insert_sql = 'INSERT INTO re_info(company, title, title_url, site_name, field1, career, academic, area, workingcondition, deadline) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                    
                    insert_val = company, title, title_url, site_name, field1, career, academic, area, workingcondition, deadline
                    
                    c.execute(insert_sql, insert_val)
                    
                conn.commit()

def main():
    page_count = 6
    crawling(page_count)

    conn.close()

main()
