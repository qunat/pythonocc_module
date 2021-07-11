#抛物线 parabola
from OCC.Core.GCE2d import GCE2d_MakeParabola
from OCC.Core.gp import gp_Pnt, gp_Ax2d, gp_Pnt2d, gp_Dir2d
from OCC.Display.SimpleGui import init_display


focal=5
parabola=GCE2d_MakeParabola(gp_Ax2d(gp_Pnt2d(0 , 0),gp_Dir2d(0,1)),focal,False)


display, start_display, add_menu, add_function_to_menu = init_display()

display.DisplayShape(parabola.Value(),update=True)


start_display()