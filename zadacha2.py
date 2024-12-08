def read_cookbook(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return {
            line.strip(): [
                {
                    'ingredient_name': data[0],
                    'quantity': int(data[1]),
                    'measure': data[2]
                }
                for data in (file.readline().strip().split(' | ') for _ in range(int(file.readline().strip())))
            ]
            for line in file if line.strip()
        }


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count  
            measure = ingredient['measure']
            
            
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    
    return shop_list



file_path = r'C:\Users\XXX\Desktop\Files\recipes.txt'  
cook_book = read_cookbook(file_path)  
dishes = ['Запеченный картофель', 'Омлет']  
person_count = 2  

shop_list = get_shop_list_by_dishes(dishes, person_count)
print(shop_list)
