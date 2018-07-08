#question 1
import pandas as pd
tab={"name":["Shubham","Prattay","Ankit"],"age":[12,23,34],"mail_id":["x.com","y.com","z.com"]}
df=pd.DataFrame(tab)
print(df)
print("\n")
tab={"name":["Shubham","Prattay","Ankit","Ankita"],"age":[12,23,34,45],"mail_id":["x.com","y.com","z.com","a.com"]}
d=pd.DataFrame(tab)
print(d)


#question2
import pandas as pd
df=pd.read_csv("weather.csv")
print("whole data")
print(df)
print("\n")
print("first five data:")
print("\n")
print(df.head())
print("first ten data:")
print("\n")
print(df.head(10))
print("statistics:")
print("\n")
print(df.describe())
print("last five data:")
print("\n")
print(df.tail())
st=df["MinTemp"]
print("stats")
print("\n")
print(st.describe())
