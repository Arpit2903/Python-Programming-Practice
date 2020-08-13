def decorator1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Func1 executed")
    return nowexec()

@decorator1
def who_is_arpit():
    print("Arpit is a Boy")

who_is_arpit()