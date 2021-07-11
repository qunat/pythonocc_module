#导出 iges，step，stl格式文件
from OCC.Display.SimpleGui import init_display
from OCC.Extend.DataExchange import write_iges_file,write_step_file,write_stl_file
shapes=read_iges_file(fileName1)
#shapes=write_step_file(fileName1)
#shapes=write_stl_file(fileName1)
display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(shapes, update=True)