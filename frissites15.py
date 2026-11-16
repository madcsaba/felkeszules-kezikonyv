#!/usr/bin/env python3
"""
A 15. fejezet „Közzététel előtt a hazai hatóságoktól pontosítandó" listája:
minden pont mellé a megkérdezés helye (kihez, hol) kerül.

A lista a kézikönyv azon pontjait tartalmazza, amelyekhez nincs nyilvános
hivatalos magyar adat – de a hatóság meg tudja mondani. A „kipipálható" jelölés
a szerkesztőnek marad: a pont akkor zárható, ha a válasz megvan.
"""
import io, re, sys

F = 'index.html'
h = io.open(F, encoding='utf-8').read()

REGI = '''    <ul class="checklist">
      <li><label><input type="checkbox"><span>A kijelölt vészhelyzeti rádió- és tévéadó, valamint a frekvenciák (Kossuth Rádió és helyi adók).</span></label></li>
      <li><label><input type="checkbox"><span>A lakossági SMS- vagy cell broadcast riasztás működése és a telefonon szükséges beállítások.</span></label></li>
      <li><label><input type="checkbox"><span>A háborús légiriadó és a „légiriadó vége” hazai szirénajele; a MoLaRi-rendszeren kívüli települések riasztási módja.</span></label></li>
      <li><label><input type="checkbox"><span>Az óvóhelyek és védett helyek nyilvántartása, jelölése és elérhetősége.</span></label></li>
      <li><label><input type="checkbox"><span>A jódtabletta hazai ajánlása és beszerzése (pl. a paksi atomerőmű körzetében).</span></label></li>
      <li><label><input type="checkbox"><span>Az önkormányzati gyülekezőpontok, vízosztó helyek és kiürítési tervek.</span></label></li>
      <li><label><input type="checkbox"><span>A honvédelmi kötelezettség és a polgári védelmi kötelezettség hazai szabályai, ha a kiadvány kitér rájuk.</span></label></li>
      <li><label><input type="checkbox"><span>Akadálymentes változatok: könnyen érthető kiadás, jelnyelvi videó, hangos és Braille-változat, idegen nyelvű kiadások.</span></label></li>
    </ul>'''

UJ = '''    <ul class="checklist">
      <li><label><input type="checkbox"><span>A kijelölt vészhelyzeti rádió- és tévéadó, valamint a frekvenciák. <em>Kérdezd: az önkormányzatnál és a megyei katasztrófavédelmi igazgatóságnál, melyik rádióállomás sugározza a polgári védelmi tájékoztatást.</em></span></label></li>
      <li><label><input type="checkbox"><span>A cell broadcast alapú lakossági riasztás aktuális állapota és a telefonon szükséges beállítások. <em>Kérdezd: a Nemzeti Média- és Hírközlési Hatóságnál (nmhh.hu), hol tart a végrehajtási rendelet és a tesztüzeme.</em></span></label></li>
      <li><label><input type="checkbox"><span>A háborús „légiriadó” és a „légiriadó vége” hazai szirénajele; a MoLaRi-rendszeren kívüli települések riasztási módja. <em>Kérdezd: a megyei katasztrófavédelmi igazgatóságnál és a polgári védelmi szerveknél.</em></span></label></li>
      <li><label><input type="checkbox"><span>Az óvóhelyek és védett helyek nyilvántartása, jelölése és elérhetősége. <em>Kérdezd: az önkormányzatnál (polgári védelem) és a megyei katasztrófavédelmi igazgatóságnál.</em></span></label></li>
      <li><label><input type="checkbox"><span>A jódtabletta hazai ajánlása és beszerzése (pl. a paksi atomerőmű körzetében). <em>Kérdezd: az illetékes megyei katasztrófavédelmi igazgatóságnál és a gyógyszertárnál.</em></span></label></li>
      <li><label><input type="checkbox"><span>Az önkormányzati gyülekezőpontok, vízosztó helyek és kiürítési tervek. <em>Kérdezd: az önkormányzatnál – a kiürítési terv és a gyülekezőpontok helye a polgári védelmi feladat.</em></span></label></li>
      <li><label><input type="checkbox"><span>A honvédelmi kötelezettség és a polgári védelmi kötelezettség hazai szabályai, ha a kiadvány kitér rájuk. <em>Kérdezd: a katasztrófavédelmi igazgatóságnál és a Védelmi Igazgatási Hivatalnál.</em></span></label></li>
      <li><label><input type="checkbox"><span>Az állatkimenekítés hazai rendje (nagyüzemi kimenekítési tervek, hatósági eljárás). <em>Kérdezd: az állategészségügyi hatóságnál és a jegyzőnél.</em></span></label></li>
      <li><label><input type="checkbox"><span>A nemzetközi segélyjelző rendszer (fehér–piros–kék) magyar megfelelője. <em>Kérdezd: a megyei katasztrófavédelmi igazgatóságnál; hazai hivatalos változat nincs.</em></span></label></li>
      <li><label><input type="checkbox"><span>Akadálymentes változatok: könnyen érthető kiadás, jelnyelvi videó, hangos és Braille-változat, idegen nyelvű kiadások. <em>Ez a kiadó feladata – a kiadás összeállításakor dönthető el.</em></span></label></li>
    </ul>'''

if REGI not in h:
    print("✗ a lista nem található")
    sys.exit(1)

h = h.replace(REGI, UJ, 1)
io.open(F, 'w', encoding='utf-8').write(h)
print("✓ a 15. fejezet listája frissítve: 10 pont, mindegyiknél a megkérdezés helye")
