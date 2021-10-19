import unittest
import re
from faker import Faker
from faker.contrib import pytest
from faker.providers import ssn
#from faker.providers.ssn.fi_FI import Provider as fi_Provider


class TestFiFI:
    """ Tests SSN in the fi_FI locale """

    def _init__(self):
        self.faker = Faker()
        Faker.seed(0)
        #self.provider = fi_Provider
        self.faker.add_provider(ssn)


    def test_ssn_sanity(self):
        for age in range(100):
            self.faker.ssn(min_age=age, max_age=age + 1)

    def test_valid_ssn(self):
        ssn = self.faker.ssn()
        print(ssn)
        individual_number = int(ssn[7:10])
        assert individual_number <= 899

    def test_artifical_ssn(self):
        ssn = self.faker.ssn(artificial=True)
        individual_number = int(ssn[7:10])
        assert individual_number >= 900

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r'^FI\d{8}$', self.fake.vat_id())


test = TestFiFI()
test.test_valid_ssn()