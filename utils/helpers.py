def filter_by(age, salary, list_items):
    results = []
    if len(list_items) == 0:
        return
    
    for item in list_items:
        if item['employee_salary'] > int(salary) and item['employee_age'] > int(age):
            results.append(item)

    return results