

from bs4 import BeautifulSoup
import pandas as pd

import requests
import time

data = []



headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.flipkart.com/"
}
query = "gaming+laptops"



for j in range(1,3):



    with open(f"htmls/htmlpage-{j}.html","r",encoding="utf-8") as f:
        content = f.read()
        soup = BeautifulSoup(content,"html.parser")
        names = soup.find_all("div",class_="RG5Slk")
        ratingsandviews = soup.find_all("div", class_="a7saXW")
        for name,rv in zip(names,ratingsandviews):
            name = name.text.strip()
            cleanname = name.split("-")[0].strip()




            if rv:
                text = rv.text
                parts = text.split("&")

                ratings = parts[0].strip()
                reviews = parts[1].strip()

                ratings = ratings.replace("Ratings","").strip().replace(",","")
                reviews = reviews.replace("Reviews","").strip().replace(",","")
            else:
                ratings=0
                reviews = 0

            data.append([cleanname,ratings,reviews])



df = pd.DataFrame(data,columns=["Name","Ratings","Reviews"])
df.to_csv("data1.csv",index=False)













