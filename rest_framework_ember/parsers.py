"""
Parsers
"""
from rest_framework.parsers import JSONParser
from rest_framework_ember.utils import get_resource_name

from .utils import format_keys


class EmberJSONParser(JSONParser):
    """
    By default, EmberJS sends a payload that looks like the following::

        {
            "identity": {
                "id": 1,
                "first_name": "John",
                "last_name": "Coltrane"
            }
        }

    So we can work with the grain on both Ember and RestFramework,
    Do some tweaks to the payload so DRF gets what it expects.
    """
    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as JSON and returns the resulting data
        """
        result = super(EmberJSONParser, self).parse(stream, media_type=None,
                                                    parser_context=None)
        resource = result.get(get_resource_name(parser_context.get('view', None)))
        return format_keys(resource, 'underscore')
