---
title: '1. Pre-Hackathon: Before we start, assess yourself!'
description:
    'This section will help you evaluate your skills with Python and Data Science before you take part in the Callysto hackathon.'
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="How are your Python skills?">

# Levels of Python Comfort

This is a self-assessment tool. Have a look at the code snippets below and identify one you could’ve written. If none of it looks familiar, that’s ok!

0. I have never seen any Python before.

1. Basics
```python
print('Hello World')
```

2. Variables
```python
phrase = 'Hello World'
print(phrase)
```

3. Loops
```python
for x in range(5):
    print(x + 2)
```

4. Conditions
```python
for x in range(5):
    print(x)
    if x == 2:
        print('This is two')
```

5. Functions
```python
def multiply_by_three(x):
    y = x * 3
    return y
multiply_by_three(9)
```

6. Dictionaries
```python
mars_missions_2011 = {'Fobos-Grunt':'Roskosmos', 
                      'Yinghuo-1':'CNSA', 
                      'Curiosity':'NASA'}
for mission, agency in mars_missions_2011.items():
    print('The',mission,'mission was led by',agency)
```

If you self-assessed at `5` or less consider taking the Curiosity (beginner) track challenges during the hackathon. Why do we call it [Curiosity](https://en.wikipedia.org/wiki/Curiosity_(rover))?

If you self-assessed at  `6` or higher consider taking the Amal (advanced) track challenges during the hackathon. Why do we call it [Amal](https://en.wikipedia.org/wiki/Emirates_Mars_Mission)?

</exercise>

<exercise id="2" title="How are your data science skills?">

# Levels of Data Science Comfort

This is a self-assessment tool. Have a look at the code snippets below and identify one you could’ve written. If none of it looks familiar, that’s ok!

0. I have never seen any of this before.

1. Creating a Data Frame
```python
import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/List_of_missions_to_Mars')[0]
```

2. Basic Statistics
```python
df.describe()
df['Column 1'].mean()
```

2. Filtering Data
```python
df[df['Column 1']=='green']
```

3. Cleaning Data
```python
df['Year'] = df['Launch Date'].str.split(' ', expand=True)[2]
df.fillna(value=0, inplace=True)
```

4. More Statistics
```python
df.groupby(by='Year')['Year'].count()
df.agg(['min', 'max'])
```

5. Merging Data
```python
df.append(df2, ignore_index=True)
new_df = pd.concat([df, df2], axis=1)
```

6. Plotting
```python
import cufflinks as cf
cf.go_offline()
df.iplot(kind='barh', x='Column 1', y='Column 2', xTitle='Time', yTitle='Frequency', title='Frequency over Time')
```

If you self-assessed at `1` consider taking the Curiosity (beginner) track challenges during the hackathon. Why do we call it [Curiosity](https://en.wikipedia.org/wiki/Curiosity_(rover))?

If you self-assessed at  `2` or higher consider taking the Amal (advanced) track challenges during the hackathon. Why do we call it [Amal](https://en.wikipedia.org/wiki/Emirates_Mars_Mission)?


</exercise>

<exercise id="3" title="Next Steps">

On the day of the hackathon, you'll need to choose either the Curiosity (beginner) or Amal (advanced) track of challenges. We suggest writing down the number you selected during each self-assessment so you can remember which hackathon track will work best for you.

In Chapter 2 of our pre-hackathon content, we'll walk you through an imaginary scenario that involves applying data science. Along the way, you'll get introduced to some of the data science tools and concepts you'll be using during hackathon.

</exercise>