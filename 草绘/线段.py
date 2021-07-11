#线段

from OCC.Core.gp import gp_Pnt
from OCC.Core.GC import GC_MakeSegment
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire
from OCC.Display.OCCViewer import rgb_color
# 函数作用：通过两点生成线段
# 输入：两点
# 输出：线段
aSegment = GC_MakeSegment(gp_Pnt(1,1,1), gp_Pnt(1,10,1))
anEdge = BRepBuilderAPI_MakeEdge(aSegment.Value())
aWire = BRepBuilderAPI_MakeWire(anEdge.Edge())
if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(aWire.Shape(), update=True,color=rgb_color(1,0,0))
    start_display()