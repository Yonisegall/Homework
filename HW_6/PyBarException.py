class InvalidInputException(Exception):
    pass


class OccupiedTableException(Exception):
    pass


class TooSmallTableException(Exception):
    pass


class EmptyTableException(Exception):
    pass


class AccessDeniedException(Exception):

    def __str__(self):
        return "ERROR: " + str(self.args[0])
