__author__ = 'Dell-Pc'


from bs4 import BeautifulSoup
import requests
import xlwt



def getSoupObject(url="http://www.list.lk/search/home.html"):

    # url="http://www.list.lk/search/home.html"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")
    return  soup


# divCont= soup.findAll("div",{"class":'list_l_box'})

def writeToExcelSheet(lst):
    wb=xlwt.Workbook()
    ws=wb.add_sheet('companies')

    ws.write(0,0,"Company")
    ws.write(0,1,"Telephone")

    col=2

    for item in lst:
        ws.write(col,0,item[0])
        ws.write(col,1,item[1])
        col+=1

    wb.save("F:/Projects/python/Beautiful_soup/company.xlsx")








def getDataFromPage(soupObj):

    lst=[]

    divCont= soupObj.findAll("div",{"class":'list_l_box'})

    for item in divCont:
        itemList=item.contents

        if itemList[1].findAll('img',{"alt":"No image"}) !=[]:
            continue

        else:
            companyDataList=itemList[3].contents

            if companyDataList[5].findAll("span",{"itemprop":"telephone"})!=[]:

                companyName=companyDataList[1].text
                companyTele=companyDataList[5].findAll("span",{"itemprop":"telephone"})[0].text
                temp=[]
                temp.append(companyName)
                temp.append(companyTele)
                # print companyName,companyTele

                lst.append(temp)
    return lst


def getData(numOfDetails,initialURL):

    companyList=[]
    j=1

    while len(companyList) <= numOfDetails:


        # for i in range(pageSize):
        temp=[]
        try:
            temp=getDataFromPage(getSoupObject(initialURL+str(j)))

        # else:
        #     # initialURL+str(i+j)
        #     temp=getDataFromPage(getSoupObject( initialURL+str(j)))

        except:
            print "Network Error"

        else:
            for item in temp:

                companyList.append(item)

            j+=1



    return companyList

temp=getData(100,"http://www.list.lk/search/home.html")

writeToExcelSheet(temp)