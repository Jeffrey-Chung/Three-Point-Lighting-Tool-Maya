#Three Point Lighting Tool
#This tool creates a three point lighting system for a selected object and can adjust light settings

import maya.cmds as cmds

#create a default 90 degree shaped plane in case if a plane isn't already created in the scene
def create_plane():
    poly_plane = cmds.polyPlane(w=10, h=10 )
    cmds.setAttr(poly_plane[0] + '.scaleX', 500)
    cmds.setAttr(poly_plane[0] + '.scaleY', 500)
    cmds.setAttr(poly_plane[0] + '.scaleZ', 500)
    poly_plane_edges = list(range(0, 20, 2))
    for num in poly_plane_edges:
        cmds.polyExtrudeFacet( poly_plane[0] + '.e[' + str(num) + ']', ltz = 3000)
    

