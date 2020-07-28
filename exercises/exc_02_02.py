import pandas as pd #importing the pandas library
url = 'https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/tas/1901-2016/53.544388$cckp$-113.490929/53.544388$cckp$-113.490929'
weather = pd.read_csv(url) #the data from the url is read into the weather variable

june = weather[weather[' Statistics']==' Jun Average'] #filter data for June temperatures and assign to june variable
print("June",june.mean()) #calculate and print the average temperature value for June

august = weather[weather[' Statistics']==' Aug Average'] #filter data for August temperatures and assign to august variable
print("August",august.mean()) #calculate and print the average temperature value for August
