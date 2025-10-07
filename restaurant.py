#it is a callback example. customer in restaurant put order and waiter deliver food

##--
# PS code (beachten sie arr_length is definieren in linie 12)
# def food_exists = 0
# For i = 0 BIS i <= arr_length i++
#   IF food_name == arr_foods[i]
#       food_exists=1
#   End IF
# Return food_exist
##--

def checkFoodExistance(food_name:str):
    arr_foods=["Pizza", "Pasta", "Doener"]
    arr_length=len(arr_foods)
    print(f"we have {arr_length} foods in Menu")
    if food_name in arr_foods:
        print(f"your order will be delivered in 10 minutes")
    else:
        print(f"unfortunatly your {food_name} is not in the Menu")

def orderFood(food_name:str, checkFoodExistance):
    print(f"your {food_name} deliver soon!")
    checkFoodExistance(food_name)

#-- actual program use upper defined methods --#
order_string=input("what is your order?")
orderFood(order_string,checkFoodExistance)




