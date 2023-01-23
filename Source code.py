from bs4 import BeautifulSoup
import requests 
import pandas as pd

jumia= requests.get('https://www.jumia.com.ng/phones-tablets/')
jumia.content

name_info =[]
price_info =[]
Rating_info =[]

for page in range (1,51):
  url ="https://www.jumia.com.ng/phones-tablets/"
  furl= requests.get(url)
  jsoup= BeautifulSoup(furl.content ,'html.parser')
  products= jsoup.find_all('div', class_ ='info')

  for product in products:

    Name = product.find('h3',class_ ='name').text.replace('/n','')
    Price=product.find('div',class_ ='prc').text.replace('/n','')

    try:
      Rating=product.find ('div',class_='stars_s').text.replace('/n','')
    except:
      Rating='none'

      name_info.append(Name)
      price_info.append(Price)
      Rating_info.append(Rating)

      print(name_info,price_info,Rating_info)

dict ={ 'Product Name':name_info ,'Price':price_info ,'Rating': Rating_info}
df =pd.DataFrame(dict)
df

df.to_csv('products _from_jumia.csv',index= False ,encoding ='utf-8')

        
