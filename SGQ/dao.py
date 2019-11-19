from __future__ import print_function  # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

class lista_atividades():
    def __init__(self,id_processo_atividade, processo, atividade, tempo):
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://dynamodb.us-east-2.amazonaws.com")
        table = dynamodb.Table('lista_atividade')
        try:
            response = table.get_item(
                Key={
                    'id_processo_atividade': id_processo_atividade,
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            item = response['Item']
            lista = json.dumps(item, indent=4, cls=DecimalEncoder)
            lista_json = json.loads(lista)
            self.processo = lista_json.get("processo")
            self.atividade = lista_json.get("atividade")
            self.tempo = lista_json.get("tempo")



