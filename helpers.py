import uuid


def generate_user_data():
    unique_part = uuid.uuid4().hex[:10]

    return {
        'name': 'Vladislav',
        'email': f'vladislav_{unique_part}@ya.ru',
        'password': f'Password_{unique_part}'
    }
