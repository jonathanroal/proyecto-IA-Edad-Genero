from tkinter import *
from PIL import ImageTk, Image
from tensorflow import keras
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import random
global pop
def test_images(ind, images_f_2, Model,img_url):
    image_test = images_f_2[ind]
    pred_1 = Model.predict(np.array([image_test]))
    sex_f = ['Male', 'Female']
    age = int(np.round(pred_1[1][0]))
    sex = int(np.round(pred_1[0][0]))
    #print("Predicted Age: " + str(age))
    #print("Predicted Sex: " + sex_f[sex])
    #plt.imshow(image_test)
    #plt.show()
    return {"age":age,"sex":sex_f[sex],"img":img_url}


def predict(images, ind):
    Model = keras.models.load_model('Model2.h5')
    filesTest = os.listdir(images)
    images_original_size = []
    imagesTest_f = []
    img_url="testRandom/"+filesTest[ind]
    for photo in filesTest:
        img_dir = images + '/' + photo  # url de la imagen
        image = cv2.imread(img_dir)
        images_original_size.append(image)  # para ver el tamanno original
        # simplificamos los tonos de colos
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # estandarizamos el tamanno de la imagen
        image = cv2.resize(image, (48, 48))
        imagesTest_f.append(image)
    temp_images_test = np.array(imagesTest_f)
    imagesTest_f_2 = temp_images_test / 255
    return test_images(ind, imagesTest_f_2, Model,img_url)


window = Tk()

window.title("MAXI IA")

window.geometry('1200x900')
img_maxi = ImageTk.PhotoImage(Image.open("./maxi_pali.png"))
lblbanner=Label(window,image=img_maxi)
lblbanner.grid(column=2,row=0)

lbl = Label(window, text="Tu carrito:", width=55)
lbl.grid(column=0, row=1)

img_f = ImageTk.PhotoImage(Image.open("./frijoles_img.png").resize((140, 140)))
label_imgF = Label(image=img_f)
label_imgF.grid(column=2, row=2)
lblf = Label(window, text="Frijoles")
lblf.grid(column=1, row=2)


img_Arr = ImageTk.PhotoImage(Image.open("./Arroz.png").resize((140, 140)))
label_imgArr = Label(image=img_Arr)
label_imgArr.grid(column=2, row=3)
lblArr = Label(window, text="Arroz")
lblArr.grid(column=1, row=3)


img_Num = ImageTk.PhotoImage(Image.open("./numar.jpg").resize((140, 140)))
label_imgNUM = Label(image=img_Num)
label_imgNUM.grid(column=2, row=4)
lblNum = Label(window, text="Numar")
lblNum.grid(column=1, row=4)


img_at = ImageTk.PhotoImage(Image.open("./atun.jpg").resize((140, 140)))
label_imgAT = Label(image=img_at)
label_imgAT.grid(column=2, row=5)
lblf = Label(window, text="Atún")
lblf.grid(column=1, row=5)


def clicked():
    img_ind = random.randint(1,14)
    result = predict("testRandom",img_ind)
    pop = Toplevel(window)
    pop.title("Info")
    pop.geometry("600x350")
    labelage = Label(pop,text="Edad:",width=20)
    labelage.grid(column=1, row=1)
    labelageresult = Label(pop,text=result["age"])
    labelageresult.grid(column=2, row=1)
    labelsex = Label(pop,text="Genero:",width=20)
    labelsex.grid(column=3, row=1)
    labelsexresult = Label(pop,text= "Hombre" if result["sex"] =="Male" else "Mujer")
    labelsexresult.grid(column=4, row=1)
    imgres = ImageTk.PhotoImage(Image.open(result["img"]).resize((250, 250)))
    labelimg = Label(pop,image=imgres)
    labelimg.image = imgres
    labelimg.grid(column=3, row=2)
    btn = Button(pop, text="Salir", command=lambda: pop.destroy())
    btn.grid(column=8, row=3)


btn = Button(window, text="Pagar", command=clicked)

btn.grid(column=20, row=20)

window.mainloop()


