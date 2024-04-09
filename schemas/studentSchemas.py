def student_entity(item) -> dict:
    return {
        'id': str(item['_id']),
        'name': item['name'],
        'age': item['age'],
        'address': {
            'city': item['address']['city'],
            'country': item['address']['country']
        }
    }

def all_students_entity(items):
    return [student_entity(item) for item in items]
