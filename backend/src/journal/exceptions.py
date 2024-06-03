class ObjectNotFoundException(ValueError):
    """Исключение при отсутствии запрошенного объекта."""
    pass


class ObjectAlreadyExistsException(ValueError):
    """
    Исключение при создании нового объекта,
    если уже существует объект с переданным параметром.
    """
    pass


# class ObjectIsNotActiveException(Exception):
#     """Исключение при получении неактивного статуса объекта."""
#     pass
