import psycopg2
import sys
import os

try:
	con = psycopg2.connect(database='quiz_bot')
	cur = con.cursor()

except psycopg2.DatabaseError, e:
	print 'Error %s' % e
	sys.exit(1)

#re-create tables if they exist so need to drop
cur.execute("DROP TABLE IF EXISTS question;")
cur.execute("DROP TABLE IF EXISTS category;")
cur.execute("DROP TABLE IF EXISTS sub_category;")
cur.execute("DROP TABLE IF EXISTS topic;")

#create tables
cur.execute(
	"CREATE TABLE question(id INT PRIMARY KEY NOT NULL, ask TEXT, \
	a TEXT, b TEXT, c TEXT, d TEXT, correct_answer TEXT, \
	correct INT, category_id INT, sub_cat_id INT, topic_id INT);")
cur.execute(
	"CREATE TABLE category(id INT PRIMARY KEY NOT NULL, name VARCHAR(50));")
cur.execute(
	"CREATE TABLE sub_category(id INT PRIMARY KEY NOT NULL, subject VARCHAR(50), \
	cat_id INT);")
cur.execute(
	"CREATE TABLE topic(id INT PRIMARY KEY NOT NULL, topic_n VARCHAR(50), \
	sc_id INT);")

#category and sub-category arrays
cat = []
sub = []
top = []

cat.append('math')
cat.append('science')
sub.append('add')
sub.append('sub')
sub.append('bio')
top.append('numbers')

#sequence for ids
# seq = "CREATE SEQUENCE identity START 1;"
#test inserts

insert_cat = "INSERT INTO category (id, name) VALUES (1, 'math');"
insert_sub = "INSERT INTO sub_category (id, subject, cat_id) VALUES (1, \
	'add', (SELECT id FROM category WHERE name = 'math'))"
insert_top = "INSERT INTO topic (id, topic_n, sc_id) VALUES \
	(1, 'numbers', (SELECT id FROM sub_category WHERE subject = 'add'));"
insert = "INSERT INTO question (id, ask, a, b, c, d, correct_answer, correct,\
	category_id, sub_cat_id, topic_id) VALUES \
	(1, 'What is 1+1?', '1', '2', '3', '4', '2', 0, \
	(SELECT id FROM category WHERE name = '%s'), \
	(SELECT id FROM sub_category WHERE subject = '%s'),\
	(SELECT id FROM topic WHERE topic_n = '%s'));" \
	%(cat[0], sub[0], top[0])
cur.execute(insert_cat)
cur.execute(insert_sub)
cur.execute(insert)

# count = 0
# f = open("/home/cjnitta/ecs165a/EIA_CO2_Electricity_2015.csv", 'rb')
# msnData = []
# descriptionData = []
# columnData = []
# unitData = []

# reader = csv.reader(f)
# #gets the column names
# fields = next(reader)
# #gets first set of data to initialize 
# first = next(reader)
# msnData.append(first[0])
# columnData.append(first[3])
# descriptionData.append(first[4])
# unitData.append(first[5])
# if(first[2] == "Not Available"):
# 	queryString = "INSERT INTO electric_data VALUES (%s, %s, %s);" \
# 	%(first[3], first[1], "-1")
# 	cur.execute(queryString)
# else:
# 	queryString = "INSERT INTO electric_data VALUES (%s, %s, %s);" \
# 	%(first[3], first[1], first[2])
# 	cur.execute(queryString)

# for row in reader:
# 	if (row[0] != msnData[count]): 	
# 	#if msn does not exit in table yet
# 	#increment index of msn array for next check
# 		msnData.append(row[0])
# 		columnData.append(row[3])		
# 		descriptionData.append(row[4])
# 		unitData.append(row[5])
# 		count += 1	
# 	if(row[2] == "Not Available"):
# 		queryString = "INSERT INTO electric_data VALUES (%s, %s, %s);" \
# 		%(row[3], row[1], "-1")
# 		cur.execute(queryString)
# 	else:
# 		queryString = "INSERT INTO electric_data VALUES (%s, %s, %s);" \
# 		%(row[3], row[1], row[2])
# 		cur.execute(queryString)

