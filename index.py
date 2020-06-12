email = input('Enter your email adress: ')

username = email[:email.index("@")]
username_slicer = ''.join(e for e in username if e.isalnum())

domain = email[email.index("@")+1:]

print(f'Username: {username_slicer}, Domain name: {domain}')
