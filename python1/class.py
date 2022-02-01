class Bottle(object):
    def __init__(self,color,brand,capacity,material):
        self.color = color
        self.brand = brand
        self.capacity = capacity
        self.material = material

    def hello(self):
        print("Hello")

def main():
    mybottle = Bottle("Violet","Tupperware","2 litres","Plastic")
    myBottle2 = Bottle("Red","Milton","1 litre","Steel")
    myBottle2.hello()
    print(mybottle.color)

if __name__ == "__main__":
    main()
  