# for i in range(len(msnData)):
# 	queryString = "INSERT INTO electric_misc VALUES (%s, '%s', '%s', '%s');" \
# 	%(columnData[i], msnData[i], descriptionData[i], unitData[i])
# 	cur.execute(queryString)	

# #insert transportation data
# count = 0
# f = open("/home/cjnitta/ecs165a/EIA_CO2_Transportation_2015.csv", 'rb')
# msnData = []
# descriptionData = []
# columnData = []
# unitData = []

# reader = csv.reader(f)
# #gets the column names
# fields = next(reader)
# #gets first set of data to initialize 
# first = next(reader)
# msnData.append(first[0])
# columnData.append(first[3])
# descriptionData.append(first[4])
# unitData.append(first[5])
# if(first[2] == "Not Available"):
# 	queryString = "INSERT INTO transport_data VALUES (%s, %s, %s);" \
# 	%(first[3], first[1], "-1")
# 	cur.execute(queryString)
# else:
# 	queryString = "INSERT INTO transport_data VALUES (%s, %s, %s);" \
# 	%(first[3], first[1], first[2])
# 	cur.execute(queryString)

# for row in reader:
# 	if (row[0] != msnData[count]): 	
# 	#if msn does not exit in table yet
# 	#increment index of msn array for next check
# 		msnData.append(row[0])
# 		columnData.append(row[3])		
# 		descriptionData.append(row[4])
# 		unitData.append(row[5])
# 		count += 1	
# 	if(row[2] == "Not Available"):
# 		queryString = "INSERT INTO transport_data VALUES (%s, %s, %s);" \
# 		%(row[3], row[1], "-1")
# 		cur.execute(queryString)
# 	else:
# 		queryString = "INSERT INTO transport_data VALUES (%s, %s, %s);" \
# 		%(row[3], row[1], row[2])
# 		cur.execute(queryString)

# for i in range(len(msnData)):
# 	queryString = "INSERT INTO transport_misc VALUES (%s, '%s', '%s', '%s');" \
# 	%(columnData[i], msnData[i], descriptionData[i], unitData[i])
# 	cur.execute(queryString)

# #insert mkwh data
# count = 0
# f = open("/home/cjnitta/ecs165a/EIA_MkWh_2015.csv", 'rb')
# msnData = []
# descriptionData = []
# columnData = []
# unitData = []

# reader = csv.reader(f)
# #gets the column names
# fields = next(reader)
# #gets first set of data to initialize 
# first = next(reader)
# msnData.append(first[0])
# columnData.append(first[3])
# descriptionData.append(first[4])
# unitData.append(first[5])
# if(first[2] == "Not Available"):
# 	queryString = "INSERT INTO mkwh_data VALUES (%s, %s, %s);" \
# 	%(first[3], first[1], "-1")
# 	cur.execute(queryString)
# else:
# 	queryString = "INSERT INTO mkwh_data VALUES (%s, %s, %s);" \
# 	%(first[3], first[1], first[2])
# 	cur.execute(queryString)

# for row in reader:
# 	if (row[0] != msnData[count]): 	
# 	#if msn does not exit in table yet
# 	#increment index of msn array for next check
# 		msnData.append(row[0])
# 		columnData.append(row[3])		
# 		descriptionData.append(row[4])
# 		unitData.append(row[5])
# 		count += 1	
# 	if(row[2] == "Not Available"):
# 		queryString = "INSERT INTO mkwh_data VALUES (%s, %s, %s);" \
# 		%(row[3], row[1], "-1")
# 		cur.execute(queryString)
# 	else:
# 		queryString = "INSERT INTO mkwh_data VALUES (%s, %s, %s);" \
# 		%(row[3], row[1], row[2])
# 		cur.execute(queryString)

# for i in range(len(msnData)):
# 	queryString = "INSERT INTO mkwh_misc VALUES (%s, '%s', '%s', '%s');" \
# 	%(columnData[i], msnData[i], descriptionData[i], unitData[i])
# 	cur.execute(queryString)

