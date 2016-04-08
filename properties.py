import bpy

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       BoolVectorProperty,
                       PointerProperty,
                       CollectionProperty,
                       EnumProperty)
                       
from bpy.types import PropertyGroup  
                   
class CrmLead(bpy.types.PropertyGroup):
    id= bpy.props.StringProperty()
    name = bpy.props.StringProperty()
    create_date= bpy.props.StringProperty()
  
bpy.utils.register_class(CrmLead)
  
    
class ERP_PROPERTIES(PropertyGroup):
    crm_leads = CollectionProperty(name="crm_leads", type=CrmLead)
      
bpy.utils.register_class(ERP_PROPERTIES)


def register():
    bpy.types.Scene.erplib= PointerProperty(type = ERP_PROPERTIES)
    
if __name__ == "__main__":
    register()