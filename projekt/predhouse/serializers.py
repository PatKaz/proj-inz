from rest_framework import serializers
from . models import Pred_house

class Pred_houseSerializers(serializers.ModelSerializer):
	class Meta:
		model=Pred_house
		fields=('area','room_num','floor','total_floor','year_built','dish_washer','tv_set','washer',
        'balcony','basement','elevator','internet','available_for_students','two_level','garden','district')