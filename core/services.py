"""
Base service class for handling business logic.

It helps separate data processing from views or serializers,
keeping the architecture clean and maintainable.
"""

class BaseService:
    def __init__(self, user):
        self.user = user