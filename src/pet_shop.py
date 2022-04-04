# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]
#"Camelot of Pets"

def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]
# 1000

def add_or_remove_cash(pet_shop,value1):
    pet_shop["admin"]["total_cash"] += value1

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop,value2):
    pet_shop["admin"]["pets_sold"] += value2

def get_stock_count(number_pets):
    return len(number_pets["pets"])

def get_pets_by_breed(pet_shop, breed):
    list_of_pets = []
    pets = pet_shop["pets"]
    for pet in pets :
        if pet["breed"] == breed:
            list_of_pets.append(pet)
    return list_of_pets
#update

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
#update


def remove_pet_by_name(pet_shop, name):
    pets = pet_shop["pets"]

    for pet in pets :
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)
#update

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customer, value3):
    value3 - 100
    customer["cash"]
#don't like
   
def get_customer_pet_count(customer_pets):
    list = []
    return list.count(customer_pets)

def add_pet_to_customer(customer_pets, new_pet):
    #customer_pets["pets"] = new_pet
    #customer_pets["pets"].append(new_pet)
    customer = customer_pets["pets"]
    customer.append(new_pet)


# def add_pet_to_customer(customer1, new_pet):
#     customer1["pets"].append(new_pet)
    

# def test_add_pet_to_customer(self):
#         customer = self.customers[0]
#         add_pet_to_customer(customer, self.new_pet)
#         self.assertEqual(1, get_customer_pet_count(customer)


# def test_add_friend(self):
#     add_friend(self.person2, "Scrappy-Doo")
#     self.assertEqual(2, len(self.person2["friends"]))


# def add_friend(person, new_friend):
#   person["friends"].append(new_friend)


# def get_pets_by_breed(pet_shop, breed):
#     list_of_pets = []
#     pets = pet_shop["pets"]
#     for pet in pets :
#         if pet["breed"] == breed:
#             list_of_pets.append(pet)
#     return list_of_pets