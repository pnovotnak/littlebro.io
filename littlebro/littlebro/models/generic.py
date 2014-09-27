from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from littlebro.settings import RATING_STAR_WIDTH


class Tag(models.Model):
    """
    A generic Tag that may be attached to any other model
    """
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __str__(self):              # __unicode__ on Python 2
        return self.tag


class Rating(models.Model):
    """
    A generic Rating that may be attached to any other model
    """
    rating = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __str__(self):              # __unicode__ on Python 2
        return str(self.rating)


class Official(models.Model):
    """
    A generic official class that may be extended with additional attributes
    """

    name = models.CharField(max_length=255)
    ratings = generic.GenericRelation(Rating)

    def rating(self):
        ratings = map(lambda r: r.rating, self.ratings.all())
        average_rating = float(sum(ratings))/len(ratings) if len(ratings) > 0 else None
        print average_rating
        return average_rating

    def rating_star_display(self):
        ratings = map(lambda r: r.rating, self.ratings.all())
        average_rating = float(sum(ratings))/len(ratings) if len(ratings) > 0 else None
        return int(average_rating * RATING_STAR_WIDTH)

    def get_absolute_url(self):
        verbose_name = self.urlize(self.verbose_name_plural())
        return "/%s/%d" % (verbose_name, self.id)

    def __str__(self):
        return self.name

    def verbose_name(self):
        return self._meta.verbose_name.title()

    def verbose_name_plural(self):
        return self._meta.verbose_name_plural.title()

    def urlized_verbose_name(self):
        return self.urlize(self._meta.verbose_name.title())

    def urlized_verbose_name_plural(self):
        return self.urlize(self._meta.verbose_name_plural.title())

    def get_fields(self):
        return [(field.verbose_name, field._get_val_from_obj(self)) for field in self.__class__._meta.fields]

    @staticmethod
    def urlize(title):
        return title.replace(' ', '-').lower()
