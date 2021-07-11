#缩放
from OCC.Core.GeomAPI import GeomAPI_Interpolate
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCone
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Core.TColgp import TColgp_HArray1OfPnt
from OCC.Core.gp import gp_Pnt, gp_Ax1, gp_Dir, gp_Circ, gp_Elips,gp_Trsf,gp_Vec
from OCC.Core.TopLoc import TopLoc_Location
from OCC.Core.GC import GC_MakeSegment, GC_MakeCircle, GC_MakeArcOfCircle, GC_MakeEllipse,GC_MakeRotation
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire
from OCC.Display.OCCViewer import rgb_color
#缩放
my_cone = BRepPrimAPI_MakeCone(1,0,4).Shape()
cone=TopoDS_Shape(my_cone)
T1=gp_Trsf()
T=gp_Pnt(0, 20, 0)
T1.SetScale(T,5)
coneLoc=TopLoc_Location(T1)
my_cone.Move(coneLoc)

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(cone,update=True,color=rgb_color(0,0,0))
    display.DisplayShape(my_cone, update=True,color=rgb_color(1,0,0))
    start_display()