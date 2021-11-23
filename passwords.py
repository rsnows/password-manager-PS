import sqlite3

MASTER_PASSWORD = "thisisthepassword"

project_password = input("Enter your master password: ")
if project_password != MASTER_PASSWORD:
	print("Invalid password! Leaving...")
	exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
	service TEXT NOT NULL,
	username TEXT NOT NULL,
	password TEXT NOT NULL
);
''')

def menu():
	print("**************************")
	print("* i: Insert new password *")
	print("* l: List saved services *")
	print("* r: Recover a password  *")
	print("* e: Exit                *")
	print("**************************")

def get_password(service):
	cursor.execute(f'''
	SELECT username, password FROM users
	WHERE service = '{service}'
	''')

	if cursor.rowcount == 0:
		print("Unregistered service. Use l to see all registered services.")
	else:
		for user in cursor.fetchall():
			print(user)

def insert_password(service, username, password):
	cursor.execute(f'''
	INSERT INTO users (service, username, password)
	VALUES ('{service}', '{username}', '{password}')
	''')
	conn.commit()

def show_services():
	cursor.execute('''
	SELECT service FROM users;
	''')
	for service in cursor.fetchall():
		print(service)

while True:
	menu()
	op = input("What do you want to do? ")
	if op not in ['i', 'l', 'r', 'e']:
		print("Invalid option")
		continue

	if op == 'e':
		break

	if op == 's':
		break

	if op == 'i':
		service = input("What is the name of the service? ")
		username = input("What is the username? ")
		password = input("What is the password? ")
		insert_password(service, username, password)

	if op == 'l':
		show_services()

	if op == 'r':
		service = input("What service do you need the password for? ")
		get_password(service)

conn.close()
