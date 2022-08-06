from PIL import Image
import os
'''
目的:
改資料夾內jpg圖片的dpi,並另存新檔後加dpi規格說明

要設定參數說明:
dirName:照片存檔的資料夾路徑
newDip:要另存設定的的新dpi
'''

dirName = "C:\\Users\\runra\Desktop\\test\\"   #最後要加雙斜線,不然會報錯
li=os.listdir(dirName)
for ims in li:
    im = Image.open(dirName+ims)
    nx, ny = im.size
    f = im.format
    print("原始照片尺寸: ",nx,"x",ny,"圖片格式: ",f)
    fileName=ims.split(".")

    if im.info.get('dpi'):
        x_dpi, y_dpi = im.info['dpi']
        if x_dpi != y_dpi:
            print('Inconsistent DPI image data')
        print("原本x_dpi: " + str(x_dpi),"原本y_dpi: " + str(y_dpi))
    else:
        print('No DPI data. Invalid Image header')
        print(im.info)
    

    newDpi=300  #設定新的dpi
    newFileName=fileName[0]+"_"+str(newDpi)+"dpi"+".jpg"
    im.save(f"{dirName}/"+newFileName,dpi=(newDpi,newDpi),quality=100)


print("資料夾內檔案轉換完成")