#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import unicode_literals

import hashlib


from logging import getLogger
from namekox_core.core.friendly import AsLazyProperty
from namekox_security.constants import SECURITY_CONFIG_KEY
from namekox_core.core.service.dependency import Dependency


logger = getLogger(__name__)


class MD5Helper(Dependency):
    def __init__(self, *args, **kwargs):
        super(MD5Helper, self).__init__(*args, **kwargs)

    @AsLazyProperty
    def config(self):
        return self.container.config.get(SECURITY_CONFIG_KEY, {}).get('md5', {})

    def encrypt(self, data):
        md5 = hashlib.md5()
        md5.update(data)
        return md5.hexdigest()
