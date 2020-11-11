# Install
```shell script
pip install -U namekox-security
```

# Example
```python
# ! -*- coding: utf-8 -*-
#
# author: forcemain@163.com


import time
import random


from namekox_timer.core.entrypoints.timer import timer
from namekox_security.core.dependencies.jwt import JWTHelper


class Ping(object):
    name = 'ping'

    jwt = JWTHelper()

    @timer(5)
    def test_me(self):
        data = {'user_id': 1}
        # jwt
        encrypt_jwt = self.jwt.encrypt_jwt(data)
        decrypt_jwt = self.jwt.decrypt_jwt(encrypt_jwt)
        print('Jwt:')
        print('{} -> {} -> {}'.format(data, encrypt_jwt, decrypt_jwt))
        # timed jwt
        encrypt_timed_jwt = self.jwt.encrypt_timed_jwt(data, expire=2)
        sleep_time = random.randint(1, 3)
        time.sleep(sleep_time)
        decrypt_timed_jwt = self.jwt.decrypt_timed_jwt(encrypt_timed_jwt)
        print('Timed jwt: sleep {}s'.format(sleep_time))
        print('{} -> {} -> {}'.format(data, encrypt_timed_jwt, decrypt_timed_jwt))

        # uri
        encrypt_uri = self.jwt.encrypt_uri(data)
        decrypt_uri = self.jwt.decrypt_uri(encrypt_uri)
        print('Uri:')
        print('{} -> {} -> {}'.format(data, encrypt_uri, decrypt_uri))
        # timed uri
        encrypt_timed_uri = self.jwt.encrypt_timed_uri(data)
        sleep_time = random.randint(1, 3)
        time.sleep(sleep_time)
        decrypt_timed_uri = self.jwt.decrypt_timed_uri(encrypt_timed_uri, maxage=2)
        print('Timed uri: sleep {}s'.format(sleep_time))
        print('{} -> {} -> {}'.format(data, encrypt_timed_uri, decrypt_timed_uri))
```

# Running
> config.yaml
```yaml
SECURITY:
  jwt:
    secret: namekox
    expire: 86400
    maxage: 1800
```
> namekox run ping
```shell script
2020-11-11 11:59:52,137 DEBUG load container class from namekox_core.core.service.container:ServiceContainer
2020-11-11 11:59:52,137 DEBUG starting services ['ping']
2020-11-11 11:59:52,138 DEBUG starting service ping entrypoints [ping:namekox_timer.core.entrypoints.timer.Timer:test_me]
2020-11-11 11:59:52,138 DEBUG spawn manage thread handle ping:namekox_timer.core.entrypoints.timer:_run(args=(), kwargs={}, tid=_run)
2020-11-11 11:59:52,139 DEBUG service ping entrypoints [ping:namekox_timer.core.entrypoints.timer.Timer:test_me] started
2020-11-11 11:59:52,139 DEBUG starting service ping dependencies [ping:namekox_security.core.dependencies.jwt.JWTHelper:jwt]
2020-11-11 11:59:52,139 DEBUG service ping dependencies [ping:namekox_security.core.dependencies.jwt.JWTHelper:jwt] started
2020-11-11 11:59:52,139 DEBUG services ['ping'] started
2020-11-11 11:59:57,143 DEBUG spawn worker thread handle ping:test_me(args=(), kwargs={}, context=None)
Jwt:
{'user_id': 1} -> eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxfQ.nIfgHcg7Ur-hXl8pha0DIPgucj17lZMfHgC_ESWk8I76QVg736M87n2xmFmkemYXdxRnATsFqZSuebkvUqmJjw -> {u'user_id': 1}
Timed jwt: sleep 2s
{'user_id': 1} -> eyJhbGciOiJIUzUxMiIsImV4cCI6MTYwNTA2NzIwOSwiaWF0IjoxNjA1MDY3MjA3fQ.eyJ1c2VyX2lkIjoxfQ.Wl6y7WoZkmSEi3t1J8jjQiYyDxacG-FEfYDhMcHqmSHkqTlvy7imQXzFsUwWQTR_crrgmfrTXssyLayIQbOPnw -> {u'user_id': 1}
Uri:
{'user_id': 1} -> eyJ1c2VyX2lkIjoxfQ.406796ta4fm6wtpGt5Pxdttz36o -> {u'user_id': 1}
Timed uri: sleep 2s
{'user_id': 1} -> eyJ1c2VyX2lkIjoxfQ.X6thyQ.Ve6QlFxbFZ7bv3DB2EAfkQ7PaII -> {u'user_id': 1}
2020-11-11 12:00:12,143 DEBUG spawn worker thread handle ping:test_me(args=(), kwargs={}, context=None)
^C2020-11-11 12:00:25,516 DEBUG stopping services ['ping']
2020-11-11 12:00:25,517 DEBUG stopping service ping entrypoints [ping:namekox_timer.core.entrypoints.timer.Timer:test_me]
2020-11-11 12:00:25,517 DEBUG wait service ping entrypoints [ping:namekox_timer.core.entrypoints.timer.Timer:test_me] stop
2020-11-11 12:00:25,517 DEBUG service ping entrypoints [ping:namekox_timer.core.entrypoints.timer.Timer:test_me] stopped
2020-11-11 12:00:25,517 DEBUG stopping service ping dependencies [ping:namekox_security.core.dependencies.jwt.JWTHelper:jwt]
2020-11-11 12:00:25,518 DEBUG service ping dependencies [ping:namekox_security.core.dependencies.jwt.JWTHelper:jwt] stopped
2020-11-11 12:00:25,518 DEBUG services ['ping'] stopped
2020-11-11 12:00:25,518 DEBUG killing services ['ping']
2020-11-11 12:00:25,518 DEBUG service ping already stopped
2020-11-11 12:00:25,518 DEBUG services ['ping'] killed
```
