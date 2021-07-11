#放样

from OCC.Core.AIS import AIS_Shape
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire
from OCC.Core.BRepOffsetAPI import BRepOffsetAPI_ThruSections
from OCC.Core.gp import gp_Pnt
from OCC.Display.SimpleGui import init_display

# 做第一条封闭曲线（四边形）
E11=BRepBuilderAPI_MakeEdge(gp_Pnt(40,0,0),gp_Pnt(82.5,25,0)).Edge()
E12=BRepBuilderAPI_MakeEdge(gp_Pnt(82.5,25,0),gp_Pnt(42.5,93,0)).Edge()
E13=BRepBuilderAPI_MakeEdge(gp_Pnt(42.5,93,0),gp_Pnt(0,68,0)).Edge()
E14=BRepBuilderAPI_MakeEdge(gp_Pnt(0,68,0),gp_Pnt(40,0,0)).Edge()

W1=BRepBuilderAPI_MakeWire(E11,E12,E13,E14)

# 做第2条封闭曲线（三角形）
E21=BRepBuilderAPI_MakeEdge(gp_Pnt(40,0,10),gp_Pnt(82.5,25,10)).Edge()
E22=BRepBuilderAPI_MakeEdge(gp_Pnt(82.5,25,10),gp_Pnt(42.5,93,10)).Edge()
E23=BRepBuilderAPI_MakeEdge(gp_Pnt(42.5,93,10),gp_Pnt(40,0,10)).Edge()

W2=BRepBuilderAPI_MakeWire(E21,E22,E23)

generator=BRepOffsetAPI_ThruSections(True)

generator.AddWire(W1.Wire())
generator.AddWire(W2.Wire())

ais=AIS_Shape(generator.Shape())

generator.Build()



display, start_display, add_menu, add_function_to_menu = init_display()

display.DisplayShape(W1.Shape(),update=True)
display.DisplayShape(W2.Shape(),update=True)
# display.DisplayShape(generator.Shape(),update=True)
display.DisplayShape(ais.Shape(),update=True)
start_display()

39