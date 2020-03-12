from New_user import *

new_users = []

opened_file = open('Name.txt', 'r')
lines = opened_file.readlines()
for line in lines:
        new_users.append(New_users(line))
        #print(new_users)
opened_file.close()

new_users[5].output_text_file('username1.txt')
