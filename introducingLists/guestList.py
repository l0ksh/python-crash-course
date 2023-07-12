#!/usr/bin/python3

# actual guest list
guest_list = ['Aman','Jack','Elon']

print(f'This is my guest list: {guest_list}')

# invitation message
message = f'''Hello {guest_list[0]}, You are invited to a dinner party at my home on Friday.
Hello {guest_list[1]}, You are invited to a dinner party at my home on Friday.
Hello {guest_list[2]}, You are invited to a dinner party at my home on Friday.
'''

print(message)

# removing 'Jack' from the list
not_coming = guest_list.pop(1)
not_coming_message =  f'Hey all, I\'m so sorry to have to tell you this, but {not_coming} won\'t be able to make it to the party tonight.'

print(not_coming_message)

# printing updated message
new_message = f'''Hello {guest_list[0]}, You are invited to a dinner party at my home on Friday.
Hello {guest_list[1]}, You are invited to a dinner party at my home on Friday.
'''
print('\n-------------------------------------------------')
print(new_message)

# Found a bigger dinner table.
# Now invite more people and change the list accordingly.
print('Hello all, I am glad to tell you that I got a bigger table now. So I am inviting more members.\n')

# updating guest_list
guest_list.insert(0,'Ron')
guest_list.insert(2,'Rahul')
guest_list.append('Ash')

print(f'Updated guest list : {guest_list}\n')

updated_message = f'''Hello {guest_list[0]}, You are invited to a dinner party at my home on Friday.
Hello {guest_list[1]}, You are invited to a dinner party at my home on Friday.
Hello {guest_list[2]}, You are invited to a dinner party at my home on Friday.
Hello {guest_list[3]}, You are invited to a dinner party at my home on Friday.
Hello {guest_list[4]}, You are invited to a dinner party at my home on Friday.
'''
print(updated_message)
print('-------------------------------------------------------------')

# shrinking guest_list

updated_message2 = 'New table won\'t be ready, so can only invite 2.'

print(updated_message2)


# popping users from list

popped_guest = guest_list.pop()
print(f'Sorry I can\'t invite {popped_guest}')
popped_guest = guest_list.pop()
print(f'Sorry I can\'t invite {popped_guest}')
popped_guest = guest_list.pop()
print(f'Sorry I can\'t invite {popped_guest}')

updated_message = f'''
Hello {guest_list[0]}, You are invited to a dinner party at my home on Friday.
Hello {guest_list[1]}, You are invited to a dinner party at my home on Friday.
'''

print(updated_message)

# removing all the items from the list so that it becomes empty

del guest_list[0]
del guest_list[0]

print(f'Empty list: {guest_list}')
