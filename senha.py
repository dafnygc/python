               SENHA 
senha = "1234"

qsenha = input("Digite sua senha: ")

if (senha == qsenha):
    print("acesso permitido")
else:
    print("acesso negado")


            MACA
maca = int()
qmaca = int(input("Digite a quantia e maaas que deseja comprar"))

if qmaca < 12:
    maca = 0.30
 else:
     maca = 0.25
     print("o valor total é",qmaca * maca)

n1 = int (input ("escolha o primeiro numero"))
n2 = int (input ("escolha o segundo numero"))
n3 = int (input ("escolha o terceiro numero"))

if n1 < n2 and n1 < n2 
  p1 = n1
  if n2< n1 and n2 < n3 
  p1 = n2
  else:
    p1 = n3

    RANGER

            for i in range (1,10):
print (i)

nome = input ("digite seu nome")
idade = input ("digite sua idade")
sexo = input ("digite seu sexo")

nome = input ("digite seu nome")
idade = input ("digite sua idade")
sexo = input ("digite seu sexo")

nome = input ("digite seu nome")
idade = input ("digite sua idade")
sexo = input ("digite seu sexo")

print ("nome:",nome )
print ("idade:", idade)
print ("sexo:", sexo)

print ("nome:",nome )
print ("idade:", idade)
print ("sexo:", sexo)

print ("nome:",nome )
print ("idade:", idade)
print ("sexo:", sexo)


b = int(input("digite o valor da base:"))
e = int(input("digite o valor da exponente:"))
r = b
for (i in range (1,e)
     r=r*b
     print(resultado:"," {:.2f}".format(r))


def Forca (tentativas):
   f1 = "       +-------+ "
   f2 = "       |         "
   f3 = "       |         "
   f4 = "       |         "
   f5 = "       |         "
   f6 = "       |         "
   f7 = " ______|______   "

   if tentativas >= 1: 
      f1 = "  |   |    " 

   if tentativas >= 2: 
      f2 = " |    |  "

   if tentativas >= 3:
      f3 = " |    | "

   if tentativas >= 4: 
      f4 = " |    | "

   if tentativas >= 5: 
      f5 = " |    | "

   if tentativas >= 6: 
      f6 = " |    | "

      if tentativas >= 7: 
         f7 = " |    / "

   if tentativas >= 8: 
      f8 = " |    / \ "

   print(f1)
   print(f2)
   print(f3)
   print(f4)
   print(f5)
   print(f6)
   print(f7)
   print(f8)

def continua():
   while True:
      print("-" * 20)
      novamente = input("Quer jogar novamente:S/N").upper()
      acabou = False
      break
   else:
     print("digite S ou N ")
     return Acabou 

Forca(0)

def sorteiapalavra():
   lista=["amor","ola","tudo bem","tchau",]
   return random.choice(lista)

import random
print(sorteiapalavra)

def apresentapalavra(letras,palavras):
   npalavra="_" * len(palavras)
   print(apresentapalavra("ab","amor"))

   print(apresentapalavra( "ab","abacaxi"))
   for l in range(len(palavra)):
     print(palavra[p])
   if letra[l]==palavras[p]:
      print(letras[l])
      print(l)
      print(p)

      return npalavra
def apresentaPalavras(letras,palavras):
    novaPalavras= "_" * len(palavras)
    for L in range(0,len(letras)):
        for P in range (0,len(palavras)):
            if palavras[P]==letras[L]:
                novaPalavras = novaPalavras[0:P*2]+palavras[P]+" "+novaPalavras[P*2:]
                return palavras

            listafrutas=["uva","melancia","banana"]
frutas="uva"
print(listafrutas[1])
print(frutas[1])
print(listafrutas[2][0])
listafrutas.append("abacaxi")
print(listafrutas)
listafrutas.remove("banana")
print(listafrutas)
listafrutas.sort()
print(listafrutas)

with open("arqTXT/nome.txt","r") as arquivo:
     while True:
             txt = arquivo.read()
             if not txt:
                    break
             print(txt)
                
with open("arqTXT/nome.txt", "r") as f:
       listaTexto = f.readlines()
       for texto in listaTexto:
        print(texto)
with open("arqTXT/nome2.txt","W") as f: 
      f.write('Dafny\n')
      f.write('Guetten\n')
      f.write('Cora\n')


def criar_conta(numero,nome,saldo inicial,limite):
    conta={"numero":numero,"nome":nome,"saldo inicial":saldo}
    return conta
def saldo(conta):
    print("contanumero:{}",format(conta["numero"]))
    print("nome:nome"+conta["nome"])
    print("saldo"{}.format(conta["saldo"]))


conta1=criar_conta(1234,"Dafny",50,100)
saldo(conta01)
saldo(contas02)

def extrato(conta):
    print("conta{}saldo{}".format(conta["numero"],conta["saldo"]))
def deposito(conta,valor):
    conta["saldo"]+=valor 
    return
 
def saque(conta,valor):
    if((conta["saldo"]+["limite"])-valor)>=0:conta["saldo"]-=valor
    return

deposito(conta01,100)
extrato(conta01)
deposito(conta02,80)
extrato(conta02,)
sacar(conta01,30)
sacar(conta02,20)






for i in range (1,100):
    print(i)
    i=0
    c=True
    while c:
     i=i+1
    print(i)
    if i <=99:
      c=False


      with open("arquivo.txt","r") as f:
    txt=f.readline()
    print(txt)
    txt2=f.readline()
    print(txt2)

with open("arquivo.txt2","r") as f:
    f=f.readline()
    print(l)
    for ln in l:
     print(ln)

with open("arquivo.txt","r") as f:
   texto=f.read()
   print(texto)

   with open("arquivo.txt","w") as f:
        f.write("text 1\h")
        f.write("text 2\h")

try:
  f=open("arquivo2.txt","w")
  f.write("eu 1\h")
  f.write("eu 2\h")
finally:
  f.close()

class conta:
    def __init__(self,numero,titular,saldo inicial,limite):
        self.numero=numero
        self.titular=titular
        self.saldo=saldo
        self.limite=limite









conta1=conta 
print(conta1) 
conta1=conta(134,"Dafny",600.00,50.00)
print(conta1)


from cliente import cliente

cliente("leandro")

print(cliente.nome)

print("metodo nome do cliente;,cliente.get_nome")

class cliente:
    def__init__(self, nome);
        self.__nome = nome 
    
    
    def get_nome(self):
        return self.__nome.title()
    
    @property
    def nome(self):
        return self.__nome.title()



def retangulo(tipoR,largura,altura):
    r=0
    if tipoR == "area":
     r=largura*altura
    elif tipoR == "Perimetro":
      r=2*(largura+altura)
    return r
    

def circulo(tipoR,largura,altura):
    r=0
    if tipoR == "area":
     r=largura*altura
    elif tipoR == "Perimetro":
        r=2*(largura+altura)
    return r
    
    
a= retangulo("area",15,4.5)
print(f´area:{a}´)
      
def verifica_reultado(alturalargura,raio):
  print(f´ retangulo area:{ retangulo("area",largura,altura)}´)
 print(f´ŕetangulo Perimetro:{retangulo("perimetro,largura,altura")})

 verifica_resultado(15,6,7,8)
