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
    cmds.polyExtrudeFacet( poly_plane[0] + '.e[0:18]', kft = True, ltz = 3000) #extrude the edges at the end of the plane upwards for lighting
    
def create_three_point_lighting():
    selected_object = get_selected_object()
    key_light = create_key_light(selected_object)
    fill_light = create_fill_light(selected_object)
    back_light = create_back_light(selected_object)
    cmds.group(key_light, fill_light, back_light, n='three point lighting on ' + selected_object)

#create the key light based on the object's location
'''instructions: 1. select the object in the outliner, 2. use the function'''
def create_key_light(selected_object):
    key_light = mutils.createLocator('aiAreaLight', asLight=True)
    key_light_shape = key_light[0].split('|aiAreaLight' + key_light[0][12] + '|')[1] #get the key light shape 
    
    #denote the distance differences between object and the light position
    light_x_location = cmds.getAttr(selected_object + '.translateX') - cmds.getAttr(selected_object + '.scaleX') * 100
    light_y_location = cmds.getAttr(selected_object + '.translateY') + cmds.getAttr(selected_object + '.scaleY') * 200
    light_z_location = cmds.getAttr(selected_object + '.translateZ') - cmds.getAttr(selected_object + '.scaleZ') * 200
    cmds.setAttr(key_light[1] + '.translateX', light_x_location)
    cmds.setAttr(key_light[1] + '.translateY', light_y_location)
    cmds.setAttr(key_light[1] + '.translateZ', light_z_location)
    
    #adjust the angles of the light to be multiples of 45 degrees
    cmds.setAttr(key_light[1] + '.rotateX', -45) 
    cmds.setAttr(key_light[1] + '.rotateY', -135)
    
    #the scale and intensity might be able to be changed depending on UI, but these are the default settings
    cmds.setAttr(key_light[1] + '.scaleX', cmds.getAttr(selected_object + '.scaleX') * 100)
    cmds.setAttr(key_light[1] + '.scaleY', cmds.getAttr(selected_object + '.scaleY') * 100)
    cmds.setAttr(key_light[1] + '.scaleZ', cmds.getAttr(selected_object + '.scaleZ') * 100)
    cmds.setAttr(key_light_shape + '.intensity', 100000)
    
    #renaming the area light to key light for convenience
    key_light_rename = cmds.rename(key_light[1], 'keyLight') #output = keyLight as string
    return key_light_rename
    
    
    

#create the fill light based on the object's location
'''instructions: 1. select the object in the outliner, 2. use the function'''
def create_fill_light(selected_object):
    fill_light = mutils.createLocator('aiAreaLight', asLight=True)
    fill_light_shape = fill_light[0].split('|aiAreaLight' + fill_light[0][12] + '|')[1] #get the fill light shape 
    
    #denote the distance differences between object and the light position
    light_x_location = cmds.getAttr(selected_object + '.translateX') + cmds.getAttr(selected_object + '.scaleX') * 200
    light_y_location = cmds.getAttr(selected_object + '.translateY') + cmds.getAttr(selected_object + '.scaleY') * 200
    light_z_location = cmds.getAttr(selected_object + '.translateZ') - cmds.getAttr(selected_object + '.scaleZ') * 250
    cmds.setAttr(fill_light[1] + '.translateX', light_x_location)
    cmds.setAttr(fill_light[1] + '.translateY', light_y_location)
    cmds.setAttr(fill_light[1] + '.translateZ', light_z_location)
    
    #adjust the angles of the light to be multiples of 45 degrees
    cmds.setAttr(fill_light[1] + '.rotateX', -45) 
    cmds.setAttr(fill_light[1] + '.rotateY', -180)
    cmds.setAttr(fill_light[1] + '.rotateZ', -45) 
    
    #the scale and intensity might be able to be changed depending on UI, but these are the default settings
    cmds.setAttr(fill_light[1] + '.scaleX', cmds.getAttr(selected_object + '.scaleX') * 100)
    cmds.setAttr(fill_light[1] + '.scaleY', cmds.getAttr(selected_object + '.scaleY') * 100)
    cmds.setAttr(fill_light[1] + '.scaleZ', cmds.getAttr(selected_object + '.scaleZ') * 100)
    cmds.setAttr(fill_light_shape + '.intensity', 50000)
    
    #renaming the area light to fill light for convenience
    fill_light_rename = cmds.rename(fill_light[1], 'fillLight') #output = fillLight as string
    return fill_light_rename

