from rest_framework import mixins, viewsets

class CreateUpdateViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Reusable ViewSet that supports only create, update, and list actions.
    Use this when delete/retrieve operations are not needed.
    """
    pass
