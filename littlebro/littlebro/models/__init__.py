from littlebro.models.generic import Tag, Rating

from littlebro.models.executive import Police, District, Rank

from littlebro.models.judicial import Judge
from littlebro.models.legislative import Legislator

__all__ = [
    'Tag',
    'Rating',

    # Executive models
    'Police',
    'District',
    'Rank',

    # Judicial models
    'Judge',

    # Legislative models
    'Legislator'
]