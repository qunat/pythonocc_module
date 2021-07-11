#圆柱

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder
#圆柱
my_cylinder=BRepPrimAPI_MakeCylinder(10,50).Shape()
if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(my_cylinder,update=True)
    start_display()