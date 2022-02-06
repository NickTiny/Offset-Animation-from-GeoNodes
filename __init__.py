# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the         GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Offset from Geo Nodes",
    "author" : "Nick Alberelli",
    "description" : "",
    "blender" : (3, 0, 0),
    "version" : (0, 0, 1),
    "location" : "View 3D > Sidebar > Edit Tab > GN Offset",
    "warning" : "This addon is still under development",
    "category" : "Animation"
}

import bpy
import random


classes = [] 

class offset_animation_operator(bpy.types.Operator):  #This operator takes a list of vectors and duplicates a target object to those vectors with offset NLA tracks.
    """Duplicate source object hierarchy onto each vertex of the target object and offset animations.""" #Tooltip label.
    bl_idname = "view3d.offset_anim_geonodes_op" #This name blender uses to call this operator from another operator
    bl_label = "Offset from GeoNodes" #User facing name for operator.

    def execute(self, context):
        #Definitions for objects.
        source_obj = bpy.context.scene.target_obj.propertyDisplayTarget #Calling the source object defined by the user.
        target_obj = bpy.context.scene.source_obj.propertyDisplayTarget #Calling the target object defined by the user.
        obj = source_obj.evaluated_get(bpy.context.evaluated_depsgraph_get()).data #Get vector list from source object
        vectors_list = [pos.vector for pos in obj.attributes[0].data]
        
        
        

        for index,vectors, in enumerate(vectors_list): #For each set of x,y,z vectors duplicate and move source object.
            VectorList = [] #List of x,y,z values.
            for index,vector in enumerate(vectors):
                if index == 0:
                    VectorList.append(vector)
                if index == 1:
                    VectorList.append(vector)
                if index == 2:
                    VectorList.append(vector)
            #Define the x,y,z values.
            x = VectorList[0]
            y = VectorList[1]
            z = VectorList[2]
            #Defintions for math. 
            v = bpy.context.scene.random_scale.propertyDisplayTarget #User input of random scale.
            a = 1
            b = 25
            r = random.randint(a,b)
            #Copy adn move objects 
            bpy.ops.object.select_all(action='DESELECT') #Deslect all
            target_obj.select_set(True) #Select object to copy.
            bpy.context.view_layer.objects.active = target_obj #Select object to copy.
            bpy.ops.object.select_hierarchy(direction='CHILD', extend=True) #Select object's children.
            bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, #Duplicate linked selected.
            "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0)}) #Bpy.ops is slow should be replaced with data block method.
            bpy.ops.transform.translate(value=(x, y, z)) #Translate new objects to vectors from loop.
            bpy.ops.object.select_hierarchy(direction='PARENT', extend=False) #Select parent object only.
            #Definitions for NLA Actions
            active_obj = bpy.context.object 
            action = active_obj.animation_data.action #Use of bpy.ops is needed to edit NLA Tracks.
            track = active_obj.animation_data.nla_tracks.new()
            #NLA Actions
            track.strips.new(action.name, action.frame_range[0], action) #Pushdown animation to NLA tracks.
            active_obj.animation_data.action = None
            active_obj.animation_data.nla_tracks['NlaTrack'].strips['Action'].scale = (1 if v==0 else ((.1*r)*v))  #Math needs improvement.
            active_obj.animation_data.nla_tracks['NlaTrack'].strips['Action'].frame_start += x+y #Offset NLA track start.
            active_obj.animation_data.nla_tracks['NlaTrack'].strips['Action'].frame_end += x+y #Offset NLA track end.
            bpy.context.view_layer.objects.active = source_obj #Reselect target object.
        
        return {"FINISHED"}
classes.append(offset_animation_operator)

class OffsetGeoNodesPanel(bpy.types.Panel):  #This contains all UI elements.
    """Distribute Armatures and Objects based on a Geometry Nodes Object"""
    bl_idname = "VIEW3D_PT_OGN_PNL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "GN Offset"
    bl_label = "Geo Nodes Offset Animation"
    bl_context = "objectmode"


    def draw(self, context):
        scene = bpy.context.scene
        self.layout.prop(scene.random_scale, "propertyDisplayTarget") #User input random scale. 
        self.layout.prop(scene.target_obj, "propertyDisplayTarget") #User input Target Object.
        self.layout.prop(scene.source_obj, "propertyDisplayTarget") #User input Source Object.
        self.layout.operator("view3d.offset_anim_geonodes_op") #Run Script           
classes.append(OffsetGeoNodesPanel)

class random_scale(bpy.types.PropertyGroup): #Define random scale value.
    propertyDisplayTarget : bpy.props.FloatProperty(
        name = "Random Scale",
        description="Amount of randomization of animation scale. 0 disables randomization.",
        default = 0,
        min = 0,
        max=2,
        subtype='UNSIGNED'
        )
classes.append(random_scale)

class target_obj(bpy.types.PropertyGroup): #Define and store target object.
    propertyDisplayTarget: bpy.props.PointerProperty(name = "Target", type = bpy.types.Object)
    propertyDisplayUseActiveObject: bpy.props.BoolProperty(name = "Use Active")
classes.append(target_obj)

class source_obj(bpy.types.PropertyGroup): #Define and store source object.
    propertyDisplayTarget: bpy.props.PointerProperty(name = "Source", type = bpy.types.Object)
    propertyDisplayUseActiveObject: bpy.props.BoolProperty(name = "Use Active2")
classes.append(source_obj)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.target_obj = bpy.props.PointerProperty(type=target_obj)
    bpy.types.Scene.source_obj = bpy.props.PointerProperty(type=source_obj)
    bpy.types.Scene.random_scale = bpy.props.PointerProperty(type=random_scale)

def unregister():
   for cls in reversed(classes):...
   del bpy.types.Scene.target_obj
   del bpy.types.Scene.source_obj 
   del bpy.types.Scene.random_scale

if __name__ == "__main__":
    register()
        
