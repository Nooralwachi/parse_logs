from collections import defaultdict
from datetime import datetime
def parse_logs(filename):
	logs=defaultdict(list)
	users = defaultdict(int)
	
	with open(filename, 'r') as file:
		for line in file:
			words = line.split()
			if len(words) >2: 
				current = ('-').join([words[0],words[1],words[2]])
				current_dt = datetime.strptime(current, "%b-%d-%H:%M:%S")
				#print(current_dt)

			if len(words) >8 :
				typ = words[4] # sshd[7758]:
				error = words[5] # Failed
				username = words[8] # testuser
				timestamp = ('-').join([words[0],words[1],words[2]])
				dt_object = datetime.strptime(timestamp, "%b-%d-%H:%M:%S")
				if typ.startswith('sshd') and error == 'Failed':
					logs[username].append(dt_object)
	for username, count in logs.items():
		for time in count:
			if abs((time- current_dt).days) < 4.5:
				users[username]+=1
	for user, count in users.items():
		if count >=3:
			print(user)			

parse_logs('auth.log')
