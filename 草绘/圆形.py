#圆形

from OCC.Core.GC import GC_MakeCircle
from OCC.Core.gp import gp_Pnt
from OCC.Core.gp import gp_Ax2,gp_Dir
from OCC.Display.OCCViewer import rgb_color
#圆形
Circle=GC_MakeCircle(gp_Ax2 (gp_Pnt(0,0,5),gp_Dir (0,0,-1)),8).Value()

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(Circle,update=True,color=rgb_color(0,0,1))
    start_display()