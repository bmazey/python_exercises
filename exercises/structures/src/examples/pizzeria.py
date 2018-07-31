from exercises.structures.src.examples.pizza import Pizza


def make_pizza():
    pepperoni_pizza = Pizza(['pepperoni', 'cheese', 'tomato sauce'])
    meat_lovers = Pizza(['sausage', 'meatball', 'pepperoni', 'prosciutto'])
    vodka_grandma = Pizza(['vodka sauce', 'mozzarella'])

    # total_toppings = pepperoni_pizza.toppings + meat_lovers.toppings + vodka_grandma.toppings
    # print(total_toppings)

    print(len(pepperoni_pizza))
    print(len(meat_lovers))

    print(pepperoni_pizza[1])

    supreme_pizza = pepperoni_pizza + meat_lovers + vodka_grandma
    print(supreme_pizza.toppings)



if __name__ == '__main__':
    make_pizza()
