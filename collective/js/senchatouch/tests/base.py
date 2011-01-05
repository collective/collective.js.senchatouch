import unittest

from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase import layer

try:
    from Zope2.App import zcml
    from OFS import metaconfigure
    zcml # pyflakes
    metaconfigure
except ImportError:
    from Products.Five import zcml
    from Products.Five import fiveconfigure as metaconfigure

ptc.setupPloneSite(extension_profiles=('collective.js.senchatouch:default',))

class Layer(layer.PloneSite):

    @classmethod
    def setUp(cls):
        metaconfigure.debug_mode = True
        import collective.js.senchatouch
        zcml.load_config('configure.zcml', collective.js.senchatouch)
        metaconfigure.debug_mode = False
        ztc.installPackage('collective.js.senchatouch', quiet=True)

    @classmethod
    def tearDown(cls):
        pass

class TestCase(ptc.PloneTestCase):

    layer = Layer

class FunctionalTestCase(ptc.FunctionalTestCase):
    
    layer = Layer
