from django.db.models import Count, Case, When, Avg, F
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet, GenericViewSet

from store.models import Book, UserBookRelation
from store.permissions import IsOwnerOrStaffOrReadOnly
from store.serializers import BooksSerializer, UserBookRelationSerializer


class BookViewSet(ModelViewSet):
    queryset = (Book.objects.all().annotate(
        annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
        final_price=F('price') - F('discount')).select_related('owner')
                .prefetch_related('readers').order_by('id'))

    serializer_class = BooksSerializer
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['price', 'discount']
    search_fields = ['name', 'author_name']
    ordering_fields = ['price', 'author_name', 'final_price']

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class UserBooksRelationView(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserBookRelation.objects.all()
    serializer_class = UserBookRelationSerializer
    lookup_field = 'book'

    def get_object(self):
        obj, _ = UserBookRelation.objects.get_or_create(user=self.request.user,
                                                        book_id=self.kwargs[
                                                            'book'])

        return obj


def auth(request):
    return render(request, 'oauth.html')
