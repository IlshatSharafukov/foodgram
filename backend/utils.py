import hashlib


def generate_short_link(recipe_id):
    """
    Генерация короткой ссылки для рецепта.
    """

    hash_object = hashlib.md5(str(recipe_id).encode())
    return hash_object.hexdigest()[:6]
