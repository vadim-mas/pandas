import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 Сколько всего приложений с категорией ('Category') 'BUSINESS'?
temp1 = df['Category'].value_counts()
print(temp1['BUSINESS'])
# 2 Чему равно соотношение количества приложений для подростков ('Teen') и для детей старше 10 ('Everyone 10+')?
# Ответ запиши с точностью до сотых.
temp2 = df['Content Rating'].value_counts()
teen = temp2['Teen']
everyone10 = temp2['Everyone 10+']
print(round(teen / everyone10, 2))
# 3.1 Чему равен средний рейтинг ('Rating') платных ('Paid') приложений? 
# Ответ запиши с точностью до сотых.
temp3 = df[df['Type'] == 'Paid']
pr = round(temp3['Rating'].mean(), 2)
print(round(temp3['Rating'].mean(), 2))
# 3.2 На сколько средний рейтинг ('Rating') бесплатных ('Free') приложений меньше среднего рейтинга платных ('Paid')?
# Ответ запиши с точностью до сотых.
temp4 = df[df['Type'] == 'Free']
fr = round(temp4['Rating'].mean(), 2)
print(round(pr - fr, 2))
# 4 Чему равен минимальный и максимальный размер ('Size') приложений в категории ('Category') 'COMICS'?
# Запиши ответы с точностью до сотых.
print(round(df.groupby(by='Category')['Size'].agg([max, min]), 2))
# Бонус 1. Сколько приложений с рейтингом ('Rating') строго больше 4.5 в категории ('Category') 'FINANCE'?

# Бонус 2. Чему равно соотношение бесплатных ('Free') и платных ('Paid') игр с рейтингом ('Rating') больше 4.9?

