
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Display.OCCViewer import rgb_color
#长方体
my_box = BRepPrimAPI_MakeBox (10,10,10).Shape()
if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(my_box,update=True,color=rgb_color(0,1,0))
    start_display()
