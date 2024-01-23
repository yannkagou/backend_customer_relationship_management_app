from django.contrib.auth.models import User

from rest_framework import viewsets

from .models import Lead
from .serializers import LeadSerializer

from team.models import Team
class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    
    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)
    
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team, created_by=self.request.user)
        
    def perform_update(self, serializer):
        obj = self.get_object()
        
        member_id = self.request_data['assigned_to']
        
        if member_id:
            user = User.objects.get(pk=member_id)
            serializer.save(assigned_to=user)
        else:
            serializer.save()
