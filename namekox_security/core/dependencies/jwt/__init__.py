#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals


from logging import getLogger
from namekox_security.constants import (
    SECURITY_CONFIG_KEY,
    DEFAULT_SECURITY_JWT_SECRET,
    DEFAULT_SECURITY_JWT_EXPIRE,
    DEFAULT_SECURITY_JWT_MAXAGE,
)
from namekox_core.core.friendly import AsLazyProperty
from itsdangerous import URLSafeSerializer as USerializer
from namekox_core.core.service.dependency import Dependency
from itsdangerous import URLSafeTimedSerializer as UTSerializer
from itsdangerous import JSONWebSignatureSerializer as JSerializer
from itsdangerous import TimedJSONWebSignatureSerializer as JTSerializer


logger = getLogger(__name__)


class JWTHelper(Dependency):
    def __init__(self, *args, **kwargs):
        super(JWTHelper, self).__init__(*args, **kwargs)

    @AsLazyProperty
    def config(self):
        return self.container.config.get(SECURITY_CONFIG_KEY, {}).get('jwt', {})

    @AsLazyProperty
    def expire(self):
        return self.config.get('expire', DEFAULT_SECURITY_JWT_EXPIRE)

    @AsLazyProperty
    def maxage(self):
        return self.config.get('maxage', DEFAULT_SECURITY_JWT_MAXAGE)

    @AsLazyProperty
    def secret(self):
        return self.config.get('secret', DEFAULT_SECURITY_JWT_SECRET) or DEFAULT_SECURITY_JWT_SECRET

    def encrypt_jwt(self, data, secret=None, headers=None, **options):
        secret = secret or self.secret
        s = JSerializer(secret, **options)
        return s.dumps(data, header_fields=headers)

    def decrypt_jwt(self, data, secret=None, return_header=False, **options):
        secret = secret or self.secret
        s = JSerializer(secret, **options)
        return s.loads(data, return_header=return_header)

    def encrypt_uri(self, data, secret=None, **options):
        secret = secret or self.secret
        s = USerializer(secret, **options)
        return s.dumps(data)

    def decrypt_uri(self, data, secret=None, **options):
        secret = secret or self.secret
        s = USerializer(secret, **options)
        return s.loads(data)

    def encrypt_timed_jwt(self, data, secret=None, expire=None, headers=None, **options):
        secret = secret or self.secret
        expire = expire or self.expire
        s = JTSerializer(secret, expires_in=expire, **options)
        return s.dumps(data, header_fields=headers)

    def decrypt_timed_jwt(self, data, secret=None, expire=None, return_header=False, **options):
        secret = secret or self.secret
        expire = expire or self.expire
        s = JTSerializer(secret, expires_in=expire, **options)
        return s.loads(data, return_header=return_header)

    def encrypt_timed_uri(self, data, secret=None, **options):
        secret = secret or self.secret
        s = UTSerializer(secret, **options)
        return s.dumps(data)

    def decrypt_timed_uri(self, data, secret=None, maxage=None, return_timestamp=False, **options):
        secret = secret or self.secret
        maxage = maxage or self.maxage
        s = UTSerializer(secret, **options)
        return s.loads(data, max_age=maxage, return_timestamp=return_timestamp)
