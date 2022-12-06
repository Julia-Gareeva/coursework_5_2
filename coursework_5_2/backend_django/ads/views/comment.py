from rest_framework.viewsets import ModelViewSet
from coursework_5_2.backend_django.ads.models import Comment, Ad
from coursework_5_2.backend_django.ads.serializers import CommentSerializer, CommentListSerializer, CommentCreateSerializer
from coursework_5_2.backend_django.ads.permissions import UserPermissions


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    serializer_action_classes = {
        'list': CommentListSerializer,
        'retrieve': CommentListSerializer,
        'create': CommentCreateSerializer,
        'update': CommentCreateSerializer,
    }

    permission_classes = (UserPermissions,)

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs['ad_id'])

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def perform_create(self, serializer):
        ad = Ad.objects.get(pk=self.kwargs['ad_id'])
        serializer.save(author=self.request.user, ad=ad)
