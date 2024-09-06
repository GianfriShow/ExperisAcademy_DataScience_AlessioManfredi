# create a menu where we can choose any of the things we've learnt so far and then explore it (even just a simple definition of the topic)
# use a bunch of functions, at least 2 decorators, and make it repeatable (e.g. can go back to menu and select another topic)

def showcase():

    print("Welcome to the 2nd-week showcase. Here you'll be able to learn about some of the topics we've touched so far.")

    def add_back_to_menu_option(function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            choice = int(input("Would you like to go back to the main menu? (type number)\n    1) No\n    2) Yes\n"))-1
            if choice:
                menu()
        return wrapper
    
    def menu():
        choice = int(input("Please select one of the following topics:\n    1) UML\n    2) Lists\n    3) Range\n    4) Loops\n    5) Conditions\n    6) Company roles\n    7) Tasking\n    8) Methodologies of software development\n    9) GitHub\n    10) Exit\n"))
        if choice==1:
            uml_menu()
        elif choice==2:
            lists_menu()
        elif choice==3:
            range_menu()
        elif choice==4:
            loops_menu()
        elif choice==5:
            conditions_menu()
        elif choice==6:
            roles_menu()
        elif choice==7:
            tasking_menu()
        elif choice==8:
            methodologies_menu()
        elif choice==9:
            github_menu()
        else:
            pass

    @add_back_to_menu_option
    def uml_menu():
        print("UML is...")

    @add_back_to_menu_option
    def lists_menu():
        print("UML is...")

    @add_back_to_menu_option
    def range_menu():
        print("UML is...")
    
    @add_back_to_menu_option
    def loops_menu():
        print("UML is...")

    @add_back_to_menu_option
    def conditions_menu():
        print("UML is...")

    @add_back_to_menu_option
    def roles_menu():
        print("UML is...")

    @add_back_to_menu_option
    def tasking_menu():
        print("UML is...")

    @add_back_to_menu_option
    def methodologies_menu():
        print("UML is...")

    @add_back_to_menu_option
    def github_menu():
        print("UML is...")

    menu()

showcase()
