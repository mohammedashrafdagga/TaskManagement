from rest_framework import serializers
from .models import Task
from django.utils.text import slugify


class TaskSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date',
                  'assigned_to', 'slug', 'status']

    def validate_slug(self, slug):
        if Task.objects.filter(slug=slug).exists():
            raise serializers.ValidationError(
                {'message': 'The Task you Are create Already exists'}
            )
        return slug

    def create(self, validated_data):
        validated_data['team'] = self.context['team']
        slug = slugify(validated_data.get('title'))
        validated_data['slug'] = self.validate_slug(slug)
        return super().create(validated_data)
