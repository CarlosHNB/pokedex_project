import requests
import json


url = "https://pokeapi.co/api/v2/pokemon/bulbasaur"

api_request = requests.get(url)
json_loads = json.loads(api_request.content)

value_hp = f"HP - {json_loads['stats'][0]['base_stat']}"
value_attack = f"ATTACK - {json_loads['stats'][1]['base_stat']}"
value_defense = f"DEFENSE - {json_loads['stats'][2]['base_stat']}"
value_special_attack = f"SPECIAL-ATTACK - {json_loads['stats'][3]['base_stat']}"
value_special_defense = f"SPECIAL-DEFENSE - {json_loads['stats'][4]['base_stat']}"
value_speed = f"SPEED - {json_loads['stats'][5]['base_stat']}"




print(value_hp)
print(value_attack)
print(value_defense)
print(value_special_attack)
print(value_special_defense)
print(value_speed)