import unittest
from base import FunctionalTestCase

class TestSetup(FunctionalTestCase):
    
    def afterSetUp(self):
        self.jsregistry = self.portal.portal_javascripts
    
    def test_jsregistry(self):
        self.failUnless(False, "TODO")

    def test_cssregistry(self):
        self.failUnless(False, "TODO")

    def test_example(self):
        self.failUnless(False, "TODO")


def test_suite():

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
