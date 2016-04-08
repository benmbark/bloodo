bl_info = {
    "name": "Mbu urbanisme",
    "author": "Microvellum, Inc.",
    "version": (1, 0, 0),
    "blender": (2, 71, 0),
    "location": "View 3D>Tools Panel>Library",
    "warning": "",
    "description": "This is the base library that stores objects",
    "wiki_url": "http://www.microvellum.com",
    "category": "Library Add-on",
    "icon":"OBJECT_DATA",
}
import bpy


from . import operators
from . import properties
from . import ui

def register():

    properties.register()
    operators.register()
    ui.register()
    

def unregister():


    ui.unregister()
    operators.unregister()

if __name__ == "__main__":
    register()
