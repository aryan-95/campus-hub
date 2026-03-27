import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecord')

def lambda_handler(event, context):
  
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }
    
    try:
        method = event.get('httpMethod')
        
        if method == 'GET':
           
            response = table.scan()
            items = response.get('Items', [])
            
            
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps(items)
            }
            
        elif method == 'POST':
            body = json.loads(event['body'])
            table.put_item(Item=body)
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps("Success")
            }
            
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps("Unsupported method")
        }

    except Exception as e:
        
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({"error": str(e)})
        }