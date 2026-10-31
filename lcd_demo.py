from xytft import Display
from PIL import Image, ImageDraw

with Display() as lcd:
    lcd.clear("black")

    clock_area = Image.new("RGB", (120, 40), "black")
    draw = ImageDraw.Draw(clock_area)
    draw.text((5, 5), "10:30:00", fill="yellow")

    lcd.show_region(10, 10, clock_area)
