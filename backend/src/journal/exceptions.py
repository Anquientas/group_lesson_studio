class ObjectNotFoundException(ValueError):
    """Исключение при отсутствии запрошенного объекта."""
    pass


class ObjectNotActiveException(Exception):
    """Исключение при получении неактивного статуса объекта."""
    pass


class ObjectIsExistException(ValueError):
    """
    Исключение при создании нового объекта,
    если уже существует объект с переданным параметром.
    """
    pass
