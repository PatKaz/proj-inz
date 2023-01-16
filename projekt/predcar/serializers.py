from rest_framework import serializers
from . models import Pred_car

class pred_carSerializers(serializers.ModelSerializer):
	class Meta:
		model=Pred_car
		fields=('mark','model','year','mileage','vol_engine','fuel','province')
