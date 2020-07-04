from rest_framework_json_api import serializers
from myapp.models import ActivityPeriod, User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz')

class ActivityPeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')
        
        