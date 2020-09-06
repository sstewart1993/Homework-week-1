# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pets):
    return (pets ["name"])   

def get_total_cash(pets):
    return pets["admin"]["total_cash"]

def add_or_remove_cash(pets, amount):
       cash = get_total_cash(pets)
       pets["admin"]["total_cash"] = cash + amount
       return cash

def get_pets_sold(pets):
        return pets["admin"]["pets_sold"]

def increase_pets_sold(pets, amount):
    sold = get_pets_sold(pets)
    pets["admin"]["pets_sold"] = sold + amount
    return pets["admin"]["pets_sold"]

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed_name):
    list_of_breeds = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_name:
            list_of_breeds.append(pet_shop["pets"])
    return list_of_breeds


def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

    
def remove_pet_by_name(pet_shop, pet_name):
    current_pet = find_pet_by_name(pet_shop, pet_name)
    removed_pet = pet_shop["pets"].remove(current_pet)
    return removed_pet

def add_pet_to_stock(pet_shop, pet_name):
    pet_shop["pets"].append(pet_name)
    new_pets = get_stock_count(pet_shop)
    return new_pets

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, amount):
    customers["cash"] -= amount
    return customers

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)
    pet_counter = get_customer_pet_count(customers)
    return pet_counter

#  ---OPTIONAL----

def customer_can_afford_pet(customers, pet_shop):
    money = get_customer_cash(customers)
    price = pet_shop["price"]
    if money >= price:
        return True
    elif money < price:
        return False

# --- integration ---

def sell_pet_to_customer(pet_shop, pet, customer):
    find_pet_by_name(pet_shop, pet_name)
    pet_count = customer["pets"]








