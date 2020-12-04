# USING PYTHON TO MODIFY FILE SYSTEM
import json
# with open('distros.json', 'r') as f:
#     distros_dict = json.load(f)
#     for distro in distros_dict:
#         print(distro['Name'])

# EXAMPLE: JSON STRING TO PYTHON DICTIONARY
appsettings_JSON = """
{
  "ConnectionStrings": {
    "car_app": "Server=localhost;Database=car_app;uid=root;Pwd=password;Port=3306;"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Warning"
    }
  },
  "AllowedHosts": "*"

}
"""

# Use the loads() function to turn the JSON string into a PYTHON dict
appsettings_dict = json.loads(appsettings_JSON)
# print(appsettings_dict)
# print(appsettings_dict["ConnectionStrings"])
#
# x = appsettings_dict["ConnectionStrings"]
# print(x["car_app"])

# EXAMPLE: PYTHON DICTIONARY TO JSON STRING
json_str = json.dumps(appsettings_dict)
print(json_str)