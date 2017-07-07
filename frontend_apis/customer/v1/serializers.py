from rest_framework import serializers

from customer import models


class DataLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DataLog
