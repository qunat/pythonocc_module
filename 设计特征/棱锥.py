#棱锥

my_wedge = BRepPrimAPI_MakeWedge(gp_Ax2(gp_Pnt(4, 0,4), gp_Dir(1,1,0)),4,4,4,2,2,2,2).Shape()