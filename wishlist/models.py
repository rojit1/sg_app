from django.db import models
from django.contrib.auth import get_user_model
from places.models import Place

User = get_user_model()

class WishList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user','place'],name="unique fields")
        ]

    def __str__(self):
        return f'{self.place.name}'

