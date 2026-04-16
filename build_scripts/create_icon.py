from PIL import Image, ImageDraw

def create_icons():
    # Deep Space Blue background
    img = Image.new('RGB', (256, 256), color=(15, 23, 42))
    d = ImageDraw.Draw(img)
    # Electric Cyan border
    d.rectangle([20, 20, 236, 236], outline=(0, 229, 255), width=8)
    # Steel Blue mountain/peak
    d.polygon([(128, 60), (200, 180), (56, 180)], fill=(56, 189, 248))
    
    img.save('build_scripts/icon.png')
    img.save('build_scripts/icon.ico')

if __name__ == '__main__':
    create_icons()
