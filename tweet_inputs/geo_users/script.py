import json
import ast

fo = open('nairobi_users.txt', 'rb')
fn = open('new_geo_users.txt', 'rb')

nairobi_o = fo.readlines()
nairobi_n = fn.readlines()

print tweets[0]

users = []

for uo in nairobi_o:
	users.append(uo.rstrip('\n'))

for un in nairobi_n:
	users.append(un.rstrip('\n'))

print 'read users', len(users)
nusers = set(users)
print 'unique users ', len(nusers)

fw = open('unique_users.txt', 'wb')
for user in nusers:
	fw.write(str(user)+"\n")
