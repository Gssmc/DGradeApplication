
from django.urls import path
from .views import DisplayCleaningMaterialsView,BuyKitView

urlpatterns = [
    path('display_cleaning_materials/',DisplayCleaningMaterialsView,name="display_kit"),
    path('buy_cleaning_kit/<int:user_id>/<int:kit_id>/',BuyKitView, name='buy_cleaning_kit'),

]
