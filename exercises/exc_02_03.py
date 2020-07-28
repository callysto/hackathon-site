import pandas as pd #importing the pandas library
precipitation_url = 'https://climateknowledgeportal.worldbank.org/api/data/get-download-data/historical/pr/1901-2016/53.544388$cckp$-113.490929/53.544388$cckp$-113.490929'
precipitation = pd.read_csv(precipitation_url) #the data from the url is read into the precipitation variable

june = precipitation[precipitation[' Statistics']==' Jun Average'] #filter data for June precipitation and assign to june variable
print("June",june.mean()) #calculate and print the average precipitation value for June

august = precipitation[precipitation[' Statistics']==' Aug Average'] #filter data for August precipitation and assign to august variable
print("August",august.mean()) #calculate and print the average precipitation value for August
