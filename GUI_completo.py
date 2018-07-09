from tkinter import *

class Menu:
    def __init__(self,master):
        self.master = master
        self.master.title("Menu")
        self.master.geometry("250x200")
        self.label1 = Label(self.master,text='BEM-VINDO',fg='blue').grid(row=0,column=0)
        
        self.label2 = Button(self.master, text = 'Verificar numero do cartao de cidadao', width = 20, padx = 50, command=self.gotCc).grid(row=1,column=0)
        self.botao2 = Button(self.master, text = 'Verificar numero de identificacao fiscal', width = 20, padx = 50, command = self.gotNIF).grid(row = 2, column = 0)
        
        self.botao = Button(self.master, text = 'Sair da verificacao',width = 20, padx = 50, command = self.master.destroy).grid(row = 3, column = 0)
        
    def gotCc(self):
        root3=Toplevel(self.master)
        meuGUI=Cc(root3)
        
    def gotNIF(self):
        root4 = Toplevel(self.master)
        meuGUI = NIF(root4)
        
class Cc():
    def __init__(self,master):
        self.master = master
        self.master.title('Verificacao Cartao de Cidadao')
        
        self.pesquisa = StringVar()
        self.master.geometry("500x200+100+200")
        self.label1= Label(self.master,text='Bem-vindo a verificacao do cc',fg='blue').grid(row=0,column=1)
        self.label2= Label(self.master,text='Introduza um numero do cartao de cidadao: ').grid(row=1,column=0)
        
        self.entrada= Entry(self.master,textvariable=self.pesquisa).grid(row=1,column=1)
        self.botao= Button(self.master,text='Verificacao', width = 20, padx = 50, command=self.verificacao).grid(row=2,column=0)
    
        self.botao = Button(self.master, text = 'Sair da verificacao',width = 20, padx = 50, command = self.master.destroy).grid(row = 3, column = 0)
        
        
    def verificacao(self):
        listaalfa = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        listanum = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]        
         
        cc1 = self.pesquisa.get()
        cc = cc1.lower()
        print(cc)
        soma = 0
        if len(cc) != 12:
            print('numero de cartao de cidadao invalido')
            self.labelresult = Label(self.master,text='cc invalido', fg='red').grid(row=2,column=1)
        else:
            for i in range (len(cc)-1,-1,-1):
                if i % 2 == 0:
                    if cc[i] in listaalfa:
                        pos = listaalfa.index(cc[i])
                        soma +=  listanum[pos]*2
                        if listanum[pos]*2 >= 10:
                            soma -= 9            
                else:
                    if cc[i] in listaalfa:
                        pos = listaalfa.index(cc[i])
                        soma +=  listanum[pos]
                            
            soma = soma % 10
            
            if soma == 0:
                print('cartao de cidadao valido')
                self.labelresult1 = Label(self.master,text='cc valido',fg='green').grid(row=2,column=1)
            else:
                print('cartao de cidadao invalido')
                self.labelresult2 = Label(self.master,text='cc invalido',fg='red').grid(row=2,column=1)
        
class NIF():
    def __init__(self,master):
        self.master = master
        self.master.title('Verificacao do NIF')
        
        self.pesquisa = StringVar()
        self.master.geometry("500x200+100+200")
        self.label1= Label(self.master,text='Bem-vindo a verificacao do NIF',fg='blue').grid(row=0,column=1)
        self.label2= Label(self.master,text='Introduza um numero do NIF: ').grid(row=1,column=0)
    
        self.entrada= Entry(self.master,textvariable=self.pesquisa).grid(row=1,column=1)
        self.botao= Button(self.master,text='Verificacao', width = 20, padx = 50, command=self.verificacao).grid(row=2,column=0)
        
        self.botao = Button(self.master, text = 'Sair da verificacao',width = 20, padx = 50, command = self.master.destroy).grid(row = 3, column = 0)

    def verificacao(self):
        nif = self.pesquisa.get()
        
        soma = 0
        verificacao = 0
        if len(nif) != 9:
            print('invalido')
            self.labelresult2 = Label(self.master, text='NIF invalido', fg='red').grid(row=2, column=1)
            return
        else:
            index = 7
            for i in range(2,10):
                soma += int(nif[index])*i
                index -= 1
            if soma >10:
                soma = 11-soma
            else:
                pass
            verificacao = soma % 11
            if verificacao == int(nif[8]):
                print('valido')
                self.labelresult1 = Label(self.master,text='NIF valido',fg='green').grid(row=2,column=1)
            else:
                print('invalido')
                self.labelresult2 = Label(self.master,text='NIF invalido',fg='red').grid(row=2,column=1)
            
def main():
    root = Tk()
    meuGUI= Menu(root)
    root.mainloop()
        
if __name__ == '__main__':
    main() 
