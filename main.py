import time

tempoParado = 0
avioesAguardandoChassi = []
avioesComChassi = []
avioesAguardandoAsa = []
avioesComAsa = []
avioesAguardandoCabine = []
avioesComCabine = []
avioes = []

class Aviao:
    chassi = False
    asa = False
    cabine = False


def adicionarChassi():
    global tempoParado
    if(len(avioesAguardandoChassi) > 0):
        aviao = avioesAguardandoChassi.pop()
        aviao.chassi = True
        avioesComChassi.append(aviao)
    else:
        tempoParado += 1


def adicionarAsas():
    global tempoParado
    if(len(avioesAguardandoAsa) > 0):
        aviao = avioesAguardandoAsa.pop()
        if(aviao.chassi == False):
          raise "Avião deve ter chassi para adicionar asa!"
        aviao.asa = True
        avioesComAsa.append(aviao)
    else:
        tempoParado += 1


def adicionarCabine():
    global tempoParado
    if(len(avioesAguardandoCabine) > 0):
        aviao = avioesAguardandoCabine.pop()
        if(aviao.chassi == False):
          raise "Avião deve ter asa para adicionar cabine!"
        aviao.cabine = True
        avioesComCabine.append(aviao)
    else:
        tempoParado += 1

def enviarAvioesComChassiParaAdicionarAsas():
    avioesAguardandoAsa.extend(avioesComChassi)
    avioesComChassi.clear()

def enviarAvioesComAsaParaAdicionarCabine():
      avioesAguardandoCabine.extend(avioesComAsa)
      avioesComAsa.clear()

cont = 0
while(cont < 30):
    aviao = Aviao()
    avioes.append(aviao)
    avioesAguardandoChassi.append(aviao)

    if(len(avioesComChassi) == 5):
      enviarAvioesComChassiParaAdicionarAsas()
        
    if(len(avioesComAsa) == 5):
      enviarAvioesComAsaParaAdicionarCabine()   

    adicionarChassi()
    adicionarAsas()
    adicionarCabine()

    avioesProntos = 0

    for a in avioes:
        if(a.chassi and a.asa and a.cabine):
            avioesProntos += 1

    print("------------------------------------------------------")
    print("Tempo: " + str(cont+1) + " segundos")
    print("Avioes esperando chassi: " + str(len(avioesAguardandoChassi)))
    print("Avioes esperando asa: " + str(len(avioesAguardandoAsa)))
    print("Avioes esperando cabine: " + str(len(avioesAguardandoCabine)))
    print("Quantidade de aviões fabricados: " + str(avioesProntos))
    print("Desperdicio de tempo: " + str(tempoParado))
    print("Aviões incompletos: " + str(len(avioes) - avioesProntos))
    time.sleep(1)
    cont += 1
