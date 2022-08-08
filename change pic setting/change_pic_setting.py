from PIL import Image
import tempfile
import os
import pandas as pd
import shutil


def listPicFileInfo(dirName):
    '''
    目的: 得到指定資料夾圖片檔的明細

    設定參數:
    dirName:照片存檔的資料夾路徑
    
    '''
    #dirName = "C:\\Users\\runra\Desktop\\test\\"   #最後要加雙斜線,不然會報錯
    li=os.listdir(dirName)

    for ims in li:
        im = Image.open(dirName+ims)
        size = os.path.getsize(dirName+ims)
        nx, ny = im.size
        f = im.format
        
        if im.info.get('dpi'):
            x_dpi, y_dpi = im.info['dpi']
            print("檔名: {:<15s}  像素: {}*{}  格式: {}  圖片尺寸: {:.1f} KB  DPI(x_dpi*y_dpi): {}*{}  ".format(
                                                    ims,nx,ny,f,size/1024,str(x_dpi),str(y_dpi)))
        else:
            print("檔名: {:<15s}  像素: {}*{}  格式: {}  圖片尺寸: {:.1f} KB  DPI(x_dpi*y_dpi): {}  ".format(
                                                    ims,nx,ny,f,size/1024,"No DPI data. Invalid Image header"))
        im.close()

def changeDpi(dirName,newDpi):
    '''
    目的: 改資料夾內jpg圖片的dpi,並另存新檔後加dpi規格說明

    設定參數:
    dirName:照片存檔的資料夾路徑
    newDip:要另存設定的的新dpi
    '''
    #dirName = "C:\\Users\\runra\Desktop\\test\\"   #最後要加雙斜線,不然會報錯
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
            #print(im.info)
        
    #newDpi=300  #設定新的dpi
    newFileName=fileName[0]+"_"+str(newDpi)+"dpi"+".jpg"        #另存新檔
    #newFileName=fileName[0]+".jpg"                             #直接覆蓋
    im.save(f"{dirName}/"+newFileName,dpi=(newDpi,newDpi),quality=100)
    im.close()
    print("資料夾內檔案轉換結束!")


def changePicSize(dirName,max_width):
    '''
    目的: 等比例放大/縮小圖片

    設定參數:
    dirName:照片存檔的資料夾路徑
    max :輸入指定寬度
    '''
    #dirName = "C:\\Users\\runra\Desktop\\test\\"   #最後要加雙斜線,不然會報錯
    li=os.listdir(dirName)
    for ims in li:
        im = Image.open(dirName+ims)
        width,height = im.size
        #max = 200                     # 指定寬最大的數值
        scale = height/width           # 設定 scale 為 height/width
        w = max_width                  # 設定調整後的寬度為最大的數值
        h = int(max_width*scale)       # 設定調整後的高度為 max 乘以 scale ( 使用 int 去除小數點 )
        im2 = im.resize((w, h))        # 調整尺寸
        
        fileName=ims.split(".")
        newFileName=fileName[0]+"_"+"width"+str(max_width)+".jpg"   #另存新檔
        #newFileName=fileName[0]+".jpg"                             #直接覆蓋
        im2.save(f"{dirName}/"+newFileName,quality=100) 
        im.close()
        print(ims,"圖片放大/縮小結束!")



def changeFileName(filepath,dirName):
    '''
    目的: 更改檔名

    設定參數:
    filepath:放old,new檔名xls檔的位置,不要跟圖片檔同一個資料夾
    dirName:照片存檔的資料夾路徑
    filename.xls :新增一個xls檔案,內放二欄'old','new'檔名資料
    '''
    #filepath="C:\\Users\\runra\Desktop\\test\\"        #放old,new檔名xls檔的位置
    #dirName = "C:\\Users\\runra\Desktop\\test\pic\\"   #最後要加雙斜線,不然會報錯

    file=pd.read_excel(filepath+"filename.xls")
    #print(file.head())
    old=set(file['old'].tolist())
    file.set_index("old" , inplace=True)

    li=os.listdir(dirName)
    for ims in li:
        if ims in old:
            fileName=ims.split(".") 
            new=file.loc[ims].new
            os.rename(f"{dirName}/"+ims,f"{dirName}/"+new)   
        else:
            print(ims,"未改名!")
        
    print("圖片更名結束!")

def changePNG_to_JPG(dirName):
    '''
    目的: PNG另存jpg

    設定參數:
    dirName:照片存檔的資料夾路徑
    
    '''
    #dirName = "C:\\Users\\runra\Desktop\\test\pic\\"   #最後要加雙斜線,不然會報錯

    li=os.listdir(dirName)
    for ims in li:
        fileName=ims.split(".")
        im = Image.open(dirName+ims)
        newFileName=fileName[0]+".jpg"   #另存新檔
        im.save(f"{dirName}/"+newFileName,quality=100) 
        im.close()
    print("PNG圖片另存jpg結束!")

def picFileCopy():
    '''
    目的: 找到包含指定關鍵字的檔案,並另複制到其他資料夾

    設定參數:
    filename.xls :新增一個xls檔案,只要old那欄要抓取檔案的名稱。(要含.jpg)
    dirName:照片存檔的資料夾路徑
    finalLoc:目的資料夾
    '''

    
    src_dir_path = 'C:/Users/runra/Desktop/test2/'        # 源文件夹
    
    to_dir_path = 'C:/Users/runra/Desktop/test3/'         # 存放复制文件的文件夹
    
    key = 'a1'                 # 源文件夹中的文件包含字符key则复制到to_dir_path文件夹中
    
    if not os.path.exists(to_dir_path):
        print("to_dir_path not exist,so create the dir")
        os.mkdir(to_dir_path, 1)
    if os.path.exists(src_dir_path):
        print("src_dir_path exist")
        for file in os.listdir(src_dir_path):
            # is file
            if os.path.isfile(src_dir_path+'/'+file):
                if key in file:
                    print('找到包含"'+key+'"字符的文件,绝对路径为----->'+src_dir_path+'/'+file)
                    print('复制到----->'+to_dir_path+file)
                    shutil.copy(src_dir_path+'/'+file, to_dir_path+'/'+file)# 移动用move函数



#主功能區---------------------------------------------------------------
'''備註
    在檔案夾內開新文字檔，將以下文字貼入，存成.bat，即可列出資料夾內所有檔名
    @echo off
    dir /b /on >list.txt
'''


filepath="C:\\Users\\runra\Desktop\\test3\\"        #放old,new檔名xls檔的位置
#dirName = "C:\\Users\\runra\Desktop\\test\pic\\"  #最後要加雙斜線,不然會報錯
dirName = "C:\\Users\\runra\Desktop\\test2\\"      #最後要加雙斜線,不然會報錯
finalLoc= "C:\\Users\\runra\Desktop\\test3\\"      #另存新檔的位置

#listPicFileInfo(dirName)            #得到指定資料夾圖片檔的明細
#changeDpi(dirName,300)              #改變指定資料夾圖片dpi
#changePicSize(dirName,450)          #變更指定資料夾內,指定圖片寬度，等比例放大/縮小
#changeFileName(filepath,dirName)    #大量更改檔名
#changePNG_to_JPG(dirName)           #png 另存jpg
picFileCopy()

