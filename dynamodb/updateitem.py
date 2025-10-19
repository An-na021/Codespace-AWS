from dotenv import load_dotenv
import boto3

load_dotenv()
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('cliente')
table.update_item(
    Key={
        'id': 2
    },
    UpdateExpression="SET idade = :anos, telefone = :num",
    ExpressionAttributeValues={
        ':anos': 22,
        ':num': '11988888888'
    }
)
print("Item atualizado com sucesso.")