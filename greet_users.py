def greet_users(names):
	"""向列表的每位用户都发出简单的问候"""
	for name in names:
		msg = 'Hello, ' + name.title() + '!'
		print(msg)
		
usernames = ['hannah','ty','margot']
greet_users(usernames)
