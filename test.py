# from IPython.display import clear_output

def its_a_function():
    
    shop_list = {}
    i = 0

    while True:
        # clear_output()
        what_do = input("Do you want to : Show/Add/Delete or Quit? ")
        
        if (what_do == 'quit'):
            break
        elif (what_do == 'show'):
            print(shop_list)
        elif (what_do == 'add'):
            shop_list[(input("What would you like to add ?" ))]
            i +=-1
        elif (what_do == 'delete'):
            del shop_list[(input("What would you like to delete ?" ))]
        else:
            print("Read the directions.")
            
its_a_function()
