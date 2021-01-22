import arcpy
import pythonaddins

class AB:
    workPath = ""
    listLayer = []
    ClipFeat = ""
    ClipCont = ""


class ButtonClass1(object):
    """Implementation for ADD_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        AB.workPath = pythonaddins.OpenDialog("选择存储路径")
        pass


class ButtonClass5(object):
    """Implementation for ADD_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = arcpy.mapping.MapDocument('current')
        df = arcpy.mapping.ListDataFrames(mxd, "图层")[0]
        resultFeats = AB.workPath + "/" + AB.ClipFeat
        arcpy.analysis.Clip(AB.ClipCont, AB.ClipFeat, resultFeats)


class ComboBoxClass3(object):
    """Implementation for ADD_addin.combobox (ComboBox)"""
    def __init__(self):
        mxd = arcpy.mapping.MapDocument('current')
        df = arcpy.mapping.ListDataFrames(mxd, "图层")[0]
        for lyr in arcpy.mapping.ListLayers(mxd, "", df):
            AB.listLayer.append(lyr.name)
        self.items = AB.listLayer
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWW'
        self.width = 'WWWWWW'
    def onSelChange(self, selection):
        AB.ClipFeat = selection
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        pass
    def onEnter(self):
        pass
    def refresh(self):
        pass


class ComboBoxClass4(object):
    """Implementation for ADD_addin.combobox_1 (ComboBox)"""
    def __init__(self):
        mxd = arcpy.mapping.MapDocument('current')
        df = arcpy.mapping.ListDataFrames(mxd, "图层")[0]
        for lyr in arcpy.mapping.ListLayers(mxd, "", df):
            AB.listLayer.append(lyr.name)
        self.items = AB.listLayer
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWW'
        self.width = 'WWWWWW'
    def onSelChange(self, selection):
        AB.ClipCont = selection
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        pass
    def onEnter(self):
        pass
    def refresh(self):
        pass
