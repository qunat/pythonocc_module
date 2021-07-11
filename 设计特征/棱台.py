#棱台

my_wedge = BRepPrimAPI_MakeWedge(gp_Ax2 (gp_Pnt (-4,-8,-4),gp_Dir (0,0,1)),4,4,8,1,1,3,7).Shape()
