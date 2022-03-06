from asyncio.windows_events import NULL
from math import gcd
from random import randint, randrange
import random
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
global entry
global entry1
global entry2
global entry3
global var2
global liste1

fenetre = Tk()

fenetre.title("Chiffrement")

texte2 = LabelFrame(fenetre, text="Choisissez le niveau de chiffrement souhaité :")
texte2.grid(row=1, sticky='w')

var1 = IntVar()
case1 = ttk.Radiobutton(texte2, text="Chiffrement moyen", variable=var1, value=1)
case1.grid(sticky='w')
case2 = ttk.Radiobutton(texte2, text="Chiffrement élvé avec 2 clés", variable=var1, value=2)
case2.grid(sticky='w')
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','&','é','(','-','è','_','ç','à',')','=','$','^','*','ù','!',':',';',',','<','>','§','/','.','?','%','µ','£','¨','+','°','@','^','`','|','[','{','#','~','}',']',' ']
chain = ["la chaine chiffré est : "]
premierp = [7,11]
premierq = [19,17]
def top():
        cas1 = Toplevel()
        cas1.geometry("675x250")
        cas1.title("Chiffrement moyen")
        ma_va1 = StringVar()
        ma_va2 = StringVar()
        i = IntVar()
        texte1 = LabelFrame(cas1, text="Entrer votre chaine de caractere :")
        texte1.grid(row=0, column=1, sticky='w', padx=10)
        texte2 = LabelFrame(cas1, text="Entrer votre clé de chiffrement :")
        texte2.grid(row=1, column=1, sticky='w', padx=10)
        ma_va1 = Text(texte1, height=8)
        ma_va1.grid(row=3, column=1, sticky='w', padx=10)
        entry2 = ttk.Entry(texte2, textvariable=ma_va2)
        entry2.grid()
        def chifmoy():
            for i in range(len(ma_va1.get('1.0','end'))-1):
              for j in range(len(alphabet)):
                  if ma_va1.get('1.0','end')[i]==alphabet[j]:
                   m=j
              for k in range(len(alphabet)):
                  if ma_va2.get()[i%len(ma_va2.get())]==alphabet[k]:
                   n=k
              x = (m+n) % 104
              print(alphabet[x],end="")
            print()
        def dechifmoy():
            for i in range(len(ma_va1.get('1.0','end'))-1):
              for j in range(len(alphabet)):
                  if ma_va1.get('1.0','end')[i]==alphabet[j]:
                   m=j
              for k in range(len(alphabet)):
                  if ma_va2.get()[i%len(ma_va2.get())]==alphabet[k]:
                   n=k
              x = (m-n) % 104
              print(alphabet[x],end="")
            print()
        button3 = ttk.Button(cas1, text="chiffrer", command=chifmoy)
        button3.grid(row=2, column=1, sticky='w')
        button4 = ttk.Button(cas1, text="dechiffrer", command=dechifmoy)
        button4.grid(row=3, column=1, sticky='w')
        cas1.mainloop()
def top2():
        cas2 = Toplevel()
        cas2.geometry("700x290")
        cas2.title("Chiffrement moyen")
        ma_va1 = StringVar()
        ma_va2 = IntVar()
        ma_va3 = IntVar()
        i = IntVar()
        texte1 = LabelFrame(cas2, text="Entrer votre chaine de caractere :")
        texte1.grid(row=0, column=1, sticky='w', padx=10)
        texte2 = LabelFrame(cas2, text="Entrer votre 1er clé de chiffrement :")
        texte2.grid(row=1, column=1, sticky='w', padx=10)
        texte3 = LabelFrame(cas2, text="Entrer votre 2eme clé de chiffrement :")
        texte3.grid(row=2, column=1, sticky='w', padx=10)
        ma_va1 = Text(texte1, height=8)
        ma_va1.grid(row=3, column=1, sticky='w', padx=10)
        entry2 = ttk.Entry(texte2, textvariable=ma_va2)
        entry2.grid()
        entry3 = ttk.Entry(texte3, textvariable=ma_va3)
        entry3.grid()
        def chifelv():
            def egcd(a, b):
             if a == 0:
              return (b, 0, 1)
             else:
              g, y, x = egcd(b % a, a)
             return (g, x - (b // a) * y, y)

            def modinv(a, m):
             g, x, y = egcd(a, m)
             if g != 1:
              raise Exception('modular inverse does not exist')
             else:
              return x % m
            p=randrange(0,2)
            q=randrange(0,2)
            Q=(premierp[p]-1)*(premierq[q]-1)
            n=premierp[p]*premierq[q]
            e=2
            while e<n and gcd(e,Q)!=1:
                e=e+1
            for i in range(len(ma_va1.get('1.0','end'))-1):
              j=0
              while ma_va1.get('1.0','end')[i]!=alphabet[j]:
                  j=j+1
              z = (j**e) % n
              print(z,end=";")
            print('')
            print('d = ',modinv(e,Q),'n =', n,' e :',e,' Q :',Q,' p :',premierp[p],' q :',premierq[q])
        def dechifelv():
            c='0'
            cpt=0
            for i in range(len(ma_va1.get('1.0','end'))-1):
                cpt=cpt+1
                if ma_va1.get('1.0','end')[i]!=";":
                    c+=ma_va1.get('1.0','end')[i]
                if ma_va1.get('1.0','end')[i]==";" or cpt==len(ma_va1.get('1.0','end'))-1:
                    r=int(c)
                    w = ((r**ma_va2.get()) % ma_va3.get()) % 103
                    print(alphabet[w],end="")
                    c='0'
            print()
        button3 = ttk.Button(cas2, text="chiffrer", command=chifelv)
        button3.grid(row=4, column=1, sticky='w')
        button4 = ttk.Button(cas2, text="dechiffrer", command=dechifelv)
        button4.grid(row=5, column=1, sticky='w')
        cas2.mainloop()
button1 = ttk.Button(fenetre, text="Suivant", command=lambda: suivant(var1))
button1.grid(row=7, column=0, sticky='w')

button3 = ttk.Button(fenetre, text="Quitter", command=fenetre.destroy)
button3.grid(row=7, column=1)
def suivant(var1):
    k = var1.get()
    if k == 1:
        top()
    if k == 2:
      top2()
fenetre.mainloop()