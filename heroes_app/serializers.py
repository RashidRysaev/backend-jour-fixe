from rest_framework import serializers

from .models import Hero, Team


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'


class HeroSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = Hero
        fields = '__all__'
