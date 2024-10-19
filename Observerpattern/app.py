from observable import Observable
from observer import Observer

class ImeditaNetworkDevices(Observer):
    def update(self,*args,**kwargs):
        print("Imedita Network Devices Group Received:{0}\n\{1}".format(args,kwargs))

class ImeditaEdgeRouters(Observer):
    def update(self,*args,**kwargs):
        print("Imedita Edge Routers Devices Group Received:{0}\n\{1}".format(args,kwargs))



if __name__ == "__main__":
    observable = Observable()

    Network_Device_staff = ImeditaNetworkDevices()
    observable.register(Network_Device_staff)

    EdgeRouters_staff = ImeditaEdgeRouters()
    observable.register( EdgeRouters_staff)

    observable.update_observers('Network Outage', msg = 'Provider Link Down!')


