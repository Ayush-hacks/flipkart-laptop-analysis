import pandas as pd
import numpy as np
df = pd.read_csv("data1.csv")

df["Reviews"]=df["Reviews"].astype(int)
df["Brand"]=df["Name"].apply(lambda x:x.split()[0])
df["popularity"] = df["Ratings"]+df["Reviews"]
df = df[["Name","Brand","popularity","Ratings","Reviews"]]
df["Ratings"]=pd.to_numeric(df["Ratings"],errors="coerce")
df["Reviews"] = pd.to_numeric(df["Reviews"],errors="coerce")
df=df.dropna()
df["Ratings"] = df["Ratings"].apply(lambda x:x/1000 if x>10 else x)
df=df[(df["Ratings"]>=0)&(df["Ratings"]<=5)]
# insights part

df["score"] = df["Ratings"]*df["Reviews"]
df = df.sort_values("score",ascending=False)

brand_counts=df["Brand"].value_counts()

brand_reviews = df.groupby("Brand")["Reviews"].sum().sort_values(ascending=False)
brand_ratings = df.groupby("Brand")["Ratings"].mean().sort_values(ascending=False)
final_analysis = df.groupby("Brand").agg({
    "Ratings":["mean","max"],
    "Reviews":["sum","max"]
})



print("--Brand count--")
print(brand_counts)
print("--Brand reviews--")
print(brand_reviews)
print("--Brand ratings--")
print(brand_ratings)
print("--Final analysis--")
print(final_analysis)

df.to_csv("cleaned_data.csv",index=False)

#Visualisation part
# Brand distribution graph
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.figure()
sns.countplot(x="Brand", data=df)
plt.title("Number of Laptops per Brand")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("brand_distribution.png")
plt.show()



#Average ratings per brand graph

avg_ratings = df.groupby("Brand")["Ratings"].mean().reset_index()

plt.figure()
sns.barplot(x="Brand", y="Ratings", data=avg_ratings)
plt.title("Average Rating per Brand")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("avg_ratings.png")
plt.show()
#Reviews per brand graph
avg_ratings = df.groupby("Brand")["Ratings"].mean().reset_index()

plt.figure()
sns.barplot(x="Brand", y="Ratings", data=avg_ratings)
plt.title("Average Rating per Brand")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("avg_ratings.png")
plt.show()


# top 10 score-based rating graph

reviews_sum = df.groupby("Brand")["Reviews"].sum().reset_index()

plt.figure()
sns.barplot(x="Brand", y="Reviews", data=reviews_sum)
plt.title("Total Reviews per Brand")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reviews.png")
plt.show()















