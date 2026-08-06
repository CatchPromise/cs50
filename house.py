name = input("What's your name? ")

match name:
    case "eliora" | "david" |"ruth" |"rema":
        print("ibologi")
    case "blessing" | "gift":
        print("ghana")
    case "lawrence" | "laura":
        print("kebbi")
    case _:
        print("who?")