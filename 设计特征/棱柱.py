#棱柱

my_wedge1 = BRepPrimAPI_MakeWedge(gp_Ax2(gp_Pnt(2, -6, -4), gp_Dir(0, 0, 1)), 2, 3, 4, 1).Shape()