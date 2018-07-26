import requests
from prettytable import PrettyTable
from bs4 import BeautifulSoup
import webbrowser 
url='http://dspace.amritanet.edu:8080/xmlui/handle/123456789/150'
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
ul=soup.findAll('ul',xmlns='http://di.tamu.edu/DRI/1.0/')
#print(ul[1])
li=ul[1].findAll('li')
#print(len(li)
i=1
t=PrettyTable(['S.no','Semester'])
#print(t)

for i in range(len(li)):
    t.add_row([i+1,li[i].span.text])
t.align='l'
print(t)
inp=int(input("enter the semester no: "))
if(inp<=6):
 url='http://dspace.amritanet.edu:8080'+li[inp-1].a['href']
 #print(url2)
 page2=requests.get(url)
 soup2=BeautifulSoup(page2.content,'html.parser')
 ul2=soup2.findAll('ul')
 li2=ul2[3].findAll('li')
 #print(len(li2))
 #print(ul2[3])
 t2= PrettyTable(['S.no','Type'])
 for j in range(len(li2)):
    t2.add_row([j+1,li2[j].span.text])
 t2.align='l'
 print(t2)
 inp=int(input('Enter the category no: '))
 str=li2[inp-1].a['href']
 #print(str)
 url='http://dspace.amritanet.edu:8080'+str
 page=requests.get(url)
 soup=BeautifulSoup(page.content,'html.parser')
 ul=soup.findAll('ul')
 li=ul[2].findAll('li')
 #print(len(li))
 i=0
 t3=PrettyTable(['S.no','Type'])
 for i in range(len(li)):
    t3.add_row([i+1,li[i].a.text])
 t3.align='l'
 print(t3)
 inp=int(input("Enter the category: "))
 url='http://dspace.amritanet.edu:8080'+li[inp-1].a['href']
 #print(url)
 page=requests.get(url)
 soup=BeautifulSoup(page.content,'html.parser')
 div = soup.findAll('div',class_='file-list')
 div1=div[0].findAll('div',class_='file-wrapper clearfix')
 #print(div1[0])
 t4=PrettyTable(['S.No','Title'])
 i=0
 for i in range(len(div1)):
    span=div1[i].findAll('span')
    span1=span[1]
    t4.add_row([i+1,span1.text])
 t4.align='l'
 print(t4)


 inp=int(input("Enter the choice: "))
 url='http://dspace.amritanet.edu:8080'+div1[inp-1].a['href']
 #print(url)
 webbrowser.open_new(url)
else:
    url='http://dspace.amritanet.edu:8080'+li[inp-1].a['href']
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    div=soup.findAll('div',class_='clearfix')
    ul=div[1].findAll('ul')
    li=ul[1].findAll('li')
    #print(len(li))
    i=0
    t2=PrettyTable(['S.no','Type'])
    for i in range(len(li)):
        t2.add_row([i+1,li[i].span.text])
    t2.align='l'   
    print(t2)
    inp=int(input("Enter your choice: "))
    url='http://dspace.amritanet.edu:8080'+li[inp-1].a['href']
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    ul=soup.findAll('ul')
    li=ul[2].findAll('li')
    #print(len(li))
    t3=PrettyTable(['S.No','Name'])
    i=0
    for i in range(len(li)):
      t3.add_row([i+1,li[i].a.text])
    t3.align='l'
    print(t3)
    inp=int(input("Enter your Choice: "))
    url='http://dspace.amritanet.edu:8080'+li[inp-1].a['href']
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    div=soup.findAll('div',class_='file-list')
    div1=div[0].findAll('div',class_='file-wrapper clearfix')
    div2=div1[0].findAll('div')
    #print(len(div2))
    i=0
    t4=PrettyTable(['S.No','Name'])
    for i in range(len(div1)):
     div2=div1[i].findAll('div')
     span=div2[2].findAll('span')
     span=span[1]
     t4.add_row([i+1,span.text])
    t4.align='l'
    print(t4)
    inp=int(input("Enter your choice: "))
    
    url='http://dspace.amritanet.edu:8080'+div1[2].a['href']
    webbrowser.open_new(url)





    
