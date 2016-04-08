import bpy
import xmlrpc.client
from mbutest import properties

class MbuErp(bpy.types.Operator):
    bl_idname = "mbu.import_from_server"
    bl_label = "import  leads from servers"
    leads=  [("0","nothing imported","0")] 
    
     
     
    url = 'http://192.168.50.45:8069'
    db = 'mbu'
    username = 'admin'
    password = 'admin'
    uid= 0
    
   
    
    
    @staticmethod
    def get_xmlrpc_model() :
        
        
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(MbuErp.url))
        MbuErp.uid = common.authenticate(MbuErp.db, MbuErp.username, MbuErp.password, {})
    
    
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(MbuErp.url))
        return models
        
        
    def get_projects(self,context):
        imported= False
        
        scene = context.scene

        #leads=  [("1","stuff 1","0"),("2","stuff 2","0"),("3","stuff 3","0")]
        
        
       
        models =MbuErp.get_xmlrpc_model()

        leads= models.execute_kw(
        MbuErp.db, MbuErp.uid, MbuErp.password, 'crm.lead', 'search_read',
        [[['is_blender_lead','=',True]]], {'fields': ['name','create_date']})
        
        
        
       
        print(leads)
        scene.erplib.crm_leads.clear()
            
        
        for lead in leads:
            
            cl= scene.erplib.crm_leads.add()
            cl.id=str(lead['id'])
            cl.name=lead['name']
            cl.create_date=lead['create_date']
         
        
        
        return leads
      
         
        
    def execute(self, context):
        print(self.get_projects(context))
        
        return {'FINISHED'}

   

def register(): 
    bpy.utils.register_class(MbuErp)


def unregister():
    bpy.utils.unregister_class(MbuErp)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()