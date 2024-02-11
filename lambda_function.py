import json

def lambda_handler(event, context):
    name = event.get('queryStringParameters', {}).get('name')
    if name is not None:
        message = f'Hello {name}!'
    else:
        message = 'Please provide a name parameter in the query string!'

    response = {
        'statusCode': 200,
        'body': json.dumps({'message': message})
    }

    return response
