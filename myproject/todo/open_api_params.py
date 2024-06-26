from drf_yasg import openapi

# get_params = [
#     openapi.Parameter(
#         name='id',
#         description='id',
#         type=openapi.TYPE_INTEGER,
#         default=""
#     )
# ]

post_params = openapi.Parameter(
    type=openapi.TYPE_OBJECT,
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='todo 제목'),
        'description': openapi.Schema(type=openapi.TYPE_STRING,description='todo 부가설명'),
        'completed': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='false'),
        'dueDate_at': openapi.Schema(type=openapi.FORMAT_DATE, description='2024-08-03'),
    }
)
