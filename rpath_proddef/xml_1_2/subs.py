#!/usr/bin/env python

#
# Generated  by generateDS.py.
#

import sys
from string import lower as str_lower
from xml.dom import minidom

import supers as supermod

#
# Globals
#

ExternalEncoding = 'utf-8'

#
# Data representation classes
#

class stageTypeSub(supermod.stageType):
    def __init__(self, labelSuffix=None, name=None, valueOf_=''):
        supermod.stageType.__init__(self, labelSuffix, name, valueOf_)
supermod.stageType.subclass = stageTypeSub
# end class stageTypeSub


class stageListTypeSub(supermod.stageListType):
    def __init__(self, stage=None):
        supermod.stageListType.__init__(self, stage)
supermod.stageListType.subclass = stageListTypeSub
# end class stageListTypeSub


class searchPathTypeSub(supermod.searchPathType):
    def __init__(self, troveName=None, version=None, label=None, valueOf_=''):
        supermod.searchPathType.__init__(self, troveName, version, label, valueOf_)
supermod.searchPathType.subclass = searchPathTypeSub
# end class searchPathTypeSub


class searchPathListTypeSub(supermod.searchPathListType):
    def __init__(self, searchPath=None):
        supermod.searchPathListType.__init__(self, searchPath)
supermod.searchPathListType.subclass = searchPathListTypeSub
# end class searchPathListTypeSub


class factorySourceListTypeSub(supermod.factorySourceListType):
    def __init__(self, factorySource=None):
        supermod.factorySourceListType.__init__(self, factorySource)
supermod.factorySourceListType.subclass = factorySourceListTypeSub
# end class factorySourceListTypeSub


class amiImageTypeSub(supermod.amiImageType):
    def __init__(self, autoResolve=None, freespace=None, name=None, baseFileName=None, installLabelPath=None, amiHugeDiskMountpoint=None, valueOf_=''):
        supermod.amiImageType.__init__(self, autoResolve, freespace, name, baseFileName, installLabelPath, amiHugeDiskMountpoint, valueOf_)
supermod.amiImageType.subclass = amiImageTypeSub
# end class amiImageTypeSub


class applianceIsoImageTypeSub(supermod.applianceIsoImageType):
    def __init__(self, maxIsoSize=None, autoResolve=None, bugsUrl=None, name=None, anacondaCustomTrove=None, betaNag=None, mediaTemplateTrove=None, installLabelPath=None, anacondaTemplatesTrove=None, baseFileName=None, showMediaCheck=None, valueOf_=''):
        supermod.applianceIsoImageType.__init__(self, maxIsoSize, autoResolve, bugsUrl, name, anacondaCustomTrove, betaNag, mediaTemplateTrove, installLabelPath, anacondaTemplatesTrove, baseFileName, showMediaCheck, valueOf_)
supermod.applianceIsoImageType.subclass = applianceIsoImageTypeSub
# end class applianceIsoImageTypeSub


class installableIsoImageTypeSub(supermod.installableIsoImageType):
    def __init__(self, maxIsoSize=None, autoResolve=None, bugsUrl=None, name=None, anacondaCustomTrove=None, betaNag=None, mediaTemplateTrove=None, installLabelPath=None, anacondaTemplatesTrove=None, baseFileName=None, showMediaCheck=None, valueOf_=''):
        supermod.installableIsoImageType.__init__(self, maxIsoSize, autoResolve, bugsUrl, name, anacondaCustomTrove, betaNag, mediaTemplateTrove, installLabelPath, anacondaTemplatesTrove, baseFileName, showMediaCheck, valueOf_)
supermod.installableIsoImageType.subclass = installableIsoImageTypeSub
# end class installableIsoImageTypeSub


class liveIsoImageTypeSub(supermod.liveIsoImageType):
    def __init__(self, autoResolve=None, name=None, zisofs=None, baseFileName=None, unionfs=None, installLabelPath=None, valueOf_=''):
        supermod.liveIsoImageType.__init__(self, autoResolve, name, zisofs, baseFileName, unionfs, installLabelPath, valueOf_)
supermod.liveIsoImageType.subclass = liveIsoImageTypeSub
# end class liveIsoImageTypeSub


class netbootImageTypeSub(supermod.netbootImageType):
    def __init__(self, autoResolve=None, baseFileName=None, installLabelPath=None, name=None, valueOf_=''):
        supermod.netbootImageType.__init__(self, autoResolve, baseFileName, installLabelPath, name, valueOf_)
supermod.netbootImageType.subclass = netbootImageTypeSub
# end class netbootImageTypeSub


