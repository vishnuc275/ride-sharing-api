from .serializers import RegisterSerializer, RideSerializer, RideStatusSerializer, RideLocationSerializer
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions, status as drf_status
from.models import Ride
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model


class RegisterView(generics.CreateAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(rider = self.request.user)

    def get_queryset(self):
        return Ride.objects.filter(rider = self.request.user)
    
    @action(detail=True, methods=['patch'], url_path='status')
    def update_status(self, request, pk=None):
        ride = self.get_object()
        serializer = RideStatusSerializer(ride, data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Status Updated Succesfully...", "ride":serializer.data})
        return Response(serializer.errors, status= drf_status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['patch'], url_path='accept')
    def accept_ride(self, request):
        user = request.user
        if user.role != 'driver':
            return Response({"detail": "Only drivers can accept rides."}, status=drf_status.HTTP_403_FORBIDDEN)

        # Find the first unassigned ride
        ride = Ride.objects.filter(status='requested', driver__isnull=True).first()

        if not ride:
            return Response({"detail": "No available rides."}, status=drf_status.HTTP_404_NOT_FOUND)

        # Assign the ride to this driver
        ride.driver = user
        ride.status = 'accepted'
        ride.save()

        serializer = self.get_serializer(ride)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['patch'], url_path='location')
    def update_location(self, request, pk=None):
        ride = self.get_object()

        if ride.driver != request.user:
            return Response({"error": "Only the assigned driver can update location."}, status=403)

        serializer = RideLocationSerializer(ride, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "location updated...",
                "current_location": serializer.data['current_location']}, status=drf_status.HTTP_200_OK)
        return Response(serializer.errors, status=drf_status.HTTP_400_BAD_REQUEST)