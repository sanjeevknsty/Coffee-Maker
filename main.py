# from turtle import Turtle,Screen
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("Red")
# for _ in range(5):
#     timmy.forward(100)
#     timmy.backward(200)
# timmy.position
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
# table.max_table_width()

table.add_column("Name",["me", "You","panchapatlasarangipanni"])
table.add_column("age",["12","34","34"])
table.align ="r"
print(table)