# mongo connection
MONGO_URI = 'mongodb://localhost:27017/eve-course'

# мотоди доступні для ресурсів
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']  # добавляємо дозволені методи

# методи доступні для items
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']  # GET=read, PATCH=edit, PUT=replace

# відключення перевірки if_match 
IF_MATCH = False

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
    'works': {
        'resource_methods': ['GET'],
        'item_methods': ['GET'],
    },
}
