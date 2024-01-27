from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TeamViewSet, UserDetails, get_my_team, add_member, upgrade_plan, get_stripe_pub_key

router = DefaultRouter()
router.register('teams', TeamViewSet, basename='teams')

urlpatterns = [
    path("teams/member/<int:pk>/", UserDetails.as_view(), name="user_details"),
    path('teams/get_my_team/', get_my_team, name='get_my_team'),
    path('teams/add_member/', add_member, name='add_member'),
    path("teams/upgrade_plan/", upgrade_plan, name="upgrade_plan"),
    path("teams/get_stripe_pub_key/", get_stripe_pub_key, name="get_stripe_pub_key"),
    path('', include(router.urls))
]
