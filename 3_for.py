"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

sold = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def sum_item():
    sold_product = {}
    for i in sold:
        sold_product[i["product"]] = sum(i["items_sold"])
    return sold_product


def average_sold_item():
    avarage = {}
    for i in sold:
        avarage[i["product"]] = round(sum(i["items_sold"]) / len(i["items_sold"]), 1)
    return avarage


def sum_items():
    sm = sum_item()
    return sum([i for i in sm.values()])


def average_sold_items():
    sm = average_sold_item()
    return round(sum([i for i in sm.values()]) / len(sm), 1)


def main():
    print()
    print("Cуммарное количество продаж для каждого товара:")
    for i, j in sum_item().items():
        print(f"  {i}: {j}")
    print()
    print("Cреднее количество продаж для каждого товара:")
    for i, j in average_sold_item().items():
        print(f"  {i}: {j}")
    print()
    print(f"Cуммарное количество продаж всех товаров: {sum_items()}", "\n")
    print(f"Cреднее количество продаж всех товаров: {average_sold_items()}", "\n")


if __name__ == "__main__":
    main()
