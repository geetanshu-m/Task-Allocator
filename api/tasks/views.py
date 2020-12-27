'''
Following API's are needed

- Company Creation flow, company_admin creates account, create company, add employees,
- Validate users
- User task [CRUD]
    - user can add a task
    - update a task [Mark as complete]
    - Get a list of his tasks
'''

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})