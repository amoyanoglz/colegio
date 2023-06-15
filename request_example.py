import requests

def generate_name_and_email():
    uri = 'https://randomuser.me/api/?results=1'
    r = requests.get(uri)
    randomuser = r.json()
    user = randomuser["results"][0]
    my_user_data = {
        "nombre": f'{user["name"]["first"]} {user["name"]["last"]}',
        "correo": user["email"]
    }
    return [my_user_data]

def main():
    my_user = generate_name_and_email()[0]
    print(f"NOMBRE: {my_user['nombre']}")
    print(f"CORREO: {my_user['correo']}")

if __name__ == "__main__":
    main()


# import requests
# # recuerda instalar la libreria
# #     Win: pip install requests
# #     Mac: pip3 install requests

# def get_json_from(uri):
#     r = requests.get(uri)
#     # print(r.status_code)
#     # print(r.headers['content-type'])
#     # print(r.encoding)
#     # print(r.text)
#     # print(r.json())

#     return r.json()

# def pretty(d, indent=0):
#     for key, value in d.items():
#         print('  ' * indent + str(key))
#         if isinstance(value, dict):
#             pretty(value, indent+1)
#         else:
#             print('\t' * (indent+1) + str(value))

# def main():
#     results = "1"  # input("Cuantos quieres? ")
#     uri = f'https://randomuser.me/api/?results=1'
#     dict = get_json_from(uri)

#     for user in dict["results"]:
#         pretty(user)

# if __name__ == "__main__":
#     main()

# Viejo request: No funciona a la priemra en windows:

# import json
# import urllib.request

# def get_json_from(uri):
#     urlopenRet = urllib.request.urlopen(urlData)
#     data = urlopenRet.read()
#     encoding = urlopenRet.info().get_content_charset('utf-8')
#     JSON_object = json.loads(data.decode(encoding))

#     return JSON_object