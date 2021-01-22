import arcpy
import pythonaddins

class AB:
    workPath = ""
    Feature = ""

class TollClassRandom(object):
    """Implementation for Random_addin.tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.cursor = 3
        self.shape = 'Rectangle'
    def onMouseDown(self, x, y, button, shift):
        pass
    def onMouseDownMap(self, x, y, button, shift):
        pass
    def onMouseUp(self, x, y, button, shift):
        pass
    def onMouseUpMap(self, x, y, button, shift):
        pass
    def onMouseMove(self, x, y, button, shift):
        pass
    def onMouseMoveMap(self, x, y, button, shift):
        pass
    def onDblClick(self):
        pass
    def onKeyDown(self, keycode, shift):
        pass
    def onKeyUp(self, keycode, shift):
        pass
    def deactivate(self):
        pass
    def onCircle(self, circle_geometry):
        pass
    def onLine(self, line_geometry):
        pass
    def onRectangle(self, rectangle_geometry):
        extent = rectangle_geometry
        arcpy.env.workspace = AB.workPath
        if arcpy.Exists(AB.Feature):
            arcpy.Delete_management(AB.Feature)
            randompts = arcpy.CreateRandomPoints_management(arcpy.env.workspace, AB.Feature, "", rectangle_geometry)
            arcpy.RefreshActiveView()
            return randompts
