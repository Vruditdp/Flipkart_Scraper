from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "_13oc-S"})
# print(len(containers))

# print(soup.prettify(containers[0]))
container = containers[0]
# print(container.div.img["alt"])
# price = container.findAll("div",{"class": "_30jeq3 _1_WHN1"})
# print(price[0].text.lstrip("₹"))

# rating=container.findAll("div",{"class":"_3LWZlK"})
# print(rating[0].text.strip())

filename = "product.csv"
f = open(filename,"w")

headers="Product Number,Product Name,Price,Ratings\n\n"
f.write(headers)
i=1
for container in containers:
    product_name=container.div.img["alt"]

    price_container=container.findAll("div", {"class":"_30jeq3 _1_WHN1"})
    price1=price_container[0].text.lstrip('₹')
    price= "Rs. " + price1
    

    rating_container=container.findAll("div",{"class": "_3LWZlK"})
    rating=rating_container[0].text.strip()
    # print('\n\n',i)
    # print('Product Name:',product_name)
    # print('Price:',price)
    # print('Rating:',rating)
    
    
    print(str(i) + " , " + product_name.replace(","," |") + " , " + price.replace(",","") + " , " + rating + "\n")
    f.write(str(i) + " , " + product_name.replace(","," |") + " , " + price.replace(",","") + " , " + rating + "\n")
    
    i=i+1

f.close()    
