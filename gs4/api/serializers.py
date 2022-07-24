from rest_framework import serializers
from api.models import *


class StudentSerializer(serializers.ModelSerializer):
    # def start_with_r(value):
    #     if value[0].lower() !=  'r':
    #         raise serializers.ValidationError('Name should be start with R.')
            
    # name = serializers.CharField(validators=[start_with_r])
    
    class Meta:
        model = Student
        fields = ["id", "name", "roll", "city"]
        
        # This fields are not changeable.
        # read_only_fields = ['name', 'roll']
        # extra_kwargs = {'name': {'read_only':True}}
        
    # def validate_roll(self, value):
    #     if value >= 200:
    #         raise serializers.ValidationError('Seat Full.')
    #     return value
        
    # def validate(self, data):
    #     nm = data.get('name')
    #     ct = data.get('city')
    #     if nm.lower() == 'rohit' and ct.lower() != 'rachi':
    #         raise serializers.ValidationError('City must be rachi')
    #     return data