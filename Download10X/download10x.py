import requests
from bs4 import BeautifulSoup as Soup
import unicodedata

def get_links(cik, priorto, count,report_type):
    max_count = 20
    if report_type == '10-K':
        link = "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+str(cik)+"&type=10-K&dateb="+str(priorto)+"&owner=exclude&output=xml&count="+str(max_count)
    elif report_type == '10-Q':
        link = "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+str(cik)+"&type=10-Q&dateb="+str(priorto)+"&owner=exclude&output=xml&count="+str(max_count)
    else:
        return None
    data = requests.get(link).text
    soup = Soup(data, "lxml")
    links = []
    # If the link is .htm convert it to .html
    for link in soup.find_all('filinghref'):
        # convert http://*-index.htm to http://*.txt
        url = link.string
        if link.string.split(".")[len(link.string.split("."))-1] == "htm":
            url += "l"
        required_url = url.replace('-index.html', '')
        txtdoc = required_url + ".txt"
        #docname = txtdoc.split("/")[-1]
        links.append(txtdoc)

    links = links[:int(count)]
    return links


def clean_soup(link):
    data = requests.get(link).text
    soup = Soup(data, "lxml")
    blacklist = ["script", "style"]
    attrlist = ["class", "id", "name", "style", 'cellpadding', 'cellspacing']
    skiptags = ['font', 'a', 'b', 'i', 'u']

    for tag in soup.findAll():
        if tag.name.lower() in blacklist:
            # blacklisted tags are removed in their entirety
            tag.extract()

        if tag.name.lower() in skiptags:
            tag.replaceWithChildren()

        for attribute in attrlist:
            del tag[attribute]
    return soup

def normtxt(txt):
    return unicodedata.normalize("NFKD",txt)
def extract_section_10k(soup, section='1a', section_end='1b'):
    search_next = ["p", "div", "table"]
    # loop over all tables
    items = soup.find_all(("table", "div"))
    myitem = None
    search_txt = ['item '+ section ]
    for i, item in enumerate(items):
        txt = normtxt(item.get_text())
        # this is to avoid long sentences or tables that contain the item
        if len(txt.split()) > 5:
            continue
        if any([w in txt.lower() for w in search_txt]):
            myitem = item
    if myitem is None:
        # print("section not found, returned None")
        return None
    lines = ""
    des = myitem.find_next(search_next)
    search_txt = [ 'item '+section_end ]
    while not des is None:
        des = des.find_next(search_next)
        if des is None:
            raise ValueError("end section not properly found")
        if any([w in normtxt(des.get_text()).lower() for w in search_txt]):
            break
        elif des is not None:
            if len(des.get_text().split()) > 2 and '|' not in normtxt(des.get_text()):
                # need to get rid of escape characters
                lines += normtxt(" "+des.get_text())
        else:
            continue
    return lines[1:]


def extract_section_10q(soup, section='1a', section_end='2.'):
    search_next = ["p", "div", "table"]
    # loop over all tables
    items = soup.find_all(("table", "div"))
    myitem = None
    search_txt = ['item '+ section ]
    for i, item in enumerate(items):
        txt = normtxt(item.get_text())
        # this is to avoid long sentences or tables that contain the item
        if len(txt.split()) > 5:
            continue
        if any([w in txt.lower() for w in search_txt]):
            myitem = item
    if myitem is None:
        # print("section not found, returned None")
        return None
    lines = ""
    des = myitem.find_next(search_next)
    search_txt = [ 'item '+section_end ]
    while not des is None:
        des = des.find_next(search_next)
        if des is None:
            raise ValueError("end section not properly found")
        if any([w in normtxt(des.get_text()).lower() for w in search_txt]):
            break
        elif des is not None:
            if len(des.get_text().split()) > 2 and '|' not in normtxt(des.get_text()):
                # need to get rid of escape characters
                lines += normtxt(" "+des.get_text())
        else:
            continue
    return lines[1:]




def acceptance_date(soup):
    i=soup.get_text().index('.txt : ')
    return soup.get_text()[i+7:i+15]


def get_rf_10q(cik, company,max_n,date):
    report_type = '10-Q'
    mylinks = get_links(cik, date, str(max_n),report_type)
    date = int(date[:4])
    dates = range(date, 1000, -1)
    result_txt = []
    i=0
    for link in mylinks:
        soup = clean_soup(link)
        section = extract_section_10q(soup)
        accp_date = acceptance_date(soup)
        filename = company+"_10q_"+accp_date+"_RiskFactor"+".txt"
        if section is None:
            continue
        print("writing "+filename+"...")
        with open(filename,"w") as f:
            f.write(section)
        i+=1


def get_rf_10k(cik, company,max_n,date):
    report_type = '10-K'
    mylinks = get_links(cik, date, str(max_n),report_type)
    date = int(date[:4])
    dates = range(date, 1000, -1)
    result_txt = []
    i=0
    for link in mylinks:
        soup = clean_soup(link)
        section = extract_section_10k(soup)
        accp_date = acceptance_date(soup)
        filename = company+"_10k_"+accp_date+"_RiskFactor"+".txt"
        if section is None:
            continue
        print("writing "+filename+"...")
        with open(filename,"w") as f:
            f.write(section)
        i+=1
