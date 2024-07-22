def total_salary(path):
    total_sum = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():  
                    parts = line.split(',')
                    if len(parts) == 2:
                        try:
                            salary = int(parts[1].strip())
                            total_sum += salary
                            count += 1
                        except ValueError:
                            print(f"Помилка: некоректне значення заробітної плати у рядку '{line.strip()}'")
                    else:
                        print(f"Помилка: некоректний формат рядка '{line.strip()}'")
    
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return None
    
    except Exception as e:
        print(f"Помилка: {e}")
        return None

    if count > 0:
        average_salary = total_sum / count
    else:
        average_salary = 0

    return (total_sum, average_salary)

total, average = total_salary('./salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