class rawFsImageTypeSub(supermod.rawFsImageType):
    def __init__(self, autoResolve=None, freespace=None, name=None, swapSize=None, baseFileName=None, installLabelPath=None, valueOf_=''):
        supermod.rawFsImageType.__init__(self, autoResolve, freespace, name, swapSize, baseFileName, installLabelPath, valueOf_)
supermod.rawFsImageType.subclass = rawFsImageTypeSub
# end class rawFsImageTypeSub


class rawHdImageTypeSub(supermod.rawHdImageType):
    def __init__(self, autoResolve=None, freespace=None, name=None, swapSize=None, baseFileName=None, installLabelPath=None, valueOf_=''):
        supermod.rawHdImageType.__init__(self, autoResolve, freespace, name, swapSize, baseFileName, installLabelPath, valueOf_)
supermod.rawHdImageType.subclass = rawHdImageTypeSub
# end class rawHdImageTypeSub


class tarballImageTypeSub(supermod.tarballImageType):
    def __init__(self, autoResolve=None, baseFileName=None, installLabelPath=None, name=None, swapSize=None, valueOf_=''):
        supermod.tarballImageType.__init__(self, autoResolve, baseFileName, installLabelPath, name, swapSize, valueOf_)
supermod.tarballImageType.subclass = tarballImageTypeSub
# end class tarballImageTypeSub


class updateIsoImageTypeSub(supermod.updateIsoImageType):
    def __init__(self, mediaTemplateTrove=None, baseFileName=None, valueOf_=''):
        supermod.updateIsoImageType.__init__(self, mediaTemplateTrove, baseFileName, valueOf_)
supermod.updateIsoImageType.subclass = updateIsoImageTypeSub
# end class updateIsoImageTypeSub


class vhdImageTypeSub(supermod.vhdImageType):
    def __init__(self, autoResolve=None, freespace=None, name=None, vhdDiskType=None, swapSize=None, baseFileName=None, installLabelPath=None, valueOf_=''):
        supermod.vhdImageType.__init__(self, autoResolve, freespace, name, vhdDiskType, swapSize, baseFileName, installLabelPath, valueOf_)
supermod.vhdImageType.subclass = vhdImageTypeSub
# end class vhdImageTypeSub


class virtualIronImageTypeSub(supermod.virtualIronImageType):
    def __init__(self, autoResolve=None, freespace=None, name=None, vhdDiskType=None, swapSize=None, baseFileName=None, installLabelPath=None, valueOf_=''):
        supermod.virtualIronImageType.__init__(self, autoResolve, freespace, name, vhdDiskType, swapSize, baseFileName, installLabelPath, valueOf_)
supermod.virtualIronImageType.subclass = virtualIronImageTypeSub
# end class virtualIronImageTypeSub


class vmwareEsxImageTypeSub(supermod.vmwareEsxImageType):
    def __init__(self, autoResolve=None, freespace=None, name=None, natNetworking=None, vmMemory=None, swapSize=None, installLabelPath=None, baseFileName=None, valueOf_=''):
        supermod.vmwareEsxImageType.__init__(self, autoResolve, freespace, name, natNetworking, vmMemory, swapSize, installLabelPath, baseFileName, valueOf_)
supermod.vmwareEsxImageType.subclass = vmwareEsxImageTypeSub
# end class vmwareEsxImageTypeSub


class vmwareImageTypeSub(supermod.vmwareImageType):
    def __init__(self, autoResolve=None, freespace=None, name=None, natNetworking=None, vmMemory=None, swapSize=None, diskAdapter=None, installLabelPath=None, baseFileName=None, vmSnapshots=None, valueOf_=''):
        supermod.vmwareImageType.__init__(self, autoResolve, freespace, name, natNetworking, vmMemory, swapSize, diskAdapter, installLabelPath, baseFileName, vmSnapshots, valueOf_)
supermod.vmwareImageType.subclass = vmwareImageTypeSub
# end class vmwareImageTypeSub


class xenOvaImageTypeSub(supermod.xenOvaImageType):
    def __init__(self, autoResolve=None, freespace=None, name=None, vmMemory=None, swapSize=None, baseFileName=None, installLabelPath=None, valueOf_=''):
        supermod.xenOvaImageType.__init__(self, autoResolve, freespace, name, vmMemory, swapSize, baseFileName, installLabelPath, valueOf_)
supermod.xenOvaImageType.subclass = xenOvaImageTypeSub
# end class xenOvaImageTypeSub


class buildDefinitionTypeSub(supermod.buildDefinitionType):
    def __init__(self, build_=None):
        supermod.buildDefinitionType.__init__(self, build_)
supermod.buildDefinitionType.subclass = buildDefinitionTypeSub
# end class buildDefinitionTypeSub


