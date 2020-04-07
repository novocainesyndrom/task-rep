from datetime import timedelta, datetime as dt
import random

next_date = (dt.today() + timedelta(days=1)).strftime("%d-%m-%Y %H:%M:%S.%f")
print(f'Date on next day = {next_date}', type(next_date))

date_string = "2020-02-03 09:18:36.000"
date_time = dt.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")
print(date_time, type(date_time))

for dobj in date_time.timetuple()[:6]:
	print(f"{dobj:02}")

print(random.sample([num for num in range(100,1000) if num%5==0],3))
alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
random.shuffle(alphabet)
rand_str = ''.join(alphabet[:10])
print(f"String of random chars \"{rand_str}\"")

rand_tickets = random.sample(range(1000000000, 9999999999), 100)
for ticket in range(1,3):
	print(f"Ticket {ticket} = {random.choice(rand_tickets)}")

def raise_excp(): 
	raise Exception

try:
	raise_excp()
except:
	print("Exception was raised")
finally:
	print('To be continued...')
