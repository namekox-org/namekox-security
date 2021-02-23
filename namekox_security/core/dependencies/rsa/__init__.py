#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals


from logging import getLogger
from namekox_core.core.friendly import AsLazyProperty
from namekox_security.constants import SECURITY_CONFIG_KEY
from namekox_core.core.service.dependency import Dependency


logger = getLogger(__name__)


class RSAHelper(Dependency):
    def __init__(self, *args, **kwargs):
        super(RSAHelper, self).__init__(*args, **kwargs)

    @AsLazyProperty
    def config(self):
        return self.container.config.get(SECURITY_CONFIG_KEY, {}).get('rsa', {})

    def encrypt(self, *args, **kwargs):
        pass

    def decrypt(self, *args, **kwargs):
        pass
