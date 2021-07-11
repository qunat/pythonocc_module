#布尔剪（Boolean cut）
my_cylinder = BRepPrimAPI_MakeCylinder (gp_Ax2 (gp_Pnt(-3,5,2),gp_Dir (1,0,1)),1,20).Shape()
my_box = BRepPrimAPI_MakeBox(10, 10, 10).Shape()
new_thing1 = BRepAlgoAPI_Cut(my_box, my_cylinder).Shape()
1