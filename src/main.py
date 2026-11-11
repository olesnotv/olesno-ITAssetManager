import json

jsonExemple = {
    "id": 12909,
    "user": "A. Lexius",
    "category": "laptop",
    "brand": "Dell",
    "model": "bullshit",
    "serialNumber": "AC87-ES90-SD90-KO27",
    "purchaseDate": '21/03/2001',
    "status": 'available'
}

print(json.dumps(jsonExemple, indent=4))