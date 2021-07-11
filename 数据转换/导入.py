2.读取/写入 iges，step，stl格式文件
from OCC.Display.SimpleGui import init_display
from OCC.Extend.DataExchange import read_iges_file,read_step_file,read_stl_file
shapes=read_iges_file(fileName1)
#shapes=read_step_file(fileName1)
#shapes=read_stl_file(fileName1)
display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(shapes, update=True)