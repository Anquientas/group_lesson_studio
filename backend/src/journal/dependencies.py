
class Paginator:
    def __init__(self, limit: int = 10, skip: int = 0):
        self.limit = limit
        self.skip = skip


def pagination_parameters(limit: int = 10, skip: int = 0):
    return {'limit': limit, 'skip': skip}
