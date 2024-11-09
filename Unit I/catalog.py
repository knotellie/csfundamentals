""" Welcome to your first project. 
Develop a catalog for a company. 
Assume that this company sells three different Items. 
The seller can sell individual items or a combination of any two items. 
A gift pack is a special combination that contains all three items. 
Here are some special considerations:

    If a customer purchases individual items, he does not receive any discount.
    If a customer purchases a combo pack with two unique items, he gets a 10% discount.
    If the customer purchases a gift pack, he gets a 25% discount. 

Write a function for the above scenario. 
Perform the calculations in code wherever applicable. 
The function should be your own creation, not copied from any other source. 

Include the following in your Part 2 submission:

    The code for the function that you created.
    The output of the code.
    A description of what feature(s) your function illustrates.
    The code and its output must be explained technically. 
    The explanation can be provided before or after the code, or in the form of comments within the code. 

If you use an informational source, be sure to identify the source and share the link to the source you used.
 """

def print_catalog():
    item1 = input("What's the name for the first item? ")
    item1_price = float(input("What's its price? "))
    item2 = input("What's the name for the second item? ")
    item2_price = float(input("What's its price? "))
    item3 = input("What's the name for the third item? ")
    item3_price = float(input("What's its price? "))

    print("\n\n\n\n\nGenerating the catalog...\n\n\n\n\n")

    print("Online Store")
    print("--------------------------------------------------------------------")
    print("Product(s)                                          Price")
    print(f'{item1}                                            $ {item1_price}')
    print(f'{item2}                                            $ {item2_price}')
    print(f'{item3}                                            $ {item3_price}')
    print(f'Combo 1 ({item1} + {item2})                        $ {(item1_price + item2_price) * 0.9}')
    print(f'Combo 2 ({item1} + {item3})                        $ {(item1_price + item3_price) * 0.9}')
    print(f'Combo 3 ({item2} + {item3})                        $ {(item2_price + item3_price) * 0.9}')
    print(f'Gift Pack ({item1} + {item2} + {item3})            $ {(item1_price + item2_price + item3_price) * 0.75}')
    print("--------------------------------------------------------------------")
    print("For delivery Contact:584247592768")

print_catalog()