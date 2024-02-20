from django.http import JsonResponse

def show_endpoints(request):
    base_url = "http://127.0.0.1:8000"
    
    endpoints = [
        {"Tool": "Swagger UI", "Endpoint": f"{base_url}/swagger/", "Description": "Swagger UI Documentation"},
        {"Tool": "ReDoc", "Endpoint": f"{base_url}/redoc/", "Description": "ReDoc API Explorer"},
    ]

    user_endpoints = [
        {"Method": "POST", "Endpoint": f"{base_url}/api/v1/user/register/", "Description": "Register a new user", "Body": "(username, password)", "Header": "-", "Response": "New user data"},
        {"Method": "POST", "Endpoint": f"{base_url}/api/v1/user/token/", "Description": "Obtain JWT token", "Body": "User credentials (username, password)", "Header": "-", "Response": "JWT tokens"},
        {"Method": "POST", "Endpoint": f"{base_url}/api/v1/user/token/refresh/", "Description": "Refresh JWT token", "Body": "Refresh token", "Header": "-", "Response": "New access token"},
        {"Method": "GET", "Endpoint": f"{base_url}/api/v1/user/all-users/", "Description": "List all users", "Body": "-", "Header": "-", "Response": "List of users"},
        {"Method": "GET", "Endpoint": f"{base_url}/api/v1/user/lislt-update/", "Description": "Get user information", "Body": "-", "Header": "Authorization token 'Bearer + access_token'", "Response": "User information"},
        {"Method": "PUT", "Endpoint": f"{base_url}/api/v1/user/lislt-update/", "Description": "Update user information", "Body": "Updated user data (username, password)", "Header": "Authorization token 'Bearer + access_token'", "Response": "Updated user data"},
        {"Method": "PATCH", "Endpoint": f"{base_url}/api/v1/user/lislt-update/", "Description": "Partially update user information", "Body": "Partial user data (username, password)", "Header": "Authorization token 'Bearer + access_token'", "Response": "Updated user data"},
    ]

    messaging_endpoints = [
        {"Method": "POST", "Endpoint": f"{base_url}/api/v1/messaging/send-message/", "Description": "Send a message", "Body": "Message data (text, receiver_username)", "Header": "Authorization token 'Bearer + access_token'", "Response": "Success message"},
        {"Method": "GET", "Endpoint": f"{base_url}/api/v1/messaging/inbox/", "Description": "Get inbox messages for the authenticated user", "Body": "-", "Header": "Authorization token 'Bearer + access_token'", "Response": "List of inbox messages"},
        {"Method": "GET", "Endpoint": f"{base_url}/api/v1/messaging/outbox/", "Description": "Get outbox messages for the authenticated user", "Body": "-", "Header": "Authorization token 'Bearer + access_token'", "Response": "List of outbox messages"},
    ]

    endpoints.extend(user_endpoints)
    endpoints.extend(messaging_endpoints)

    return JsonResponse({"endpoints": endpoints}, json_dumps_params={'indent': 2})
