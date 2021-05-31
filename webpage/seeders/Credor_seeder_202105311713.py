from ..models import Credor

# Start the database seeding
data = [
    {
        "id": 2000,
        "nome": "ASPA - ESCOLA ADVENTISTA DE REDENCAO"
    },
    {
        "id": 2001,
        "nome": "ASPA - ADVENTISTA CONCEICAO DO ARAGUAIA"
    },
    {
        "id": 2002,
        "nome": "ASPA - ESCOLA ADVENTISTA DE PARAGOMINAS"
    }
]

def seed():
    for credor_on in data:
        Credor.objects.create(**credor_on)