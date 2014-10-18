

import sqlite3

def main():

	CONN = sqlite3.connect("ubermelon.db")
	DB = CONN.cursor()

	f = open("customers.csv")

	header = f.readline().rstrip().split(',')

	for line in f:
		data = line.rstrip().split(',')
		query = """INSERT into Customers VALUES (?, ?, ?, ?, ?, ?)"""
		DB.execute(query, (data[0], data[1], data[2], data[3], data[4], data[5]))
	CONN.commit()
	print "Successfully loaded data from customers into the Ubermelon database." 
	f = open("orders.csv")

	header = f.readline().rstrip().split(',')

	for line in f:
		line = line.decode('utf-8')
		data = line.rstrip().split(',')
		query = """INSERT into Orders VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
		print data
		DB.execute(query, (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13]))
	CONN.commit()
	print "Successfully loaded data from orders into Ubermelon database."


if __name__ == "__main__":
	main()
