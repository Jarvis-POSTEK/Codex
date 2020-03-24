class wut:
    def __init__(self):
        self.message = "hellowasdasdw"

    def fun(self):
        print(self.message)

class test(wut):
    def __init__(self):
        super().__init__()
    
    def wutwut(self):
        self.fun()

tester = test()
tester.wutwut()
