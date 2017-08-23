from numpy import *
from pyhdf.SD import SD, SDC
import sys, traceback
import glob
import os
import re
import subprocess
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import gdal
import  tkinter as tk
import stat


#****************variables globales*************



#************************************************










def val_empty(rota):
    os.system('clear')
    ruta = rota
    hdf = {}
    completo = {}
    cont1 = 0
    cont = 0
    try:
        # fazer função deste
        arq = os.listdir(ruta)

        if not arq:
            x=messagebox.showinfo("Say Hello", "no exixten archivos .hdf")
            if x=="ok":
                exit()


            #print(u"Não existem arquivos HDF impossível iniciar o processo...")

        else:
            for i in arq:
                cont = cont + 1
                if i.endswith(".hdf"):
                    hdf[cont] = i
                    # até aqui a função
            for i, values in hdf.items():
                global  ver
                ver = ruta + values
                b = str(values)
                var = b[0:3]
                data = SD(ver, SDC.READ)
                if (data.attributes != None) and (data.datasets != None):
                    if var == "MOD":
                        cont1 = cont1 + 1
                        #print("arquivo MODIS:.. ", ver, "...OK")
                        completo[cont1] = ver
                        list.insert(END,ver)

                        # função CrearPRM
                else:
                    messagebox.showinfo("Say Hello", "Hello World")

                    print ("arquivo:.. ", ver, "Não contem informação válida, desea eliminarlo...")

    except OSError:
        tb = sys.exc_info()[-1]
        stk = traceback.extract_tb(tb, 1)
        fname = stk[0][2]
        messagebox.showinfo("error", "ruta invalida")
        #print(u'Rota de arquivos não existe....falho em função', fname)



    #print("estructura ",prm)
    criar_PRM (completo, prm, ruta)






def criar_PRM(hdfs, prm, ruta):

    entradas = {}  # diccionario com os nomes dos arquivos HDF
    entradas = hdfs  # diccionario com os nomes dos arquivos HDF
    template = prm  # rota onde se encontra o arquivo prm
    rota = ruta  # rota onde se guardaram os prms
    lista_prms = {}  # diccionario com os arquivos .prm criados
    cont = 0
    #######################################
    # ver posibilidad de crear una función#
    ######################################
    ######################################
    directorio_prms = rota + "prm//"
    salida_hdf = rota + "modisRecorte//"
    if os.path.exists(directorio_prms):

        print('Directorio para arquivos PRM criado...')
    else:
        a=messagebox.askquestion("Create folders", "Create folders for prm and modisRecorte ")
        if a == "yes":
            os.makedirs(directorio_prms)
            print("hola mundo")
        elif "no":
            exit()



    if os.path.exists(salida_hdf):
        print('Directorio para arquivos HDF pre-processados criado...')
    else:
        print("creando directorio")
        os.makedirs(salida_hdf)

    #######################################
    # ver posibilidad de crear una función#
    ######################################
    ######################################


    for i, values in entradas.items():
        nom = str(values)
        prms = nom[-45:-4] + ".prm"
        # prms = nom[-45:-29] + ".prm" #nombre de arquivo de saida
        shutil.copy2(template, directorio_prms + prms)

    ruta_prm = os.listdir(directorio_prms)

    if not ruta_prm:
        print(u"Não existem arquivos HDF impossível iniciar o processo...")
        exit
    else:
        for i in ruta_prm:
            if i.endswith(".prm"):
                cont = cont + 1
                lista_prms[cont] = directorio_prms + i
        print(lista_prms)
    ############################################################
    #                       PRMS Criados                       #
    ############################################################
    for i, values1 in lista_prms.items():

        with open(values1, 'r+') as abrir:
            lines = abrir.readlines()
            # print lines
            abrir.seek(0)
            abrir.truncate()
            for line in lines:
                if 'INPUT_FILENAME =' in line:
                    entrada = str(values1)
                    entrada_hdf = entrada[-45:-4] + ".hdf"
                    entrada_completa = rota + entrada_hdf
                    abrir.write("INPUT_FILENAME = " + entrada_completa + "\n")
                    # line = line.replace(line,  + values)

                elif 'OUTPUT_FILENAME' in line:
                    salida = str(values1)
                    sal_hdf = salida[-45:-29] + ".hdf"
                    sal_completa = salida_hdf + sal_hdf
                    abrir.write("OUTPUT_FILENAME = " + sal_completa + "\n")
                    # print "Encontrado....", sal_completa

                else:
                    abrir.write(line)
        abrir.close
    criar_bat(rota, directorio_prms)


