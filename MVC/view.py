from model import Device


def showAllview(list):
    print("In our DB we have %i device entries:" % len(list))
    for i in list:
        print(i.name())

def startView():
    print('MVC example')
    print('Do you have to see devices in my db?[y/n]')

def endView():
    print('GoodBye!')


