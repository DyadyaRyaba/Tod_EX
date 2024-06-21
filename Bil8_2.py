import xml.etree.ElementTree as ET
import json

# Загрузка и парсинг XML-файла
xml_file_path = 'path_to_steps_sample.xml'  # Замените на реальный путь к файлу
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Формирование словаря
steps_dict = {}
for recipe in root.findall('recipe'):
    recipe_id = recipe.find('id').text
    steps = [step.text for step in recipe.findall('steps/step')]
    steps_dict[recipe_id] = steps

# Сохранение словаря в JSON-файл
json_file_path = 'steps_sample.json'
with open(json_file_path, 'w') as json_file:
    json.dump(steps_dict, json_file, indent=4, ensure_ascii=False)

print(f"Данные успешно сохранены в файл {json_file_path}")
