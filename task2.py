def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():  
                    cat_id, name, age = line.strip().split(',')
                    try:
                        cats_info.append({
                            'id': cat_id,
                            'name': name,
                            'age': int(age)
                        })
                    except ValueError:
                        print(f"Помилка: некоректне значення віку у рядку '{line.strip()}'")
                else:
                    print(f"Помилка: некоректний формат рядка '{line.strip()}'")
    except FileNotFoundError:
        print(f"Помилка: файл {path} не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")
    
    return cats_info

cats_info = get_cats_info("./cats.txt")
print(cats_info)