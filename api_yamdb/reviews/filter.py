import django_filters

from .models import Title


class TitleFilter(django_filters.FilterSet):
    genre = django_filters.filters.CharFilter(
        field_name='genre__slug',
        lookup_expr='icontains'
    )
    category = django_filters.filters.CharFilter(
        field_name='category__slug',
        lookup_expr='icontains'
    )
    name = django_filters.filters.CharFilter(
        field_name='name',
        lookup_expr='icontains'
    )

    class Meta:
        model = Title
        fields = ('name', 'year', 'genre', 'category')