class buildTypeSub(supermod.buildType):
    def __init__(self, baseFlavor=None, flavor=None, architectureRef=None, imageTemplateRef=None, name=None, amiImage=None, applianceIsoImage=None, installableIsoImage=None, liveIsoImage=None, netbootImage=None, rawFsImage=None, rawHdImage=None, tarballImage=None, updateIsoImage=None, vhdImage=None, virtualIronImage=None, vmwareImage=None, vmwareEsxImage=None, xenOvaImage=None, stage=None, imageGroup=None):
        supermod.buildType.__init__(self, baseFlavor, flavor, architectureRef, imageTemplateRef, name, amiImage, applianceIsoImage, installableIsoImage, liveIsoImage, netbootImage, rawFsImage, rawHdImage, tarballImage, updateIsoImage, vhdImage, virtualIronImage, vmwareImage, vmwareEsxImage, xenOvaImage, stage, imageGroup)
supermod.buildType.subclass = buildTypeSub
# end class buildTypeSub


class stageSub(supermod.stage):
    def __init__(self, ref=None, valueOf_=''):
        supermod.stage.__init__(self, ref, valueOf_)
supermod.stage.subclass = stageSub
# end class stageSub


class platformDefinitionTypeSub(supermod.platformDefinitionType):
    def __init__(self, version=None, baseFlavor=None, searchPaths=None, factorySources=None, architectures=None, imageTemplates=None):
        supermod.platformDefinitionType.__init__(self, version, baseFlavor, searchPaths, factorySources, architectures, imageTemplates)
supermod.platformDefinitionType.subclass = platformDefinitionTypeSub
# end class platformDefinitionTypeSub


class platformTypeSub(supermod.platformType):
    def __init__(self, sourceTrove=None, useLatest=None, baseFlavor=None, searchPaths=None, factorySources=None, architectures=None, imageTemplates=None):
        supermod.platformType.__init__(self, sourceTrove, useLatest, baseFlavor, searchPaths, factorySources, architectures, imageTemplates)
supermod.platformType.subclass = platformTypeSub
# end class platformTypeSub


class nameFlavorTypeSub(supermod.nameFlavorType):
    def __init__(self, flavor=None, name=None, valueOf_=''):
        supermod.nameFlavorType.__init__(self, flavor, name, valueOf_)
supermod.nameFlavorType.subclass = nameFlavorTypeSub
# end class nameFlavorTypeSub


class architecturesTypeSub(supermod.architecturesType):
    def __init__(self, architecture=None):
        supermod.architecturesType.__init__(self, architecture)
supermod.architecturesType.subclass = architecturesTypeSub
# end class architecturesTypeSub


class imageTemplatesTypeSub(supermod.imageTemplatesType):
    def __init__(self, imageTemplate=None):
        supermod.imageTemplatesType.__init__(self, imageTemplate)
supermod.imageTemplatesType.subclass = imageTemplatesTypeSub
# end class imageTemplatesTypeSub


class productDefinitionSub(supermod.productDefinition):
    def __init__(self, version=None, productName=None, productShortname=None, productDescription=None, productVersion=None, productVersionDescription=None, conaryRepositoryHostname=None, conaryNamespace=None, imageGroup=None, baseFlavor=None, stages=None, searchPaths=None, factorySources=None, architectures=None, imageTemplates=None, buildDefinition=None, platform=None):
        supermod.productDefinition.__init__(self, version, productName, productShortname, productDescription, productVersion, productVersionDescription, conaryRepositoryHostname, conaryNamespace, imageGroup, baseFlavor, stages, searchPaths, factorySources, architectures, imageTemplates, buildDefinition, platform)
supermod.productDefinition.subclass = productDefinitionSub
# end class productDefinitionSub



def parse(inFilename):
    doc = minidom.parse(inFilename)
    rootNode = doc.documentElement
    rootObj = supermod.stageType.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     sys.stdout.write('<?xml version="1.0" ?>\n')
##     rootObj.export(sys.stdout, 0, name_="stageType",
##         namespacedef_='')
    doc = None
    return rootObj


def parseString(inString):
    doc = minidom.parseString(inString)
    rootNode = doc.documentElement
    rootObj = supermod.stageType.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     sys.stdout.write('<?xml version="1.0" ?>\n')
##     rootObj.export(sys.stdout, 0, name_="stageType",
##         namespacedef_='')
    return rootObj


def parseLiteral(inFilename):
    doc = minidom.parse(inFilename)
    rootNode = doc.documentElement
    rootObj = supermod.stageType.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     sys.stdout.write('#from supers import *\n\n')
##     sys.stdout.write('import supers as model_\n\n')
##     sys.stdout.write('rootObj = model_.stageType(\n')
##     rootObj.exportLiteral(sys.stdout, 0, name_="stageType")
##     sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    root = parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


