# scope is where a variable is accessble and visible to be used
# there is a rule called (LEGB) local -> Enclosed -> Global -> Build-in


def func1():
    x = 1
    print(x)

    def func2():
        x = 2
        print(
            x
        )  # will print 2 as local scope resolved first before enclosed scope variable

    func2()


func1()
