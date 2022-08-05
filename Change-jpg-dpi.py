from PIL import Image
import os

#改資料夾內jpg圖片的dpi
#要換路徑的話,改dirName
dirName = "C:\\Users\\runra\Desktop\\test\\"   #最後要加雙斜線,不然會報錯
li=os.listdir(dirName)
for ims in li:
    im = Image.open(dirName+ims)
    nx, ny = im.size
    f = im.format
    print("原始x_dpi: ",nx,"原本x_dpi: ",ny,"圖片格式: ",f)

    if im.info.get('dpi'):
        x_dpi, y_dpi = im.info['dpi']
        if x_dpi != y_dpi:
            print('Inconsistent DPI image data')
        print("x_dpi: " + str(x_dpi),"y_dpi: " + str(y_dpi))
    else:
        print('No DPI data. Invalid Image header')
        print(im.info)
    #im2 = im.resize((int(nx*2.5), int(ny*2.5)), Image.BICUBIC)
    #print(filename)
    im.save(f"{dirName}/"+ims,dpi=(300,300),quality=100)


print("轉換完成")