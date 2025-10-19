from dotenv import load_dotenv
import boto3

load_dotenv()
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('cliente')
response = table.put_item(
   Item={
        'id': 2,
        'nome': 'Anna Heloisa',
        'idade': 21,
        'email': 'anna.heloisa@example.com',
        'telefone': '11999999999'
    }
)   
print("Item inserido com sucesso:", response)