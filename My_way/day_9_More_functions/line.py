def line(times, string):
    if times > 0:
        if string[0] == "" or string[0] == " ":
            print("*" * times)
        else:
            print(string[0] * times)
    else:
        print("times cannot be negative or zero")
line (4, "67")