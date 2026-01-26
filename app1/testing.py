# import io
# import json

# my_dict = {"user": "admin", "action": "login", "timestamp": 2026}

# # dumping to json
# json_bytes = json.dumps(my_dict).encode("utf-8")
# print(json_bytes)

# #buffer the json bytes 

# json_buffer = io.BytesIO(json_bytes)

# json_buffer.seek(0)

# json_data = json.loads(json_buffer.read().decode("utf-8"))
# print(json_data)


#import jsonrender to convert a dict to json 


from rest_framework.renderers import JSONRenderer

