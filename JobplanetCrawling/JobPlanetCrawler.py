from robobrowser import RoboBrowser

browser = RoboBrowser(parser='html.parser')

browser.open('https://www.jobplanet.co.kr/welcome/index_new')

form = browser.get_form(action='/search')
form['query'] = '삼성생명보험(주)'
browser.submit_form(form, list(form.submit_fields.values()))

for a in browser.select('.is_company_card div > a'):
    print(a.text)
    print(a.get('href'))
    print()
