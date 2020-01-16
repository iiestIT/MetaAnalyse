#from backend import code

def console_input():
    with open("welcome.txt", "r") as first:
        for line in first:
            print(line)
    while True:
        user_input = input("MetaAnalyse > ")

        if user_input == "q":
            quit()
        if user_input == "quit":
            quit()

        if user_input == "-h":
            with open("help.txt", "r") as user_help:
                for help_line in user_help:
                    print(help_line)
        if user_input == "-help":
            with open("help.txt", "r") as user_help:
                for help_line in user_help:
                    print(help_line)

        else:
            print("console ~# undefined input")
console_input()