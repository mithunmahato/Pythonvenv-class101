try:
    file = open('example.txt','r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    file.close() 