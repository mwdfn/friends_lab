
# Question 1
from pickle import FALSE


def get_name(person):
    return person["name"]

# Quesiton 2
def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

# Question 3
# def likes_food(person2):
#     if ["favourite"] ["snacks"] == "bread":
#         return person2 = True 

def likes_to_eat(person, food):

    foundFood = False
    snacks = person["favourites"]["snacks"]

    for snack in snacks:
        if snack == food:
         foundFood = True
    return foundFood

def add_friend(person, new_friend):
    person ["friends"].append(new_friend)


def remove_friend(person, not_friend):
    person ["friends"].remove(not_friend)

# def likes_to_eat(person, food):
#     snacks = person["favourites"]["snacks"]

#     for snack in snacks:
#         if snack != food:
#             return False
      




