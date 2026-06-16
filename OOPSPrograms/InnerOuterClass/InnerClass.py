
class Outer:
    def __init__(self):
            print("outer class")
    class Inner:
        def __init__(self):
            print("inner class")

outer=Outer()
inner=outer.Inner()
