#圆台

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere, BRepPrimAPI_MakeCone
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Display.OCCViewer import rgb_color
#圆台
my_cone = BRepPrimAPI_MakeCone(1,0,4).Shape()
my_cone=BRepPrimAPI_MakeCone(gp_Ax2 (gp_Pnt(0,0,0),gp_Dir (0,0,-1)),1,2,4).Shape( )
if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(my_cone, update=True)
    # display.DisplayShape(my_cone, update=True, color=rgb_color(0, 1, 1 ))
    start_display()