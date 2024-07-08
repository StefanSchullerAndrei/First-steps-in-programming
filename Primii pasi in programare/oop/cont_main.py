from oop.cont_bancar import ContBancar

cont1 = ContBancar('Stefan S', 'R1199')
cont2 = ContBancar('Stefan Andrei' , 'R2314')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.alimentareCont(300)
cont2.alimentareCont(700)
cont2.alimentareCont(500)
cont1.alimentareCont(600)

cont1.plataCard(800)
cont2.plataCard(700)
cont2.plataCard(200)

cont1.interogareSold()
cont2.interogareSold()

#tema
#clasa angajat
#nume, prenume, salariu, vechime
#constructor : nume, prenume, salariu, functie, vechime
#metode
#descriere buna sunt x sunt din y am z ani etc
#marire salariu in functie de vechime
# actualizare vechime(parametru  noua vechime)
      #self.vechime = noua_vechime
#daca are vechime sub 5 ani, marim cu 300, peste 5 ani, 500