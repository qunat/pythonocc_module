#椭圆

from OCC.Core.GeomAPI import GeomAPI_Interpolate
from OCC.Core.TColgp import TColgp_HArray1OfPnt
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir, gp_Circ, gp_Elips
from OCC.Core.GC import GC_MakeSegment, GC_MakeCircle, GC_MakeArcOfCircle, GC_MakeEllipse
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire
# 函数作用：通过半长轴和半短轴及原点绘制椭圆
# 输入：原点坐标，半长轴值，半短轴值
# 输出：暂定只输出椭圆
Location = gp_Pnt(0,0,0)
Axis = gp_Dir(0,0,1)
ElipsAxis= gp_Ax2(Location, Axis)
ElipsAxis0 = gp_Elips(ElipsAxis, 9, 3)
ElipsAxis1 = BRepBuilderAPI_MakeEdge(ElipsAxis0)
ElipsAxis = BRepBuilderAPI_MakeWire(ElipsAxis1.Edge())

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(ElipsAxis.Edge(),update=True)
    start_display()