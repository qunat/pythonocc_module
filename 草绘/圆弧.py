#圆弧

from OCC.Core.GeomAPI import GeomAPI_Interpolate
from OCC.Core.TColgp import TColgp_HArray1OfPnt
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir, gp_Circ, gp_Elips
from OCC.Core.GC import GC_MakeSegment, GC_MakeCircle, GC_MakeArcOfCircle, GC_MakeEllipse
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire
# 函数作用：通过圆心和半径和角度生成圆弧
# 输入：圆心坐标，半径值，角度值
# 输出：暂定只输出圆弧
Location = gp_Pnt(0,0,0)
Axis = gp_Dir (0,0,-1)
CircleAxis= gp_Ax2(Location, Axis)
Circle = gp_Circ(CircleAxis,5)
ArcofCircle0 = GC_MakeArcOfCircle(Circle, 0/180*3.14, 180/180*3.14, True)
ArcofCircle1 = BRepBuilderAPI_MakeEdge(ArcofCircle0.Value())
ArcofCircle = BRepBuilderAPI_MakeWire(ArcofCircle1.Edge())
if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(ArcofCircle.Edge(),update=True)
    start_display()