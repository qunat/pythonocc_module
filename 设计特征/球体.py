from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere
from OCC.Core.gp import gp_Pnt
from OCC.Display.OCCViewer import rgb_color
#qiu
center=gp_Pnt(5,5,10)
radius=19
my_sphere =BRepPrimAPI_MakeSphere(center ,radius).Shape()
if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(my_sphere, update=True)
    display.DisplayShape(my_sphere, update=True, color=rgb_color(0, 1,0 ))
    start_display()