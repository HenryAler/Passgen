import base64

picture = open('button.png', 'rb')
content = f'img = {base64.b64encode(picture.read())}\n'
picture.close()

with open('buttontostr.py', 'w') as file:
    file.write(content)