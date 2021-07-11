TopoDS_Compound aCompound;
BRepBuilder aBuilder;
aBuilder.MakeCompound(aCompound);

// then add all your shape
aBuilder.Add(aCompound,shape1);
aBuilder.Add(aCompound,shape2);
aBuilder.Add(aCompound,shape3);
aBuilder.Add(aCompound,shape4);

self.shape.Free(True)#先释放shape
new_build=TopoDS_Builder()#建立一个TopoDS_Builder()
aCompound=TopoDS_Compound()#定义一个复合体
new_build.MakeCompound(aCompound)#生成一个符合体DopoDS_shape
new_build.Add(aCompound,shape123)#将shaoe添加入复合体
new_build.Add(aCompound, self.shape)