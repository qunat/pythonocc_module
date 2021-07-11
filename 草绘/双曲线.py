#绘制双曲线hyperbola


from OCC.Core.GCE2d import GCE2d_MakeHyperbola
from OCC.Core.gp import gp_Pnt, gp_Ax2d, gp_Pnt2d, gp_Dir2d
from OCC.Display.SimpleGui import init_display


MajorRadius=5
MinorRadius=1
hyperbola=GCE2d_MakeHyperbola(gp_Ax2d(gp_Pnt2d(0 , 0.2),gp_Dir2d(0,1)),MajorRadius,MinorRadius,False)


display, start_display, add_menu, add_function_to_menu = init_display()

display.DisplayShape(hyperbola.Value(),update=True)


start_display()