# API

from rest_framework import serializers
from .models import Reestr_1
from SANZ_1.models import SEZ1


class Reestr1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Reestr_1
        fields = ['namber', 'date_creation', 'date_rendering', 'vid', 'predpr', 'dejat','fact_adr','adres_Applicant','Otd','sp','Vip','Prim']




class EmailSerializer(serializers.Serializer):
    resipient = serializers.EmailField()
    subject = serializers.CharField(max_length=200)
    content = serializers.CharField(max_length=200)