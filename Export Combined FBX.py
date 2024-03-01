import bpy
import os

from bpy.types import Operator
from bpy.props import StringProperty

# Define the Export Operator
class ExportCombinedFBXOperator(Operator):
    bl_idname = "object.export_combined_fbx"
    bl_label = "Export Combined FBX"
    bl_description = "Export all scene models as a single combined FBX file"

    filepath: StringProperty(subtype='FILE_PATH')

    def execute(self, context):
        # Get the current scene
        scene = context.scene

        # Set the directory where the FBX file will be saved
        output_dir = os.path.dirname(self.filepath)

        # Get the scale of the scene
        scene_scale = scene.unit_settings.scale_length

        # Combine all objects into one mesh
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.join()

        # Apply the scene scale to the combined mesh
        bpy.context.object.scale = (scene_scale, scene_scale, scene_scale)

        # Export the combined mesh as FBX
        fbx_filepath = self.filepath
        bpy.ops.export_scene.fbx(filepath=fbx_filepath, check_existing=False, axis_forward='-Z', axis_up='Y', global_scale=1.0)

        print("FBX file exported:", fbx_filepath)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


# Define the UI Panel
class ExportCombinedFBXPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_export_combined_fbx_panel"
    bl_label = "Export Combined FBX"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.export_combined_fbx", text="Export Combined FBX")


# Register classes
def register():
    bpy.utils.register_class(ExportCombinedFBXOperator)
    bpy.utils.register_class(ExportCombinedFBXPanel)

def unregister():
    bpy.utils.unregister_class(ExportCombinedFBXOperator)
    bpy.utils.unregister_class(ExportCombinedFBXPanel)

if __name__ == "__main__":
    register()
