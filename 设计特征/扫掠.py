#管道（实体）

from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.BRepOffsetAPI import BRepOffsetAPI_MakePipe
from OCC.Core.gp import gp_Circ, gp_Ax2, gp_Pnt, gp_Dir


E21=BRepBuilderAPI_MakeEdge(gp_Pnt(40,0,10),gp_Pnt(82.5,25,10)).Edge()
E22=BRepBuilderAPI_MakeEdge(gp_Pnt(82.5,25,10),gp_Pnt(42.5,93,10)).Edge()

W2=BRepBuilderAPI_MakeWire(E21,E22)

c=gp_Circ(gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 1, 0)), 10)

Ec = BRepBuilderAPI_MakeEdge(c).Edge()
Wc = BRepBuilderAPI_MakeWire(Ec).Wire()
F = BRepBuilderAPI_MakeFace(Wc, True)
S = BRepOffsetAPI_MakePipe(W2.Wire(), F.Shape())# 第一个参数 轨迹线，第二个参数是轮廓线

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(S.Shape(), update=True)
    start_display()