#create the back light based on the object's location
'''instructions: 1. select the object in the outliner, 2. use the function'''
def create_back_light(selected_object):
    back_light = mutils.createLocator('aiAreaLight', asLight=True)
    back_light_shape = back_light[0].split('|aiAreaLight' + back_light[0][12] + '|')[1] #get the back light shape 
    
    #denote the distance differences between object and the light position
    light_x_location = cmds.getAttr(selected_object + '.translateX') + cmds.getAttr(selected_object + '.scaleX') * 250
    light_y_location = cmds.getAttr(selected_object + '.translateY') + cmds.getAttr(selected_object + '.scaleY') * 45
    light_z_location = cmds.getAttr(selected_object + '.translateZ') + cmds.getAttr(selected_object + '.scaleZ') * 400
    cmds.setAttr(back_light[1] + '.translateX', light_x_location)
    cmds.setAttr(back_light[1] + '.translateY', light_y_location)
    cmds.setAttr(back_light[1] + '.translateZ', light_z_location)
    
    #adjust the angles of the light to be multiples of 45 degrees
    cmds.setAttr(back_light[1] + '.rotateX', 225) 
    cmds.setAttr(back_light[1] + '.rotateY', -180)
    cmds.setAttr(back_light[1] + '.rotateZ', -100) 
    
    #the scale and intensity might be able to be changed depending on UI, but these are the default settings
    cmds.setAttr(back_light[1] + '.scaleX', cmds.getAttr(selected_object + '.scaleX') * 100)
    cmds.setAttr(back_light[1] + '.scaleY', cmds.getAttr(selected_object + '.scaleY') * 100)
    cmds.setAttr(back_light[1] + '.scaleZ', cmds.getAttr(selected_object + '.scaleZ') * 100)
    cmds.setAttr(back_light_shape + '.intensity', 25000)
    
    #renaming the area light to back light for convenience
    back_light_rename = cmds.rename(back_light[1], 'backLight') #output = backLight as string
    return back_light_rename

#class for three point lighting UI
class ThreePointLightingTool():
    #setup window and tabs for UI
    def __init__(self):
        self.win = cmds.window(title="Three Point Lighting Tool", menuBar=True, widthHeight=(100,100),resizeToFitChildren=True)
        self.tabs = cmds.tabLayout()
        self.draw_UI()

    #function to draw the UI itself
    def draw_UI(self):
        #first Tab: create three point lighting based on object
        first_tab = cmds.columnLayout(adjustableColumn = True)
        cmds.tabLayout(self.tabs, edit=True, tabLabel=[first_tab, 'Set Up Lighting'])
        cmds.separator(h=10)
        cmds.text('Set up Plane to add Lighting if Needed', fn='fixedWidthFont') #Description for the plane
        cmds.text('Note: it will spawn an L shaped plane')
        cmds.separator(h=20)
        cmds.button(label = 'Create Plane', command = 'create_plane()')
        cmds.separator(h=20)
        
        cmds.separator(h=20)
        cmds.text('Add Three Point Lighting Based on Selected Object', fn='fixedWidthFont') #Description for the Three Point Lighting
        cmds.text('1. Select the object to apply lighting on\n 2. Click on "Add Light" button to apply it on the object')
        cmds.separator(h=20)
        cmds.button(label = 'Add Light', command = 'create_three_point_lighting()')
        cmds.separator(h=20)
        cmds.setParent("..")

        cmds.showWindow(self.win)
        
def main():
    ThreePointLightingTool()

if __name__ == "__main__":
    main()