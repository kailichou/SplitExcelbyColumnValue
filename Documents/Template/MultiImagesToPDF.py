from PIL import Image
import os
# import tkinter as tk

# HEIGHT = 300
# WIDTH = 500


# root = tk.Tk()

# canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
# canvas.pack()


# frame = tk.Frame(root, bg='#80c1ff')
# frame.place(relx=0.1, rely= 0.1, relwidth=0.8,relheight=0.8)

# label = tk.Label(canvas, text='Do you want to transfer multiple images into one PDF file?')
# label.pack()

# yesButton = tk.Button(root, text = "YES", bg='lightgray')
# yesButton.pack(side='center')

# exitButton = tk.Button(root, text = " No, Exit the Program")
# exitButton.pack(side='center')
# noButton = tk.Button(root, text ='NO',bg='lightgrey')




def getImage(filepath):

    images = []

    for f in filepath:
        x = Image.open(f)
        images.append(x)

    im1 = images.pop(0)
    imagelist = images
    if input(f"Would you like to save your file in {fileDirectory}? ====>").lower() == 'yes':
        savepath = fileDirectory
    else:
        print("Please specify the directory, you'd like to save your file\n")
        savepath = input("===>")
        


    im1.save(f'{savepath}/Combined.pdf',save_all=True, append_images=imagelist)
    print(f'Thank you for using this program. The file is saved at {savepath}')

            


fileDirectory = os.getcwd()

filepaths = input("Please add images that you want to convert into a PDF file and seperate them with a comma ','===> \n").split(',')
getImage(filepaths)


#root.mainloop()