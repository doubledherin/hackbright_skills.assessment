"""
call.py - Telemarketing script that displays the next name 
          and phone number of a Customer to call.

          This script is used to drive promotions for 
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""

import sqlite3
from datetime import date 


CONN = None
DB = None

# Class definition to store our customer data
class Customer(object):
	def __init__(self, id=None, first=None, last=None, telephone=None):
		self.id = id
		self.first = first
		self.last = last
		self.telephone = telephone
		pass

	def __str__(self):
		output = " Name: %s, %s\n" % (self.last, self.first)
		output += "Phone: %s" % self.telephone

		return output

# Connect to the Database
def connect_to_db():
	global DB, CONN
	CONN = sqlite3.connect('ubermelon.db')

	DB = CONN.cursor()


# Retrieve the next uncontacted customer record from the database.
# Return the data in a Customer class object.
#
# Remember: Our telemarketers should only be calling customers
#           who have placed orders of 20 melons or more.
def get_next_customer():
	# query = """SELECT * FROM Customers WHERE called='' LIMIT 1"""
	query = """SELECT * FROM Customers 
	           JOIN Orders ON Customers.customer_id=Orders.customer_id 
	           WHERE (called='') AND (num_watermelons > 20)
	           LIMIT 1
	        """	
	DB.execute(query)
	row = DB.fetchone()
	id, first, last, telephone = row[0], row[1], row[2], row[4]
	c = Customer(id, first, last, telephone)
	print "debug", c.id
	return c


def display_next_to_call(customer):
	print "---------------------"
	print "Next Customer to call"
	print "---------------------\n"
	print customer, "id:", customer.id
	print "%s %s: %s" % (customer.first, customer.last, customer.telephone)
	print "\n"


# Update the "last called" column for the customer
#   in the database.
def update_customer_called(customer):
	today = date.today().strftime("%m/%d/%y")
	print today, customer
	query = """UPDATE Customers
			   SET called = ?
	           WHERE customer_id = ?
	           """
	DB.execute(query, (today, customer.id,))
	CONN.commit()
	print "%s %s record updated in Ubermelon database as called on today's date." % (customer.first, customer.last)

def main():
	connect_to_db()

	done = False

	while not done:
		customer = get_next_customer()
		display_next_to_call(customer)

		print "Mark this customer as called?"
		user_answer = raw_input('(y/n) > ')

		if user_answer.lower() == 'y':
			update_customer_called(customer)
		else:
			done = True


if __name__ == '__main__':
	main()