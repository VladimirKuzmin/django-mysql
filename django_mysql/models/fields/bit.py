# -*- coding:utf-8 -*-
from django.db.models import BooleanField, NullBooleanField
from django.utils import six

from django_mysql.shims import field_class

__all__ = ('Bit1BooleanField', 'NullBit1BooleanField',)


class Bit1Mixin(object):
    def db_type(self, connection):
        return 'bit(1)'

    def to_python(self, value):
        # Meant to be binary/bytes but can come back as unicode strings
        if isinstance(value, six.binary_type):
            value = (value == b'\x01')
        elif isinstance(value, six.text_type):
            value = (value == '\x01')
        return value

    def from_db_value(self, value, expression, connection, context):
        # Meant to be binary/bytes but can come back as unicode strings
        if isinstance(value, six.binary_type):
            value = (value == b'\x01')
        elif isinstance(value, six.text_type):
            value = (value == '\x01')
        return value

    def get_prep_value(self, value):
        if value is None:
            return value
        else:
            return 1 if value else 0


class Bit1BooleanField(field_class(Bit1Mixin, BooleanField)):
    pass


class NullBit1BooleanField(field_class(Bit1Mixin, NullBooleanField)):
    pass