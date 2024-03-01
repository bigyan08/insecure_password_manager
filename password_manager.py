import pyperclip

print("Welcome to the password manager!")
passwords={
    'email':'email_password',
    'facebook':'facebook_password',
    'instagram':'insta_password'
}
print("Enter account name:")
account_name=input()
if account_name in passwords:
    pyperclip.copy(passwords[account_name])
    print("Password of "+account_name+" copied to clipboard.")
else:
    print("invalid input!")
