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

file_path = r'C:\Users\XXX\Desktop\Files\recipes.txt'  
cook_book = read_cookbook(file_path)
print(cook_book)
