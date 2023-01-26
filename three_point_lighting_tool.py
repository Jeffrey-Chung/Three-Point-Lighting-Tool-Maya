#Three Point Lighting Tool
#This tool creates a three point lighting system for a selected object and can adjust light settings

import maya.cmds as cmds
import mtoa.utils as mutils

#get selected object to apply lighting
def get_selected_object():
    for selected_object in cmds.ls(sl=True):
        if selected_object:
            return selected_object
            
#create a default 90 degree shaped plane in case if a plane isn't already created in the scene
def create_plane():
    poly_plane = cmds.polyPlane(w=10, h=10 )
    cmds.setAttr(poly_plane[0] + '.scaleX', 500)
    cmds.setAttr(poly_plane[0] + '.scaleY', 500)
    cmds.setAttr(poly_plane[0] + '.scaleZ', 500)
    cmds.polyExtrudeFacet( poly_plane[0] + '.e[0:18]', kft = True, ltz = 3000)
    
#create the key light based on the object's location
'''instructions: 1. select the object in the outliner, 2. use the function'''
def create_key_light(selected_object):
    key_light = mutils.createLocator('aiAreaLight', asLight=True)
    key_light_shape = key_light[0].split('|aiAreaLight1|')[1]
    light_x_location = cmds.getAttr(selected_object + '.translateX') - 100
    light_y_location = cmds.getAttr(selected_object + '.translateY') + 200
    light_z_location = cmds.getAttr(selected_object + '.translateZ') - 200
    cmds.setAttr(key_light[1] + '.translateX', light_x_location)
    cmds.setAttr(key_light[1] + '.translateY', light_y_location)
    cmds.setAttr(key_light[1] + '.translateZ', light_z_location)
    cmds.setAttr(key_light[1] + '.rotateX', -45)
    cmds.setAttr(key_light[1] + '.rotateY', -135)
    cmds.setAttr(key_light[1] + '.scaleX', 100)
    cmds.setAttr(key_light[1] + '.scaleY', 100)
    cmds.setAttr(key_light[1] + '.scaleZ', 100)
    cmds.setAttr(key_light_shape + '.intensity', 100000)
    



