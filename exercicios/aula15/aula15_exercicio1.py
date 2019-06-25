class  MeuTempo :

    def  __init__ (self ,  hrs = 0 ,  mins = 0 ,  segs = 0): 
        """ Criar um novo objeto MeuTempo inicializado para hrs, min, segs. 
           Os valores de mins e segs podem estar fora do intervalo de 0-59, 
           mas o objecto MeuTempo resultante será normalizado.  """ 
        # Calcular total de segundos para representar 
        self.totalsegs =  hrs * 3600  +  mins * 60  +  segs 
        self.horas =  self.totalsegs  //  3600  # Divisão em h, m, s 
        restosegs =  self.totalsegs  %  3600 
        self.minutos  =  restosegs  //  60 
        self.segundos  =  restosegs  %  60
        if self.horas >= 24:
            self.horas = self.horas%24


    def  to_seconds (self): 
        "" "Retorna o número de segundos representados por esta instância " "" 
        return  self.totalsegs
    

    def  __add__ (self, other): 
        """ Retorna a soma do tempo atual e outro, para utilizar com o símbolo + """
        return  MeuTempo (0, 0, self.to_seconds() + other.to_seconds())


    def  __sub__ (self, other): 
        """ Retorna a soma do tempo atual e outro, para utilizar com o símbolo - """
        return  MeuTempo (0, 0, self.to_seconds() - other.to_seconds())


    def __str__ (self):
        return f'{self.horas}:{self.minutos}:{self.segundos}'


    def  add_time (t1, t2): 
        h = t1.horas + t2.horas 
        m = t1.minutos + t2.minutos 
        s = t1.segundos + t2.segundos

        while s >= 60:
            s = s - 60
            m = m + 1

        while m >= 60:
            m = m - 60
            h = h + 1
 
        sum_t  =  MeuTempo (h, m, s) 
        return  sum_t


    def incremento (t, segs): 
        t.segundos += segs 

        while  t.segundos >= 60: 
            t.segundos -= 60 
            t.minutos += 1 

        while  t.minutos >= 60: 
            t.minutos -= 60 
            t.horas += 1


    def  depois (self, time2): 
        "" "Retorna True se self for estritamente maior que time2" "" 
        if  self.horas > time2.horas: 
            return  True 
        if  self.horas < time2.horas: 
            return  False 
        if  self.minutos > time2.minutos: 
            return  True 
        if  self.minutos < time2.minutos: 
            return  False 
        if  self.segundos > time2.segundos: 
            return  True 
        return  False

t1 = MeuTempo(12, 30, 26)
t2 = MeuTempo(10, 52, 36)
print(t1, t2)
print(t1 + t2)
print(t1 - t2)
print(t1.depois(t2))  # Mostra se é True ou False que t1 vem depois de t2
hora_atual = MeuTempo(11, 59, 30)
tempo_bolo = MeuTempo(18, 40, 190)
bolo_pronto = MeuTempo.add_time(hora_atual, tempo_bolo)
hora_atual.incremento(500)  # incrementar em 500 segundos = 6 minutos e 20 segundos
print(hora_atual)
print(bolo_pronto)
