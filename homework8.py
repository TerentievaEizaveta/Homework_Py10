#Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. 
#Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).
import pandas as pd
df = pd.read_csv('C:\\Users\\User\\Desktop\\HW\\Homework_Py8\\california_housing_train.csv')
print(df.head())
print(round(df[df['population'] <= 500]['median_house_value'].mean(), 2))

#Задача 42: Узнать какая максимальная households в зоне минимального значения population.
print(df[df['population'] == df['population'].min()]['households'].max())