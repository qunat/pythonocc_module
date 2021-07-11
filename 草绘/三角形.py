#三角形

from OCC.Core.GeomAPI import GeomAPI_Interpolate
from OCC.Core.TColgp import TColgp_HArray1OfPnt
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_DX, gp_Circ, gp_Elips
from OCC.Core.GC import GC_MakeSegment, GC_MakeCircle, GC_MakeArcOfCircle, GC_MakeEllipse
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire

# 函数作用：通过三点生成任意三角形
# 输入：三点
# 输出：三角形
aSegment1 = GC_MakeSegment(gp_Pnt(1,1,1), gp_Pnt(2,1,5))
anEdge1 = BRepBuilderAPI_MakeEdge(aSegment1.Value())
aWire1 = BRepBuilderAPI_MakeWire(anEdge1.Edge())
aSegment2 = GC_MakeSegment(gp_Pnt(2,1,5), gp_Pnt(9,1,5))
anEdge2 = BRepBuilderAPI_MakeEdge(aSegment2.Value())
aWire2 = BRepBuilderAPI_MakeWire(anEdge2.Edge())
aSegment3 = GC_MakeSegment(gp_Pnt(9,1,5), gp_Pnt(1,1,1))
anEdge3 = BRepBuilderAPI_MakeEdge(aSegment3.Value())
aWire3 = BRepBuilderAPI_MakeWire(anEdge3.Edge())
aTriangle = BRepBuilderAPI_MakeWire(aWire1 .Edge(),aWire2 .Edge(),aWire3 .Edge())
if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(aTriangle.Shape(), update=True)
    start_display()