# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gnm', [dirname(__file__)])
        except ImportError:
            import _gnm
            return _gnm
        if fp is not None:
            try:
                _mod = imp.load_module('_gnm', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _gnm = swig_import_helper()
    del swig_import_helper
else:
    import _gnm
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method: return method(self, value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)

def _swig_getattr(self, class_type, name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def GetUseExceptions(*args):
  return _gnm.GetUseExceptions(*args)
GetUseExceptions = _gnm.GetUseExceptions

def UseExceptions(*args):
  return _gnm.UseExceptions(*args)
UseExceptions = _gnm.UseExceptions

def DontUseExceptions(*args):
  return _gnm.DontUseExceptions(*args)
DontUseExceptions = _gnm.DontUseExceptions
class MajorObject(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MajorObject, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MajorObject, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def GetDescription(self, *args): return _gnm.MajorObject_GetDescription(self, *args)
    def SetDescription(self, *args): return _gnm.MajorObject_SetDescription(self, *args)
    def GetMetadataDomainList(self, *args): return _gnm.MajorObject_GetMetadataDomainList(self, *args)
    def GetMetadata_Dict(self, *args): return _gnm.MajorObject_GetMetadata_Dict(self, *args)
    def GetMetadata_List(self, *args): return _gnm.MajorObject_GetMetadata_List(self, *args)
    def SetMetadata(self, *args): return _gnm.MajorObject_SetMetadata(self, *args)
    def GetMetadataItem(self, *args): return _gnm.MajorObject_GetMetadataItem(self, *args)
    def SetMetadataItem(self, *args): return _gnm.MajorObject_SetMetadataItem(self, *args)
MajorObject_swigregister = _gnm.MajorObject_swigregister
MajorObject_swigregister(MajorObject)

GATDijkstraShortestPath = _gnm.GATDijkstraShortestPath
GATKShortestPath = _gnm.GATKShortestPath
GATConnectedComponents = _gnm.GATConnectedComponents
GNM_EDGE_DIR_BOTH = _gnm.GNM_EDGE_DIR_BOTH
GNM_EDGE_DIR_SRCTOTGT = _gnm.GNM_EDGE_DIR_SRCTOTGT
GNM_EDGE_DIR_TGTTOSRC = _gnm.GNM_EDGE_DIR_TGTTOSRC

def CastToNetwork(*args):
  """CastToNetwork(MajorObject base) -> Network"""
  return _gnm.CastToNetwork(*args)

def CastToGenericNetwork(*args):
  """CastToGenericNetwork(MajorObject base) -> GenericNetwork"""
  return _gnm.CastToGenericNetwork(*args)
class Network(MajorObject):
    """Proxy of C++ GNMNetworkShadow class"""
    __swig_setmethods__ = {}
    for _s in [MajorObject]: __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Network, name, value)
    __swig_getmethods__ = {}
    for _s in [MajorObject]: __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Network, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _gnm.delete_Network
    __del__ = lambda self : None;
    def ReleaseResultSet(self, *args):
        """ReleaseResultSet(Network self, OGRLayerShadow * layer)"""
        return _gnm.Network_ReleaseResultSet(self, *args)

    def GetVersion(self, *args):
        """GetVersion(Network self) -> int"""
        return _gnm.Network_GetVersion(self, *args)

    def GetName(self, *args):
        """GetName(Network self) -> char const *"""
        return _gnm.Network_GetName(self, *args)

    def GetFeatureByGlobalFID(self, *args):
        """GetFeatureByGlobalFID(Network self, GIntBig GFID) -> OGRFeatureShadow *"""
        return _gnm.Network_GetFeatureByGlobalFID(self, *args)

    def GetPath(self, *args, **kwargs):
        """GetPath(Network self, GIntBig nStartFID, GIntBig nEndFID, GNMGraphAlgorithmType eAlgorithm, char ** options=None) -> OGRLayerShadow *"""
        return _gnm.Network_GetPath(self, *args, **kwargs)

    def DisconnectAll(self, *args):
        """DisconnectAll(Network self) -> CPLErr"""
        return _gnm.Network_DisconnectAll(self, *args)

    def GetProjection(self, *args):
        """GetProjection(Network self) -> char const *"""
        return _gnm.Network_GetProjection(self, *args)

    def GetProjectionRef(self, *args):
        """GetProjectionRef(Network self) -> char const *"""
        return _gnm.Network_GetProjectionRef(self, *args)

    def GetFileList(self, *args):
        """GetFileList(Network self) -> char **"""
        return _gnm.Network_GetFileList(self, *args)

    def CreateLayer(self, *args, **kwargs):
        """
        CreateLayer(Network self, char const * name, OSRSpatialReferenceShadow * srs=None, OGRwkbGeometryType geom_type=wkbUnknown, 
            char ** options=None) -> OGRLayerShadow *
        """
        return _gnm.Network_CreateLayer(self, *args, **kwargs)

    def CopyLayer(self, *args, **kwargs):
        """CopyLayer(Network self, OGRLayerShadow * src_layer, char const * new_name, char ** options=None) -> OGRLayerShadow *"""
        return _gnm.Network_CopyLayer(self, *args, **kwargs)

    def DeleteLayer(self, *args):
        """DeleteLayer(Network self, int index) -> OGRErr"""
        return _gnm.Network_DeleteLayer(self, *args)

    def GetLayerCount(self, *args):
        """GetLayerCount(Network self) -> int"""
        return _gnm.Network_GetLayerCount(self, *args)

    def GetLayerByIndex(self, *args):
        """GetLayerByIndex(Network self, int index=0) -> OGRLayerShadow *"""
        return _gnm.Network_GetLayerByIndex(self, *args)

    def GetLayerByName(self, *args):
        """GetLayerByName(Network self, char const * layer_name) -> OGRLayerShadow *"""
        return _gnm.Network_GetLayerByName(self, *args)

    def TestCapability(self, *args):
        """TestCapability(Network self, char const * cap) -> bool"""
        return _gnm.Network_TestCapability(self, *args)

    def StartTransaction(self, *args, **kwargs):
        """StartTransaction(Network self, int force=False) -> OGRErr"""
        return _gnm.Network_StartTransaction(self, *args, **kwargs)

    def CommitTransaction(self, *args):
        """CommitTransaction(Network self) -> OGRErr"""
        return _gnm.Network_CommitTransaction(self, *args)

    def RollbackTransaction(self, *args):
        """RollbackTransaction(Network self) -> OGRErr"""
        return _gnm.Network_RollbackTransaction(self, *args)

Network_swigregister = _gnm.Network_swigregister
Network_swigregister(Network)

class GenericNetwork(Network):
    """Proxy of C++ GNMGenericNetworkShadow class"""
    __swig_setmethods__ = {}
    for _s in [Network]: __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GenericNetwork, name, value)
    __swig_getmethods__ = {}
    for _s in [Network]: __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GenericNetwork, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _gnm.delete_GenericNetwork
    __del__ = lambda self : None;
    def ConnectFeatures(self, *args):
        """
        ConnectFeatures(GenericNetwork self, GIntBig nSrcFID, GIntBig nTgtFID, GIntBig nConFID, double dfCost, double dfInvCost, 
            GNMDirection eDir) -> CPLErr
        """
        return _gnm.GenericNetwork_ConnectFeatures(self, *args)

    def DisconnectFeatures(self, *args):
        """DisconnectFeatures(GenericNetwork self, GIntBig nSrcFID, GIntBig nTgtFID, GIntBig nConFID) -> CPLErr"""
        return _gnm.GenericNetwork_DisconnectFeatures(self, *args)

    def DisconnectFeaturesWithId(self, *args):
        """DisconnectFeaturesWithId(GenericNetwork self, GIntBig nFID) -> CPLErr"""
        return _gnm.GenericNetwork_DisconnectFeaturesWithId(self, *args)

    def ReconnectFeatures(self, *args):
        """
        ReconnectFeatures(GenericNetwork self, GIntBig nSrcFID, GIntBig nTgtFID, GIntBig nConFID, double dfCost, double dfInvCost, 
            GNMDirection eDir) -> CPLErr
        """
        return _gnm.GenericNetwork_ReconnectFeatures(self, *args)

    def CreateRule(self, *args):
        """CreateRule(GenericNetwork self, char const * pszRuleStr) -> CPLErr"""
        return _gnm.GenericNetwork_CreateRule(self, *args)

    def DeleteAllRules(self, *args):
        """DeleteAllRules(GenericNetwork self) -> CPLErr"""
        return _gnm.GenericNetwork_DeleteAllRules(self, *args)

    def DeleteRule(self, *args):
        """DeleteRule(GenericNetwork self, char const * pszRuleStr) -> CPLErr"""
        return _gnm.GenericNetwork_DeleteRule(self, *args)

    def GetRules(self, *args):
        """GetRules(GenericNetwork self) -> char **"""
        return _gnm.GenericNetwork_GetRules(self, *args)

    def ConnectPointsByLines(self, *args, **kwargs):
        """ConnectPointsByLines(GenericNetwork self, char ** papszLayerList, double dfTolerance, double dfCost, double dfInvCost, GNMDirection eDir) -> CPLErr"""
        return _gnm.GenericNetwork_ConnectPointsByLines(self, *args, **kwargs)

    def ChangeBlockState(self, *args):
        """ChangeBlockState(GenericNetwork self, GIntBig nFID, bool bIsBlock) -> CPLErr"""
        return _gnm.GenericNetwork_ChangeBlockState(self, *args)

    def ChangeAllBlockState(self, *args):
        """ChangeAllBlockState(GenericNetwork self, bool bIsBlock=False) -> CPLErr"""
        return _gnm.GenericNetwork_ChangeAllBlockState(self, *args)

GenericNetwork_swigregister = _gnm.GenericNetwork_swigregister
GenericNetwork_swigregister(GenericNetwork)

# This file is compatible with both classic and new-style classes.