def criar_bat(ruta, prms):
    dir_prms = prms
    rota = ruta
    nom_file = te3.get()
    global nom_file1
    a=len(nom_file)










    #input("Ingrese un nome para o arquivo .BAT...")

    directorio_bat = rota + "bat//"
    if os.path.exists(directorio_bat):
        print('Directorio para arquivos PRM criado...')
    else:
        os.makedirs(directorio_bat)

    completo = directorio_bat + nom_file + '.sh'
    nom_file1 = nom_file + '.sh'
    #os.chmod(nom_file1, 0o644)

    try:
        bat = os.listdir(dir_prms)
        if not bat:
            print(u"Não existem arquivos PRM impossível iniciar o processo...")
            exit
        else:
            bates = open(completo, "w")
            for i in bat:
                if i.endswith(".prm"):
                    bates.write(" resample –p " + dir_prms + i+ "\n" + "/home/martinez/Escritorio/img/modisRecorte/")




    except OSError:
        tb = sys.exc_info()[-1]
        stk = traceback.extract_tb(tb, 1)
        fname = stk[0][2]
        print(u'Rota de arquivos não existe....falho em função', fname)
    bates.close()
    ejecutar(directorio_bat,nom_file1)


def ejecutar(ruta, bats):
    rota = ruta
    cont = 0
    bat = bats
    execute = rota + bat
    try:
        arq = os.listdir(rota)
        if not arq:
            print(u"Não existem arquivos impossível iniciar o processo...")
            exit
        else:
            for i in arq:
                if i == bat:
                    p = subprocess.Popen(execute, shell=True, stdout=subprocess.PIPE)
                    stdout, stderr = p.communicate()
                    print(p.returncode)  # is 0 if success
                    print(bat)



    except OSError:
        tb = sys.exc_info()[-1]
        stk = traceback.extract_tb(tb, 1)
        fname = stk[0][2]
        print(u'Rota de arquivos não existe....falho em função', fname)


#********************FUNCIONES BOTONES*************************************


def callback():
    ruta = (te.get())
    val_empty(ruta)

def bruta ():
    te.delete(0, END)
    current_directory = filedialog.askdirectory()
    file_name = ""
    file_path = os.path.join(current_directory, file_name)
    te.insert(INSERT, file_path)

    print(file_path)



def clear ():
    list.delete(0,END)
    te.delete(0,END)
    te2.delete(0, END)

    b1.config(state=DISABLED)
    b1.update()
    te3.delete(0, END)



    te.focus_set()

def prm2():
    te2.delete(0, END)
    ventana.filename = filedialog.askopenfilename(initialdir="/home/martinez/", title="Select file",
                                                      filetypes=((" files", "*.prm"), ("all files", "*.*")))
    te2.insert(INSERT, ventana.filename)
    prm = ventana.filename

    print (prm)


    global prm


def activar_run():
    b4.config(state=ACTIVE)
    te2.focus_set()
    b5.config(state=ACTIVE)

def act_run():
    te3.focus_set()
    b5.config(state=ACTIVE)
    b6.config(state=ACTIVE)

def run1():
    nom_file = te3.get()
    a = len(nom_file)
    if a >0:
        b1.config(state=ACTIVE)
    else:
        messagebox.showinfo("Say Hello", "Diguite nombre para el archivo .bat")

#**************************************************************************








ventana = Tk()
ventana.title("procesamiento de imagenes ")
ventana.config (bg="#036C1A")
#*********************Comandos de interface*****************************************
w = Label(ventana, text="Seleccione  la ruta .HDF" )
w.place(relx=1, x=-500, y=30, anchor=CENTER)
w2 = Label(ventana, text="Seleccione Archivo .PRM" )
w2.place(relx=1, x=-500, y=60, anchor=CENTER)

w3 = Label(ventana, text="Diguite Nombre Para .bat" )
w3.place(relx=1, x=-500, y=90, anchor=CENTER)



te= Entry(ventana)

te.place(relx=1, x=-350, y=30, anchor=CENTER)
te.focus_set()

te2= Entry(ventana)
te2.get()
te2.place(relx=1, x=-350, y=60, anchor=CENTER)

te3= Entry(ventana)
te3.get()
te3.place(relx=1, x=-350, y=90, anchor=CENTER)





b= Button(ventana, text="...", width=5, command=bruta )
b.place(relx=1, x=-230, y=30, anchor=CENTER)

b4= Button(ventana, text="...", width=5, command=prm2 )
b4.config(state=DISABLED)

b4.place(relx=1, x=-230, y=60, anchor=CENTER)

b1 = Button(ventana, text="Run", width=5, command=callback)
b1.config(state=DISABLED)
b1.place(relx=1, x=-160, y=90, anchor=CENTER)

b2 = Button(ventana, text="Next", width=5, command=activar_run)
b2.place(relx=1, x=-160, y=30, anchor=CENTER)

b5 = Button(ventana, text="Next", width=5, command=act_run)
b5.place(relx=1, x=-160, y=60, anchor=CENTER)
b5.config(state=DISABLED)

b6 = Button(ventana, text="Next", width=5, command=run1)
b6.place(relx=1, x=-230, y=90, anchor=CENTER)
b6.config(state=DISABLED)

b3 = Button(ventana, text="Clear", width=5, command=clear)
b3.place(relx=1, x=-50, y=50, anchor=CENTER)







#*************************************************************************************

##################MENU####################










ventana.geometry("700x500")
ventana.resizable(False, False)

list = Listbox(ventana, width=80,height=20)
list.place(relx=1, x=-350, y=300, anchor=CENTER)
#list.pack()








#listbox.pack()
ventana.grab_set()
mainloop()













