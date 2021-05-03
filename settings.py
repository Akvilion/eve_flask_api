# mongo connection
MONGO_URI = 'mongodb://localhost:27017/eve-course'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']  # добавляємо дозволені методи

# модель для нашого people
schema = {
    'firstname': {'type': 'string'},
    'lastname': {'type': 'string'},
}


# 
DOMAIN = {
    'people': {
        'schema': schema 
    },
}
