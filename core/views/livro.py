from rest_framework.viewsets import ModelViewSet

from core.models import Livro
from core.serializers.livro import LivroSerializer,  LivroListSerializer,  LivroRetrieveSerializer
class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return LivroListSerializer
        elif self.action == 'retrive':
            return LivroRetrieveSerializer
        return LivroSerializer