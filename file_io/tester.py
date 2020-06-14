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


class master():
    def __init__(self):
        self.message = "Fk bank of america"
        self.node = None

    def add_node(self):
        self.node = Node(self)

class Node():
    def __init__(self, m):
        self.previous = m

    def fun(self):
        print(self.previous.message)

tester = master()
tester.add_node()
tester.node.fun()