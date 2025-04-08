email1 = 'user@example.com'
email2 = 'user@example'
print(f'이메일 주소 : {email1}')
if '@' in email1 and '.' in email1.split('@')[1]:
    print("유효함")
else:
    print("유효하지 않음")
print(f'이메일 주소 : {email2}')
if '@' in email2 and '.' in email2.split('@')[1]:
    print("유효함")
else:
    print("유효하지 않음")