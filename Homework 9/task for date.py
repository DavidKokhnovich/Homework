def transformed_date(date: str):
    d, m, y = date.split('.')
    transform_date = f"{y}-{m}-{d}"
    return transform_date

date = "26.07.2024"
print(transformed_date(date))