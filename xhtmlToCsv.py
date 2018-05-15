#Name:    Abhimanyu Kumawat
#Class:   CS-288 (02)
#Date:    May 4th 2018
#Version: Final V2.

import os
import sys
import csv
import mysql.connector
import xml.dom.minidom 

file=(sys.argv[1])										#Read the argument and parse it to a document variable

city=sys.argv[2]											#set city
stateString=sys.argv[1]										#strip state
printState=stateString[20:22]									#set state

document = xml.dom.minidom.parse(sys.argv[1])						#Parses argument using minidom

elements = document.getElementsByTagName('body')[0];					#all elements tag addresses
main=elements.getElementsByTagName('main')[0];						#all main tag addresses			
div=main.getElementsByTagName('div')[1];							#all div tag addresses under first child
tbody=div.getElementsByTagName("table")[0];						#table body tags under table
td=tbody.getElementsByTagName("td")[0];							#table data inside of table body tag

if printState == "PA":
	weather=(div.getElementsByTagName("h4")[1].firstChild.nodeValue) 		#PA WEATHER
else:
	weather=(div.getElementsByTagName("h4")[2].firstChild.nodeValue) 		#OTHER STATES WEATHER
print(weather)

temperature=(div.getElementsByTagName("h1")[0].firstChild.nodeValue)[0:2]	#Temperature data in Fahrenhiet is [0] Celcius is [3]
humidity=(tbody.getElementsByTagName("td")[1].firstChild.nodeValue)[0:2]	#Humidity data extracted

mySet = set('1234567890.')
pre=(tbody.getElementsByTagName("td")[5].firstChild.nodeValue).strip()[0:5]
pressure = ''.join(filter(mySet.__contains__, pre))
print(pressure)

#Writes extracted Data to a CSV file
with open("output.csv", "a") as csv_file:
	csv_app = csv.writer(csv_file)
	csv_app.writerow([printState, city, weather, temperature, humidity, pressure])

try:   

    mydb = mysql.connector.connect(host='localhost', user='abhi', password='Demo_pw9', database='myDB')
    cursor = mydb.cursor()
    
    querry = """INSERT INTO myDB.tableWeather(state, city, weather, temperature, humidity, pressure) VALUES (%s,%s,%s,%s,%s,%s) on 	DUPLICATE KEY UPDATE weather=%s, temperature=%s, humidity=%s, pressure=%s"""
  
    cursor.execute(querry, (printState, city, weather, temperature, humidity, pressure, weather, temperature, humidity, pressure))
    mydb.commit()
    
    cursor.close()
except mysql.connector.Error as err:
    print(err)
finally:
    mydb.close()

os.remove(file)	#Removes file once done adding data to csv



