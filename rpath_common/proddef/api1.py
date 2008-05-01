#
# Copyright (c) 2008 rPath, Inc.
#
# This program is distributed under the terms of the Common Public License,
# version 1.0. A copy of this license should have been distributed with this
# source file in a file called LICENSE. If it is not present, the license
# is always available at http://www.rpath.com/permanent/licenses/CPL-1.0.
#
# This program is distributed in the hope that it will be useful, but
# without any warranty; without even the implied warranty of merchantability
# or fitness for a particular purpose. See the Common Public License for
# full details.
#
"""
The rPath Common Library Module for Product Definition, API version 1

All interfaces in this modules that do not start with a C{_}
character are public interfaces.
"""

__all__ = [ 'ProductDefinition' ]

import StringIO

from rpath_common.xmllib import api1 as xmllib
from rpath_common.proddef import _xmlConstants
from rpath_common.proddef import _imageTypes

class ProductDefinition(object):
    """
    Represents the definition of a product.
    """
    version = '1.0'
    defaultNamespace = _xmlConstants.defaultNamespace
    xmlSchemaNamespace = _xmlConstants.xmlSchemaNamespace
    xmlSchemaLocation = _xmlConstants.xmlSchemaLocation

    def __init__(self, fromStream = None):
        """
        Pass in either a dictionary as constructed in the example below, or an
        xml string to create an instance.
        """

        self._initFields()

        if fromStream:
            if isinstance(fromStream, (str, unicode)):
                fromStream = StringIO.StringIO(fromStream)
            self.parseStream(fromStream)

    def parseStream(self, stream):
        self._initFields()
        binder = xmllib.DataBinder()
        binder.registerType(_ProductDefinition, 'productDefinition')
        xmlObj = binder.parseFile(stream)
        self.baseFlavor = getattr(xmlObj, 'baseFlavor', None)
        self.stages.extend(getattr(xmlObj, 'stages', []))
        self.upstreamSources.extend(getattr(xmlObj, 'upstreamSources', []))
        self.buildDefinition.extend(getattr(xmlObj, 'buildDefinition', []))

    def serialize(self, stream):
        """Serialize the current object"""
        baseFlavor = xmllib.TextNode(name = 'baseFlavor')
        baseFlavor.characters(self.baseFlavor)
        class N(xmllib.BaseNode):
            def iterChildren(slf):
                return [ baseFlavor,
                         self.stages,
                         self.upstreamSources,
                         self.buildDefinition ]
        attrs = {'version' : ProductDefinition.version,
                 'xmlns' : ProductDefinition.defaultNamespace,
                 'xmlns:xsi' : ProductDefinition.xmlSchemaNamespace,
                 "xsi:schemaLocation" : ProductDefinition.xmlSchemaLocation,
        }
        nameSpaces = {}
        n = N(attrs, nameSpaces, name = "productDefinition")
        binder = xmllib.DataBinder()
        stream.write(binder.toXml(n))

    def getBaseFlavor(self):
        return self.baseFlavor

    def setBaseFlavor(self, baseFlavor):
        self.baseFlavor = baseFlavor

    def getStages(self):
        return self.stages

    def addStage(self, name = None, label = None):
        obj = _Stage(name = name, label = label)
        self.stages.append(obj)

    def getUpstreamSources(self):
        return self.upstreamSources

    def addUpstreamSource(self, troveName = None, label = None):
        obj = _UpstreamSource(troveName = troveName, label = label)
        self.upstreamSources.append(obj)

    def getBuildDefinitions(self):
        return self.buildDefinition

    def addBuildDefinition(self, name = None, baseFlavor = None,
                           byDefault = None, imageType = None):
        obj = _Build(name = name, baseFlavor = baseFlavor,
                               byDefault = byDefault, imageType = imageType)
        self.buildDefinition.append(obj)

    def _initFields(self):
        self.baseFlavor = None
        self.stages = _Stages()
        self.upstreamSources = _UpstreamSources()
        self.buildDefinition = _BuildDefinition()

    def _setFromDict(self):
        # Functions to call to set attributes on the root element.
        self._setNameSpace()
        self._setNameSpaceXsi()
        self._setXsiSchemaLocation()
        self._setVersion()

        self.setBaseFlavor(self.elementDict.pop('baseFlavor', ''))

        # Set each of our 3 possible list elements.
        self.setStages(self.elementDict.pop('stages', []))
        self.setUpstreamSources(self.elementDict.pop('upstreamSources', []))
        self.setBuildDefinition(self.elementDict.pop('buildDefinition', []))

        # Merge any remaining items in self.elementDict into the instance's
        # main dictionary, causing them to show up as elements.
        self.xmlobj.__dict__.update(self.elementDict)

    def _setNameSpace(self):
        setattr(self.xmlobj.__class__, 'xmlns',
                'http://www.rpath.com/permanent/pd.xsd')

    def _setNameSpaceXsi(self):
        setattr(self.xmlobj.__class__, 'xmlns:xsi',
                'http://www.w3.org/2001/XMLSchema-instance')

    def _setXsiSchemaLocation(self):
        setattr(self.xmlobj.__class__, 'xsi:schemaLocation',
                'http://www.rpath.com/permanent/pd.xsd pd.xsd')

    def _setVersion(self):
        setattr(self.xmlobj.__class__, 'version', '1.0')

    def _setElemObj(self, elem, name, elementObject):
        """
        Creates an object with an attribute called name set to elementObject.
        Then, sets that object to an attribute called elem on self.xmlobj.

        This method is typically used in conjuction with self._genElemObj to
        set the returned list at the desired location.
        """
        Elem = type('Elem', (object,), {})
        e = Elem()
        setattr(e, name, elementObject)
        setattr(self.xmlobj, elem, [e])

    @staticmethod
    def _genElemObj(elementList):        
        """
        Create an object (using the cls helper function) that has elements set
        as attributes and xml attributes set as class attributes for each item
        in elementList.  Returns the list of objects.
        """
        elementObjList = []

        # For each item in that list, we expect a dict representing the
        # attributes (or possible more child elements).
        for element in elementList:
            # Append an object created from the element dict to elementObjList.
            elementObjList.append(cls(**element))

        return elementObjList

    def toXml(self):
        return self.xmldb.toXml(self.xmlobj, 'productDefinition')

