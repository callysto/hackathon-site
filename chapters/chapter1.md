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

This is a self-assessment tool. Have a look at the code snippets below and identify ones you could’ve written. If none of it looks familiar, that’s ok!

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

If you self-assessed at `5` or lower, consider taking the Curiosity (beginner) track challenges.

If you self-assessed at  `6` or higher, consider taking the Amal (advanced) track challenges.

</exercise>

<exercise id="2" title="How are your data science skills?">

# Levels of Data Science Comfort

This is a self-assessment tool. Have a look at the code snippets below and identify ones you could’ve written. If none of it looks familiar, that’s ok!

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

4. Plotting
```python
import plotly.express as px
px.bar(df, x='Year', y='Number of Missions', title='Number of Missions per Year')
```

5. More Statistics
```python
df.groupby(by='Year')['Year'].count()
df.agg(['min', 'max'])
```

6. Merging Data
```python
df.append(df2, ignore_index=True)
new_df = pd.concat([df, df2], axis=1)
```


If you self-assessed at `1`, consider taking the Curiosity (beginner) track challenges.

If you self-assessed at  `2` or higher, consider taking the Amal (advanced) track challenges.


</exercise>

<exercise id="3" title="Next Steps">

You'll need to choose either the Curiosity (beginner) or Amal (advanced) track of challenges.

Why do we call them [Curiosity](https://en.wikipedia.org/wiki/Curiosity_(rover)) and [Amal](https://en.wikipedia.org/wiki/Emirates_Mars_Mission)?

In Chapter 2 of our pre-hackathon content, we'll walk you through an imaginary scenario that involves applying data science. Along the way, you'll get introduced to some of the data science tools and concepts you'll be using during hackathon.

</exercise>