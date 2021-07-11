#矩形（任意多边形就是改变Pi数量顺次连接）

from OCC.Core.GeomAPI import GeomAPI_Interpolate
from OCC.Core.TColgp import TColgp_HArray1OfPnt
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_DX, gp_Circ, gp_Elips
from OCC.Core.GC import GC_MakeSegment, GC_MakeCircle, GC_MakeArcOfCircle, GC_MakeEllipse
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire
# 函数作用：在yz平面上通过一顶点及长宽绘制矩形
# 输入：一顶点坐标，长值，宽值
# 输出：暂定只输出矩形
coor0=[0,3,3]#矩阵某一行
Length=3
Width=1
yPlus = [0, Length, 0]
zPlus = [0, 0, Width]
coor1 = [coor0[i] + yPlus[i] for i in range(3)]
coor2 = [coor0[i] + zPlus[i]+ yPlus[i] for i in range(3)]
coor3 = [coor0[i] + zPlus[i] for i in range(3)]
P0 = gp_Pnt(coor0[0],coor0[1],coor0[2])
P1 = gp_Pnt(coor1[0],coor1[1],coor1[2])
P2 = gp_Pnt(coor2[0],coor2[1],coor2[2])
P3 = gp_Pnt(coor3[0],coor3[1],coor3[2])
aSegment1 = GC_MakeSegment(P0, P1)
anEdge1 = BRepBuilderAPI_MakeEdge(aSegment1.Value())
aWire1 = BRepBuilderAPI_MakeWire(anEdge1.Edge())
aSegment2 = GC_MakeSegment(P1, P2)
anEdge2 = BRepBuilderAPI_MakeEdge(aSegment2.Value())
aWire2 = BRepBuilderAPI_MakeWire(anEdge2.Edge())
aSegment3 = GC_MakeSegment(P2, P3)
anEdge3 = BRepBuilderAPI_MakeEdge(aSegment3.Value())
aWire3 = BRepBuilderAPI_MakeWire(anEdge3.Edge())
aSegment4 = GC_MakeSegment(P3, P0)
anEdge4 = BRepBuilderAPI_MakeEdge(aSegment4.Value())
aWire4 = BRepBuilderAPI_MakeWire(anEdge4.Edge())
aRectangle = BRepBuilderAPI_MakeWire(aWire1 .Edge(),aWire2 .Edge(),aWire3 .Edge(),aWire4 .Edge())
if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(aRectangle.Shape(), update=True)
    start_display()