import json
users = ['Enzo', 'Jean', 'Marc']
categories = ['pc', 'laptop', 'printer']

def addDevice(id, user, category, brand, model, serialNumber, dateOfPurchase):
    verif = False
    if user in users and category in categories:
        verif = True

    if verif == True:
        device = {
            'id': id,
            'user': user,
            'category': category,
            'brand': brand,
            'model': model,
            'serialNumber': serialNumber,
            'dateOfPurchase': dateOfPurchase,
            'status': 'available'
        }
        return device
    else:
        print("Un des champs n'as pas été remplis correctement...")


result = addDevice(1, 'Enzo', 'laptop', 'brand', 'model', 'SN', '01/10/21')
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)