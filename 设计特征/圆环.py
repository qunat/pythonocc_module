#环形

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeTorus
from OCC.Core.gp import gp_Pnt
from OCC.Core.gp import gp_Ax2,gp_Dir
my_Torus = BRepPrimAPI_MakeTorus(gp_Ax2 (gp_Pnt (0,0,2),gp_Dir (0,0,1)),0.55,0.1).Shape()
if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(my_Torus, update=True)
    start_display()