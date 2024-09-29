from model import Device
import view as view

def showall():
    device_in_db = Device.getall()
    return view.showAllview(device_in_db)

def start():
    view.startView()
    answer = input()
    if answer == 'y':
        return showall()
    else:
        return view.endView()
    
if __name__ == "__main__":
    start()