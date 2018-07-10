Portuguese ID and NIF validation checker
===

* This was part of a project when I was student at *University of The Azores*.  
* The code works with python 3.6  
* The code may contain **portuguese language**  
* The Python file contains a GUI.  

---
The portuguese ID, known in Portugal as *Cartão de cidadão*, is the first part of the code.  
The algorithm is in the pdf file along with this post and has a example code in C#. Since we were learning Python 3, we had to translate the C# code into pyhton. 
if you want only the function I create to validate the ID/CC, you can copy the following code:  
'''

    def verificacao():
        listaalfa = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        listanum = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]        
         
        cc1 = input()
        cc = cc1.lower()
        print(cc)
        soma = 0
        if len(cc) != 12:
            print('numero de cartao de cidadao invalido')
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
            else:
                print('cartao de cidadao invalido')
     
'''
---
The NIF, known in Portugal as *Numero de Identificação Fiscal*, or Fiscal Code, was made with the guide of the portuguese wikipedia (https://pt.wikipedia.org/wiki/N%C3%BAmero_de_identifica%C3%A7%C3%A3o_fiscal).  
if you want only the python code:  
'''

    def verificacao():
        nif = input()
        
        soma = 0
        verificacao = 0
        if len(nif) != 9:
            print('invalido')
            return
        else:
            index = 7
            for i in range(2,10):
                soma += int(nif[index])*i
                index -= 1
            verificacao = soma % 11
            if verificacao == 0 or verificacao == 1:
                verificacao = 0
            else:
                verificacao = 11 - verificacao
            if verificacao == int(nif[8]):
                print('valido')
            else:
                print('invalido')
                

'''
