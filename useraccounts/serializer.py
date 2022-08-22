from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    
    cpassword = serializers.CharField(style={'input_type': 'password'}, write_only=True)
      
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'cpassword']
        extra_kwargs = {
            'password': {'write_only':True}
        }
        
    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        cpassword = self.validated_data['cpassword']
        
        if password != cpassword:
            return serializers.ValidationError({'Message': 'Password mismatch.'})
        
        if User.objects.filter(username=username).exists():
            return serializers.ValidationError({'Message': 'The user already exists.'})
        
        if User.objects.filter(email=email).exists():
            return serializers.ValidationError({'Message': 'Email already exists.'})
        
        accounts = User(username=username, email=email)
        accounts.set_password(password)
        accounts.save()
        
        return accounts