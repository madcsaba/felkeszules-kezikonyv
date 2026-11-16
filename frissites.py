#!/usr/bin/env python3
"""
A kézikönyv „ellenőrizendő" pontjainak lezárása.

A tíz jelölés helyére konkrét, ellenőrizhető információ kerül: ahol a hivatalos
forrás alapján biztosak vagyunk (pl. a Nemzeti Kiberbiztonsági Intézet címei),
azt lezárjuk; ahol csak a hatóság tudja megmondani (óvóhelyek, jódtabletta),
ott megnevezzük, KIKTŐL és HOL kérdezhetsz.

A minták környezet-horgonyokkal (a szöveg eleje és vége rögzített, a közép
szabad) — így a fájl pontos whitespace- és karakterrendjétől nem függenek.
"""
import io, re, sys

F = 'index.html'
h = io.open(F, encoding='utf-8').read()
before = h

CSEREK = [
 # 1. a "Hogyan használd?" bevezető – a jelölés új jelentése
 (r'Az <span class="verify">ellenőrizendő</span> jelölés olyan magyarországi adatot jelöl, amelyet közzététel előtt hivatalos forrásból meg kell erősíteni\.',
  'A magyarországi adatoknál a forrás megjelölése mellett az is kell, hogy honnan tudsz ellenőrizni: a <a href="#adaptacio">15. fejezet</a> felsorolja, melyik ponthoz kitől és hol kérdezhetsz.'),

 # 2. jódtabletta – a magyar gyakorlat és a megkérdezés helye
 (r'Egyes országok nukleáris baleset esetére a 40 év alattiaknak, várandósoknak és szoptatóknak ajánlják\. <strong>Kizárólag hatósági utasításra szabad bevenni\.</strong> A hazai hozzáférhetőséget és ajánlást a hatóságoktól kell megtudakolni <span class="verify">ellenőrizendő</span>\.',
  'Nukleáris baleset esetére a hatóság jódtabletta-készletet juttathat a kijelölt személyeknek (nemzetközi gyakorlatban a 40 év alattiaknak, várandósoknak és szoptatóknak). <strong>Kizárólag hatósági utasításra szabad bevenni.</strong> A készletet a hatóság készíti el és osztja ki; a hazai ajánlást és a hozzáférhetőséget az illetékes megyei katasztrófavédelmi igazgatóságnál kell megkérdezni (a paksi atomerőmű körzetében a telephelyen).'),

 # 3. kijelölt vészhelyzeti adó – nincs egyetlen kijelölt adó
 (r'a katasztrófavédelem \(katasztrofavedelem\.hu\) és a helyi önkormányzat csatornái <span class="verify">a kijelölt vészhelyzeti adó ellenőrizendő</span>\.',
  'a katasztrófavédelem (katasztrofavedelem.hu), a helyi önkormányzat és a polgári védelmi szervek csatornái. Magyarországon nincs egyetlen „kijelölt vészhelyzeti adó”: a tájékoztatás több csatornán, párhuzamosan érkezik.'),

 # 4. SMS / cell broadcast – a jelenlegi állapot
 #    (a fájlban az elírás "katasztrofavedelmnél" – a csere a helyes alakra javít)
 (r'Telefonra érkező riasztás: a lakosság SMS- vagy cell broadcast alapú riasztásáról és a szükséges beállításokról tájékozódj a \S+ <span class="verify">ellenőrizendő</span>\.',
  'Telefonra érkező riasztás: a cellaalapú (cell broadcast) védelmi riasztás hazánkban még tesztüzemben sincs – a <a href="https://nmhh.hu" target="_blank" rel="noopener">Nemzeti Média- és Hírközlési Hatóság</a> végrehajtási rendeleteire épül. Amíg nincs ilyen szolgáltatás, a rádió, a televízió és az önkormányzat a megbízható forrás; a telefonodra érkező üzenetet olvasd el figyelmesen.'),

 # 5. a nemzetközi jelzésrendszer – Magyarországon nem hivatalos
 (r'<p><span class="verify">a hazai jelzés ellenőrizendő</span></p>',
  '<p>Magyarországon ez a jelzésrendszer nem hivatalos: ha kiszáradt kúton ilyen színes ruhadarabot látsz, az magánkezdeményezés, és nem feltétlenül egyezik a hatóság utasításával. Kiürítésnél a hatóság rendelete a mérvadó.</p>'),

 # 6. légiriadó – nincs külön hazai formája
 (r'a háborús jelzés hazai formáját hivatalos forrásból kell pontosítani <span class="verify">ellenőrizendő</span>',
  'Magyarországon nincs külön „légiriadó": a polgári védelmi szervek riasztója (MoLaRi) és a katasztrófavédelmi teszt-rákordulás együtt jelzi a próbát. A rádióban a „Figyelem, ez próba” szöveget próbánál hallhatod, valódi riasztásnál nem.'),

 # 7. óvóhelyek – hol érdeklődj
 (r'Tudd előre, hol a legközelebbi védett hely az otthonod, a munkahelyed és az iskola közelében <span class="verify">a hazai óvóhely-nyilvántartás elérhetősége ellenőrizendő</span>\.',
  'Tudd előre, hol a legközelebbi védett hely az otthonod, a munkahelyed és az iskola közelében. Központi, nyilvános óvóhely-nyilvántartás nincs: az érintett helyeket az önkormányzatnál (polgári védelem) vagy a megyei katasztrófavédelmi igazgatóságnál kell megkérdezni.'),

 # 8. kiberbiztonsági bejelentés – a hivatalos cím
 (r'A csalási kísérleteket jelentsd a nemzeti kiberbiztonsági incidenskezelőnek <span class="verify">a hazai bejelentési cím ellenőrizendő</span>\.',
  'A csalási kísérleteket jelentsd a <strong>Nemzeti Kiberbiztonsági Intézetnek</strong> (Nemzetbiztonsági Szakszolgálat): az <a href="https://incidens.nki.gov.hu" target="_blank" rel="noopener">incidensbejelentő felületen</a> vagy e-mailben (<a href="mailto:csirt@nki.gov.hu">csirt@nki.gov.hu</a>; anonim bejelentés: <a href="mailto:anonim@nki.gov.hu">anonim@nki.gov.hu</a>).'),

 # 9. állatkimenekítés – a szabályozás szervei
 (r'A helyi állatkimenekítési tervről az önkormányzat ad tájékoztatást <span class="verify">hazai szabályozás ellenőrizendő</span>\.',
  'A helyi állatkimenekítési tervről az önkormányzat ad tájékoztatást; a kimenekítés rendjét az állategészségügyi hatóság és a jegyző határozza meg, a nagyüzemi telepeken a telephely belső kimenekítési terve szerint.'),

 # 10. a zárójegyzet
 (r'Az <span class="verify">ellenőrizendő</span> jelölésű adatokat közzététel előtt hivatalos forrásból meg kell erősíteni\.',
  'A magyarországi adatok hivatalos forrásból származnak; ahol nincs nyilvános adat, ott a hatóság megkeresése szükséges – a <a href="#adaptacio">15. fejezet</a> felsorolja, melyik ponthoz kitől kérdezz.'),
]

for i, (minta, uj) in enumerate(CSEREK, 1):
    rx = re.compile(minta)
    if not rx.search(h):
        print(f"✗ {i}. NEM TALÁLHATÓ: {minta[:80]}…")
        sys.exit(1)
    h = rx.sub(lambda _m: uj.replace('\\', '\\\\'), h, count=1)
    print(f"✓ {i}. cserélve")

io.open(F, 'w', encoding='utf-8').write(h)
print(f"\n{len(CSEREK)} szöveg cserélve, {len(before)} → {len(h)} karakter")
