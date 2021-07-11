#平移
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCone
from OCC.Core.TopLoc import TopLoc_Location
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Core.gp import gp_Pnt, gp_Trsf, gp_Vec, gp_Ax1, gp_Dir
from OCC.Display.OCCViewer import rgb_color

my_cone = BRepPrimAPI_MakeCone(1,0,4).Shape()
cone=TopoDS_Shape(my_cone)
T=gp_Trsf()
T.SetTranslation(gp_Vec(0,5,0))
loc=TopLoc_Location(T)
cone.Location(loc)

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(my_cone, update=True,color=rgb_color(1,0,0))
    display.DisplayShape(cone, update=True,color=rgb_color(0,0,1))
    start_display()