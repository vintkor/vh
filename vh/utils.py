from django.utils.crypto import get_random_string


def set_image_name(instanse, filename):
    name = get_random_string(40)
    ext = filename.split('.')[-1]
    path = 'images/catalog/{}.{}'.format(name, ext)
    return path
