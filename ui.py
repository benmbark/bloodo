import bpy


class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "MBU DEMO"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        
        col = layout.box().column(align=True)
        scene = context.scene
        #layout.label(text="Big Button:")
        row = layout.row()
        row.scale_y = 3.0
        props= row.operator("mbu.import_from_server")
        
       
        row = layout.row()
        row.menu('CRM_LEADS_Menu',text='crm leads')
       
        row = layout.row()
        row.scale_y = 3.0
        props= row.operator("mbu.upload_items_to_server")
        
        

class CRM_LEADS_Menu(bpy.types.Menu):
    bl_label = "Libraries"


    def draw(self, context):
        layout = self.layout
        scene = context.scene
        crm_leads = scene.erplib.crm_leads
       
        for c_l in scene.erplib.crm_leads:
            print(c_l)
            text= c_l.id+' |  '+c_l.name+' |  '+c_l.create_date
            layout.operator('object.list_item',text=text,icon='BLENDER')
            
 

def register():
    bpy.utils.register_class(LayoutDemoPanel)
    bpy.utils.register_class(CRM_LEADS_Menu)


def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)
    bpy.utils.unregister_class(CRM_LEADS_Menu)


if __name__ == "__main__":
    register()
