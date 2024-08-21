'''
This script is purely served as a code extract for the previous UI. 
It will not run on its own nor imported into three_point_lighting_tool.py
script. Therefore treat it as a pseudo code here. 
'''

#class for three point lighting UI
class ThreePointLightingTool():
    #setup window and tabs for UI
    def __init__(self):
        self.win = cmds.window(title="Three Point Lighting Tool", menuBar=True, widthHeight=(100,100),resizeToFitChildren=True)
        self.tabs = cmds.tabLayout()
        self.draw_UI()
    
    #Set the focal length of the camera via the confirm focal length button
    def set_colour(self, *args):
        menu_value = get_option_menu_value(self.change_colour_option_menu)
        selected_colour_index = light_colours.index(menu_value)
        if 'backLight' in get_obj() and get_obj() is not None:
            cmds.setAttr(get_obj() + '.color', rgb_values[selected_colour_index][0], rgb_values[selected_colour_index][1], rgb_values[selected_colour_index][2], type = 'double3')
            return
        raise Exception("You need to choose a back light to change its colour")

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

        #second Tab: Modify Three point light options
        second_tab = cmds.columnLayout(adjustableColumn = True)
        cmds.tabLayout(self.tabs, edit=True, tabLabel=[second_tab, 'Modify Lighting'])
        cmds.separator(h=10)
        cmds.text('Change Colour of Back Light', fn='fixedWidthFont') #Description to change colour of back light
        cmds.text('1. Select your back light in the outliner \n 2. Select your colour in the dropdown menu \n 3. Confirm your settings by clicking on the Confirm Colour Button\n')
        self.change_colour_option_menu = cmds.optionMenu(w = 250, label = "Change Colour")
        #add menu item for all values
        cmds.menuItem(label = "Red")
        cmds.menuItem(label = "Blue")
        cmds.menuItem(label = "Bright Red")
        cmds.menuItem(label = "Bright Green")
        cmds.menuItem(label = "Bright Blue")
        cmds.menuItem(label = "Orange")
        cmds.menuItem(label = "Pink")
        cmds.separator(h=20)
        cmds.button(label = "Confirm Colour" , command=self.set_colour)
        cmds.setParent("..")

        cmds.showWindow(self.win)
ThreePointLightingTool()