import json
import sys
import os

# Add the parent directory to the path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app import app

def lambda_handler(event, context):
    """AWS Lambda handler for API Gateway"""
    
    # Handle API Gateway proxy integration
    path = event.get('path', '/')
    http_method = event.get('httpMethod', 'GET')
    headers = event.get('headers', {})
    body = event.get('body', '')
    
    # Create WSGI environment
    environ = {
        'REQUEST_METHOD': http_method,
        'PATH_INFO': path,
        'QUERY_STRING': event.get('queryStringParameters', ''),
        'CONTENT_TYPE': headers.get('content-type', ''),
        'CONTENT_LENGTH': str(len(body)),
        'wsgi.input': body,
        'wsgi.url_scheme': 'https',
        'SERVER_NAME': headers.get('Host', 'localhost'),
        'SERVER_PORT': '443',
    }
    
    # Add headers to environ
    for key, value in headers.items():
        key = key.upper().replace('-', '_')
        if key not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
            environ[f'HTTP_{key}'] = value
    
    # Process request with Flask app
    with app.request_context(environ):
        try:
            response = app.full_dispatch_request()
            
            return {
                'statusCode': response.status_code,
                'headers': dict(response.headers),
                'body': response.get_data(as_text=True)
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }
