import bpy  
from collections import Counter
from mbutest.operators import MbuErp
  
class getListItem(bpy.types.Operator):  
    bl_idname = "mbu.upload_items_to_server"  
    bl_label = "Upload items to server"  
  
    id_crm=''
  
    def execute(self, context):
        # get the scene
        scene = bpy.context.scene
        items = []
        
        # look for the objects in the scene
        for object in scene.objects:
           
            if object.get('is_erp_product') and object['is_erp_product']:
                
                items.append(object['ref'])
           
		
		#count occurence of each item
        list = dict(Counter(items))
        
        
        models =MbuErp.get_xmlrpc_model()

        
        
        print(list)
        
        odoo_context={'blender_select':{'name':'blabla','blender_file':'test','products':list}}
        
        
        leads= models.execute_kw(
        MbuErp.db, MbuErp.uid, MbuErp.password, 'crm.lead.blender.model', 'save_last_blender_model',
        [2,odoo_context])
                                         
                                         
        return {'FINISHED'}
  
def register():  
    bpy.utils.register_class(getListItem)  
  
if __name__ == "__main__":  
    register()