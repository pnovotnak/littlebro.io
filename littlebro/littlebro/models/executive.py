from django.db import models
from django.contrib.contenttypes import generic

from generic import Official

POLICE_POTENTIALLY_UNDERCOVER_RANK_ID = 4

class Police(Official):
    """
    An officer of the law
    """
    # Disabled for now, see @save
    #image = models.ImageField(blank=True, null=True)
    badge_number = models.IntegerField()
    district = models.ForeignKey('District')
    rank = models.ForeignKey('Rank')

    class Meta:
        verbose_name_plural = 'Police'

    """
    def save(self, *args, **kwargs):
        '''
        If the Police's rank is under ..._RANK_ID it's potentially unsafe
        to the officer to even store a picture because they may be
        undercover. If this is the case, delete images associated with
        the officer.
        '''
        if self.rank.id > POLICE_POTENTIALLY_UNDERCOVER_RANK_ID:

            try:
                officer = Police.objects.get(pk=self.pk)
                if officer.image:
                    # Get the image
                    storage, path = officer.image.storage, officer.image.path

                    # Remove the image from the model
                    officer.image = None
                    officer.save()

                    # Delete the old image from storage
                    storage.delete(path)

            except Police.DoesNotExist:
                pass

            # Delete the new image from storage
            storage, path = self.image.storage, self.image.path

            # Wipe the instance variable
            self.image = None

        super(Police, self).save(*args, **kwargs)
    """

class District(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Rank(models.Model):
    title = models.CharField(max_length=255)
    rank = models.PositiveSmallIntegerField()
    district = models.ForeignKey('District')

    class Meta:
        ordering = [
            'rank'
        ]

    def __str__(self):
        return self.title
