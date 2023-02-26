#Three Point Lighting Tool
#This tool creates a three point lighting system for a selected object and can adjust light settings
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from shiboken2 import wrapInstance
from maya import OpenMayaUI as omui
import maya.cmds as cmds
import mtoa.utils as mutils

#Colours to choose to change back light
light_colours = [
    'Red',
    'Green',
    'Blue',
    'Bright Red',
    'Bright Green',
    'Bright Blue',
    'Orange',
    'Pink']

#RGB values of said colours
rgb_values = [
    [1, 0, 0], #Red
    [0, 1, 0], #Green
    [0, 0, 1], #Blue
    [1, 0.1, 0.1], #Bright Red
    [0.5, 1, 0.1], #Bright Green
    [0.7, 1, 1], #Bright Blue
    [1, 0.5, 0], #Orange
    [1, 0, 1] #Pink
]
#get selected object to apply lighting
def get_selected_object():
    for selected_object in cmds.ls(sl=True):
        if selected_object:
            return selected_object

#get the value from each option menu to coduct event
def get_option_menu_value(option_menu):
    menu_value = cmds.optionMenu(option_menu, q=True, value=True)
    return menu_value 
            

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

def get_maya_window():
    maya_main_window_ptr = omui.MQtUtil.mainWindow()
    maya_main_window = wrapInstance(int(maya_main_window_ptr), QWidget)
    return maya_main_window

#Common method to raise exception error if no object is selected
def raise_none_object_error():
    if get_selected_object() is None:
        raise Exception("Make sure you select an object before you apply lighting")
        return


#class for three point lighting UI
class ThreePointLightingTool(QMainWindow):
    def __init__(self, parent = None):
        super(ThreePointLightingTool, self).__init__(parent)
        #set name of the UI
        self.setWindowTitle("Three Point Lighting Tool")
        #Initiate tabs for UI
        tab = QTabWidget()

        #first Tab: create three point lighting based on object
        first_tab = QWidget()
        first_tab_layout = QVBoxLayout()
        first_tab.setLayout(first_tab_layout)
        
        #create plane section
        create_plane_text = QLabel("Set up Plane to add Lighting if Needed")
        header_font=QFont('Arial', 15)
        header_font.setBold(True)
        create_plane_text.setFont(header_font)
        first_tab_layout.addWidget(create_plane_text)

        create_plane_note = QLabel("Note: it will spawn an L shaped plane")
        note_font = QFont()
        note_font.setItalic(True)
        create_plane_note.setFont(note_font)
        first_tab_layout.addWidget(create_plane_note)

        create_plane_button = QPushButton("Create Plane")
        create_plane_button.clicked.connect(self.create_plane)
        first_tab_layout.addWidget(create_plane_button)
        
        #add light section
        add_light_text = QLabel("Add Three Point Lighting Based on Selected Object")
        add_light_text.setFont(header_font)
        first_tab_layout.addWidget(add_light_text)

        add_light_instructions = QLabel(' 1. Select the object to apply lighting on\n 2. Click on "Add Light" button to apply it on the object')
        first_tab_layout.addWidget(add_light_instructions)
        add_light_button = QPushButton("Add Light")
        add_light_button.clicked.connect(self.create_three_point_lighting)
        first_tab_layout.addWidget(add_light_button)
        
        #second Tab: Modify Three point light options
        second_tab = QWidget()
        second_tab_layout = QVBoxLayout()
        second_tab.setLayout(second_tab_layout)
        
        #Change Colour of Back Light
        change_colour_text = QLabel("Change Colour of Back Light")
        second_tab_header_font=QFont('Arial', 20)
        second_tab_header_font.setBold(True)
        change_colour_text.setFont(second_tab_header_font)
        second_tab_layout.addWidget(change_colour_text)

        change_colour_instructions = QLabel(' 1. Select your back light from a three point lighting group in the outliner \n 2. Select your colour in the dropdown menu \n')
        change_colour_instructions.setFont(QFont('Arial', 15))
        second_tab_layout.addWidget(change_colour_instructions)

        self.colour_dropbox = QComboBox()
        self.colour_dropbox.addItems(light_colours)
        self.colour_dropbox.activated.connect(self.set_colour)
        second_tab_layout.addWidget(self.colour_dropbox)
        
        #Add all the tabs and name them respectively
        tab.addTab(first_tab, "Set Up Lighting")
        tab.addTab(second_tab, "Modify Lighting")

        self.setCentralWidget(tab)
        self.show()
    
    #create a default 90 degree shaped plane in case if a plane isn't already created in the scene
    def create_plane(self):
        poly_plane = cmds.polyPlane(w=10, h=10 )
        cmds.setAttr(poly_plane[0] + '.scaleX', 500)
        cmds.setAttr(poly_plane[0] + '.scaleY', 500)
        cmds.setAttr(poly_plane[0] + '.scaleZ', 500)
        cmds.polyExtrudeFacet( poly_plane[0] + '.e[0:18]', kft = True, ltz = 3000) #extrude the edges at the end of the plane upwards for lighting
    
    #creates a three point lighting system based on the selected object
    def create_three_point_lighting(self):
        selected_object = get_selected_object()
        raise_none_object_error()
        key_light = create_key_light(selected_object)
        fill_light = create_fill_light(selected_object)
        back_light = create_back_light(selected_object)
        cmds.group(key_light, fill_light, back_light, n='three point lighting on ' + selected_object)
    
    #Set the focal length of the camera via the confirm focal length button
    def set_colour(self, index):
        selected_colour_index = self.colour_dropbox.currentIndex()
        if 'backLight' in get_selected_object() and get_selected_object() is not None:
            cmds.setAttr(get_selected_object() + '.color', rgb_values[selected_colour_index][0], rgb_values[selected_colour_index][1], rgb_values[selected_colour_index][2], type = 'double3')
            return
        raise Exception("You need to choose a back light to change its colour")
        
if __name__ == "__main__":
    tab_window = ThreePointLightingTool(parent=get_maya_window())