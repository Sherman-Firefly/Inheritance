class bird:
    def __init__(self):
        print("This is a bird")
    def whoisthat(self):
        print("It is a bird")
    def swim(self):
        print("Swims rather well")

class penguin(bird):

    def __init__(self):
        super().__init__()
        print("Penguin is here")
    def whoisthat(self):
        print("Bob the Penguin")
    def run(self):
        print("It can run")
    
pengu=penguin()
pengu.whoisthat()
pengu.swim()
pengu.run()
