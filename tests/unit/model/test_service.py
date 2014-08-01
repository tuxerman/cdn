import ddt
import unittest

from cdn.model import service
from cdn.model.helpers import origin
from cdn.model.helpers import domain
from cdn.model.helpers import cachingrule
from cdn.model.helpers import restriction

from tests.unit import base


@ddt.ddt
class TestService(base.TestCase):

    def test_create_service(self):
        orgns = []
        dmns = []

        orgns.append(origin.Origin('mysite.com'))
        orgns.append(origin.Origin('yoursite.io', port=80, ssl=True))

        dmns.append(domain.Domain('oursite.org'))
        dmns.append(domain.Domain('blah.cc'))

        srvc = service.Service('NewService', dmns, orgns)

        # test all properties
        # name
        with self.assertRaises(AttributeError):
            srvc.name = 'howdareyou'

        # domains
        with self.assertRaises(AttributeError):
            srvc.domains = []

        # origins
        with self.assertRaises(AttributeError):
            srvc.origins = []
