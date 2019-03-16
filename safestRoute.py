from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


""" --- We have commented out the selenium code so as to avoid any errors as we haven't yet linked it with google maps---"""

driver = webdriver.Chrome('C:\\Users\\chromedriver.exe')

##driver.get("https://www.google.com/maps/dir///@27.9112189,78.0804477,15z/data=!4m2!4m1!3e0")


time.sleep(5)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""----Reading crime values ----"""


dataset1=pd.read_csv('crime.csv')
X=dataset1.drop('Crime value',axis=1)
y=dataset1['Crime value']


""" ---Training our ML Model---- """
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X_train,y_train)





# driver.find_element_by_id('sb_ifc51').send_keys('Aligarh')
"""driver.find_element_by_xpath('//*[@id="sb_ifc50"]/input').send_keys('ISM Dhanbad')
driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input').send_keys('Shree complex dhanbad')
driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input').send_keys(Keys.RETURN)
# driver.fifind_element_by_class_name('tactile-searchbox-input').send_keys('Aligarh')"""
# driver.find_element_by_class_name('tactile-searchbox-input').send_keys('Aligarh')


time.sleep(5)


##road_xpath = '//h1[@class="section-directions-trip-title"]/span'

##roads = driver.find_elements_by_xpath(road_xpath)


list_of_via_roads_final1 = [ ]

""" --- Checking the name of roads in our roads.csv file to predict their respective crime values---"""
for road in roads:
    road_name = road.text
    print(road_name)
    check_for_and="and" in road_name
    check_for_slash="/" in road_name
    if check_for_and==True:
        
        road_name_final1 = road_name.split('and')[1].strip()
        list_of_via_roads_final1.append(road_name_final1)
        
    elif check_for_slash==True:
        
        road_name_final1 = road_name.split('/')[1].strip()
        list_of_via_roads_final1.append(road_name_final1)

    else:
        road_name_final1 = road_name
        list_of_via_roads_final1.append(road_name_final1)




print(list_of_via_roads_final1)

b=0
c=0
A=[None]*5
for i in range(len(list_of_via_roads_final1)):
    # name_of_road = list_of_via_roads_final1[i]
    csv_file = csv.reader(open('roads.csv', 'r', encoding='utf-8'))
    #print(name_of_road)

    for row in csv_file:
        if list_of_via_roads_final1[i] == row[0]:
            #print(row)
            row.pop(0)
            print(row)
            #print(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            A[i]=regressor.predict([[row[0],row[1],row[2],row[3],row[4],row[5],row[6]]])
                
            print(A[i])
            b=b+1


m=A[0]
for i in range(b):
    if m>A[i]:
        m=A[i]
        c=i
        
print(m)
print(c)


##time.sleep(3)

"""clicking_path = f'//*[@id="section-directions-trip-{c}"]/div[2]'
driver.find_element_by_xpath(clicking_path).click()
try:
    driver.find_element_by_xpath(clicking_path).click()
except:
    pass"""