#{ Objects for the representation of ProductDefinition fields
class _List(list):
    def getElementTree(self, parent = None):
        elem = xmllib.createElementTree(self.tag, {}, {}, parent = parent)
        for child in self:
            child.getElementTree(parent = elem)

class _Stages(_List):
    tag = "stages"

class _UpstreamSources(_List):
    tag = "upstreamSources"

class _BuildDefinition(_List):
    tag = "buildDefinition"

class _SerializableObject(xmllib.SerializableObject):
    def _getName(self):
        return self.tag

    def _getLocalNamespaces(self):
        return {}

    def _iterAttributes(self):
        return self._splitData()[0].items()

    def _iterChildren(self):
        return self._splitData()[1]

    def _splitData(self):
        attrs = {}
        children = []
        for fName in self.__slots__:
            fVal = getattr(self, fName)
            if isinstance(fVal, (bool, int, str, unicode)):
                attrs[fName] = fVal
            else:
                children.append(fVal)
        return attrs, children

class _Stage(_SerializableObject):
    __slots__ = [ 'name', 'label' ]
    tag = "stage"

    def __init__(self, name = None, label = None):
        self.name = name
        self.label = label

class _UpstreamSource(_SerializableObject):
    __slots__ = [ 'troveName', 'label' ]
    tag = "upstreamSource"

    def __init__(self, troveName = None, label = None):
        self.troveName = troveName
        self.label = label

class _Build(_SerializableObject):
    __slots__ = [ 'name', 'baseFlavor', 'imageType', 'byDefault' ]
    tag = "build"

    def __init__(self, name = None, baseFlavor = None,
                 imageType = None, byDefault = None):
        self.name = name
        self.baseFlavor = baseFlavor
        self.imageType = imageType
        if byDefault is None:
            byDefault = True
        self.byDefault = byDefault

    def _iterChildren(self):
        yield self.imageType

#}

class _ProductDefinition(xmllib.BaseNode):
    ndNameBaseFlavor = "{%s}%s" % (ProductDefinition.defaultNamespace,
                                   'baseFlavor')
    ndNameStages = "{%s}%s" % (ProductDefinition.defaultNamespace,
                               'stages')
    ndNameUpstreamSources = "{%s}%s" % (ProductDefinition.defaultNamespace,
                                        'upstreamSources')
    ndNameBuildDefinition = "{%s}%s" % (ProductDefinition.defaultNamespace,
                                        'buildDefinition')

    ndNameInstIso = "{%s}%s" % (ProductDefinition.defaultNamespace,
                                'installbleIsoImage')

    ndNameRawFs = "{%s}%s" % (ProductDefinition.defaultNamespace,
                             'rawFsImage')
    ndNameRawHd = "{%s}%s" % (ProductDefinition.defaultNamespace,
                             'rawHdImage')


    def addChild(self, childNode):
        chName = childNode.getAbsoluteName()
        if chName == self.ndNameBaseFlavor:
            self.baseFlavor = childNode.getText()
            return

        if chName == self.ndNameStages:
            children = childNode.getChildren('stage')
            self._addStages(children)
            return

        if chName == self.ndNameUpstreamSources:
            children = childNode.getChildren('upstreamSource')
            self._addUpstreamSources(children)
            return

        if chName == self.ndNameBuildDefinition:
            children = childNode.getChildren('build')
            self._addBuildDefinition(children)
            return

    def _addStages(self, stagesNodes):
        stages = self.stages = []
        for node in stagesNodes:
            # XXX getAttribute should be getAbsoluteAttribute
            pyObj = _Stage(name = node.getAttribute('name'),
                           label = node.getAttribute('label'))
            stages.append(pyObj)

    def _addUpstreamSources(self, upstreamSources):
        sources = self.upstreamSources = []
        for node in upstreamSources:
            pyObj = _UpstreamSource(
                troveName = node.getAttribute('troveName'),
                label = node.getAttribute('label'))
            sources.append(pyObj)

    def _addBuildDefinition(self, buildNodes):
        builds = self.buildDefinition = []
        for node in buildNodes:
            imgType = None
            for subNode in node.iterChildren():
                if not isinstance(subNode, xmllib.BaseNode):
                    continue
                imgType = _imageTypes.ImageType_Dispatcher.dispatch(subNode)
                if imgType is not None:
                    break
            if imgType is None:
                raise Exception("")
            byDefault = node.getAttribute('byDefault')
            if byDefault is None:
                byDefault = True
            else:
                byDefault = byDefault.upper() in ['TRUE', 1] and True or False
            pyobj = _Build(
                baseFlavor = node.getAttribute('baseFlavor'),
                byDefault = byDefault,
                imageType = imgType)
            builds.append(pyobj)
