__author__ = 'Dell-Pc'

from bs4 import BeautifulSoup
import requests
import xlwt

#open excel sheet to write

# wb=xlwt.Workbook()
# ws=wb.add_sheet('test1')



#set url for beatifulsoup to scrape data
url="http://www.list.lk/search/home.html"
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
#print soup.findAll("div",{"class":'list_l_box2'})

divCont= soup.findAll("div",{"class":'list_l_box2'})


ws.write(0,0,"company")
ws.write(0,1,"Telephone")
col=1

for item in divCont:
    # for elements in item.contents:
    #print item
    # print item.contents,len(item.contents)
    # temp=item.contents
    # break

    company=item.contents[1].text
    tele_html_list=item.contents[5].findAll("span",{"itemprop":"telephone"})

    if company==None or tele_html_list==[]:
        continue
    else:

        if col<9:
            # ws.write(col,0,company)
            # ws.write(col,1,tele_html_list[0].text)
            # col+=1
        print company,tele_html_list[0].text



# wb.save("F:/Projects/python/Beautiful_soup/test1.xls")