# ###################################################################################################
    
# cur.execute("DROP TABLE IF EXISTS day_table;")
# cur.execute("DROP TABLE IF EXISTS hh_table;")
# cur.execute("DROP TABLE IF EXISTS veh_table;")
# cur.execute("DROP TABLE IF EXISTS person_table;")

# #####Day Trip File
# queryString=""
# f = open("/home/cjnitta/ecs165a/DAYV2PUB.CSV", 'rb')
# reader = csv.reader(f)
# heading = next(reader)
# queryString = "CREATE TABLE day_table(%s INT, %s INT, %s INT, %s INT, %s INT, %s INT, %s INT, %s INT, %s FLOAT);" \
# %(heading[0], heading[1], heading[28], heading[38], heading[64], heading[83], heading[91], heading[93], heading[94])
# cur.execute(queryString)

# count = 0
# queryString=""
# for row in reader: 
# 	if count == 1500:
# 		count = 0
# 		cur.execute(queryString)
# 		queryString=""
# 	queryString+= "INSERT INTO day_table VALUES(%s, %s, '%s', %s, %s, %s, %s, %s, %s);" \
# 	%(row[0], row[1], row[28], row[38], row[64], row[83], row[91], row[93], row[94])
# 	count+= 1
# if queryString != "": 
# 	cur.execute(queryString)


# #####Household File
# queryString=""
# f = open("/home/cjnitta/ecs165a/HHV2PUB.CSV", 'rb')
# reader = csv.reader(f)
# heading = next(reader)
# queryString = "CREATE TABLE hh_table(%s INT, %s INT, %s INT, %s INT);" \
# %(heading[0], heading[3], heading[12], heading[15])
# cur.execute(queryString)

# count = 0
# queryString=""
# for row in reader: 
# 	if count == 1500:
# 		count = 0
# 		cur.execute(queryString)
# 		queryString=""
# 	queryString+= "INSERT INTO hh_table VALUES(%s, %s, %s, %s);" \
# 	%(row[0], row[3], row[12], row[15])
# 	count+= 1
# if queryString != "": 
# 	cur.execute(queryString)

# #####Person File
# queryString=""
# f = open("/home/cjnitta/ecs165a/PERV2PUB.CSV", 'rb')
# reader = csv.reader(f)
# heading = next(reader)
# queryString = "CREATE TABLE person_table(%s INT, %s INT, %s INT, %s INT, %s FLOAT);" \
# %(heading[0], heading[1], heading[7], heading[10], heading[100])
# cur.execute(queryString)

# count = 0
# queryString=""
# for row in reader: 
# 	if count == 1500:
# 		count = 0
# 		cur.execute(queryString)
# 		queryString=""
# 	queryString+= "INSERT INTO person_table VALUES(%s, %s, %s, %s, %s);" \
# 	%(row[0], row[1], row[7], row[10], row[100])
# 	count+= 1
# if queryString != "": 
# 	cur.execute(queryString)


# #####Vehicle File
# queryString=""
# f = open("/home/cjnitta/ecs165a/VEHV2PUB.CSV", 'rb')
# reader = csv.reader(f)
# heading = next(reader)
# queryString = "CREATE TABLE veh_table(%s INT, %s INT, %s INT, %s INT, %s FLOAT, %s INT, %s FLOAT, %s FLOAT, %s INT);" \
# %(heading[0], heading[2], heading[3], heading[6], heading[38], heading[51], heading[55], heading[57], heading[58])
# cur.execute(queryString)

# count = 0
# queryString=""
# for row in reader: 
# 	if count == 1500:
# 		count = 0
# 		cur.execute(queryString)
# 		queryString=""
# 	queryString+= "INSERT INTO veh_table VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);" \
# 	%(row[0], row[2], row[3], row[6], row[38], row[51], row[55], row[57], row[58])
# 	count+= 1
# if queryString != "": 
# 	cur.execute(queryString)
	
con.commit()
# #close file
# f.close()
# #close database connection
con.close()