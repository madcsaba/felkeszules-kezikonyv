# Szabványos közmű-kimaradási tájékoztatás – szakpolitikai javaslat

*Tervezet, 2026. november*

**Címzettek:** az energiapolitikáért, a víziközmű-szolgáltatásért és az informatikáért felelős miniszterek; továbbá a Magyar Energetikai és Közmű-szabályozási Hivatal (MEKH) és az Országos Katasztrófavédelmi Főigazgatóság.

**Javaslat:** a kormány rendeletben írja elő, hogy a villamosenergia-elosztók, a víziközmű-szolgáltatók, a földgázelosztók és a távhőszolgáltatók egységes, nyílt, géppel olvasható és hitelesített formában tegyék közzé a tervezett üzemszüneteket és az üzemzavarokat. A formátumot a MEKH adja ki műszaki szabványként, nemzetközi szabványra (CAP) építve.

## Miért most

- **Széttöredezett tájékoztatás.** A négy áramelosztó négyféleképpen értesít: online felületen, postaládás szórólapon, külön kérésre e-mailben, illetve saját mobilappban. A vízműveknél még vegyesebb a kép. Géppel olvasható, nyilvános csatornát egyik áramelosztó sem hirdet; a független aggregátorok a weboldalak lekérdezésével dolgoznak, és maguk is tájékoztató jellegűnek minősítik az adataikat.
- **A jogalap már megvan.** A Kormány tagjainak feladat- és hatásköréről szóló 2026-os rendelet szerint az energiapolitikáért, illetve a víziközmű-szolgáltatásért felelős miniszter az informatikáért felelős miniszterrel egyetértésben dolgozza ki az ágazati infokommunikációs fejlesztési javaslatokat. Ez a javaslat pontosan ilyen.
- **A kötelező értesítés ma is létezik.** Az áramelosztók a 200 kVA alatti felhasználókat 15 nappal a munka előtt kötelesek értesíteni, különben kötbért fizetnek. A javaslat nem új kötelezettséget teremt, hanem a meglévő értesítés formáját egységesíti.
- **Az uniós lakossági riasztórendszer erre épülhet.** Az EU minden tagállamtól megköveteli a mobiltelefonokra küldött, földrajzilag célzott lakossági riasztást; egy egységes közmű-adatforrás ennek is természetes kiegészítője.

## Mit nyernek az állampolgárok

| Helyzet | Ma | A szabvánnyal |
| --- | --- | --- |
| Nincs áram otthon | Ki kell deríteni, melyik elosztóé a terület, és megkeresni a honlapján | A telefon azonnal mutatja: tervezett vagy hiba, mi az oka, mikorra várható a helyreállítás |
| Több ingatlan, idős szülő, nyaraló | Szolgáltatónként és címenként külön regisztráció | Egy alkalmazásban minden mentett hely, minden szolgáltató |
| Nem magyar anyanyelvű lakos, turista | Csak magyar szöveg | A kódolt üzenetet a telefon a saját nyelvén jeleníti meg |
| Vihar, hőhullám, tömeges kimaradás | Túlterhelt hibabejelentő, keresgélés gyenge mobilneten | Kis adatforgalmú, SMS-be is beleférő értesítés; kevesebb fölösleges hívás |
| Önkormányzat, kórház, idősotthon | Kézzel másolt értesítések, Facebook-posztok | Automatikus átvétel a saját rendszerükbe, RSS-ben is |
| Hamis „vízhiány”- vagy „áramszünet”-üzenet | Nehéz megkülönböztetni a valóditól | A digitális aláírás miatt a hamis üzenet nem jelenik meg hivatalosként |

## Javasolt szabályozás

1. **Kormányrendelet** a közzétételi kötelezettségről: kire vonatkozik (minden engedélyes elosztó és víziközmű-szolgáltató), mit kell közzétenni (tervezett üzemszünet, üzemzavar, korlátozás, vízminőségi figyelmeztetés), milyen határidővel (tervezett munka a mostani 15 napos értesítéssel egy időben, üzemzavar a tudomásszerzéstől számított 30 percen belül, a helyreállítás azonnal).
2. **MEKH-rendelet vagy -ajánlás** a műszaki szabványról: adatmezők, kódlisták, terjesztési formák (JSON, RSS/Atom, tömör SMS-forma), aláírás.
3. **Állami tanúsítványlánc**: az állami gyökérkulcs alól minden szolgáltató saját kulcsot kap, amely csak a saját szolgáltatására és ellátási területére érvényes. Kezelése az állami IT-szolgáltatónál vagy a katasztrófavédelemnél.
4. **Országos továbbító** az SMS- és e-mail-értesítésekhez, egy helyen kezelt, visszavonható hozzájárulással; cím és ügyfélazonosító nélkül.
5. **Adatvédelmi garancia a jogszabályban**: a közzétett adat terület, nem személy; az érintettséget a lakos eszköze dönti el.
6. **Nyílt adat**: a közzétett adatok szabadon felhasználhatók (alkalmazásfejlesztők, kutatók, sajtó), az aláírás pedig garantálja a forrást.

## Ütemezés és költség

- **0–6. hónap:** szabványtervezet társadalmi egyeztetése a szolgáltatókkal, a MEKH-hel és a katasztrófavédelemmel; kísérleti üzem egy áramelosztóval és egy vízművel.
- **6–12. hónap:** kötelező közzététel a négy áramelosztónál; a víziközmű-szolgáltatóknál önkéntes, a kisebbeknek közös, egyszerű feltöltőfelület.
- **12–24. hónap:** kötelező a víz-, gáz- és távhőszolgáltatóknak is; az országos továbbító indulása.
- **Költség:** a szolgáltatóknál a meglévő üzemzavar-kezelő rendszerük (amely ma a weboldali térképet táplálja) egy exportfelülettel bővül; a közzététel statikus fájl, külön infrastruktúra nem kell. Állami oldalon a tanúsítványkezelés és a továbbító üzemeltetése. Becsült nagyságrendet a kísérleti üzem adna.

## Nyitott kérdések az egyeztetéshez

- Ki üzemelteti az országos továbbítót és a tanúsítványláncot?
- Lehet-e a Központi Címregiszter azonosítóit településenként nyilvánosan letölthetővé tenni az utcaszintű pontossághoz?
- Hogyan kapcsolódjon a katasztrófavédelem lakossági riasztórendszeréhez (súlyos, tömeges kimaradásnál)?
- Kapjon-e a magyar rendszer egy egységes, könnyen megjegyezhető hibabejelentő számot, mint az Egyesült Királyságban a 105?

---

# Szabványjavaslat (KÖZMŰ-KIMARADÁS K1)

A javaslat a nemzetközi Common Alerting Protocol (CAP 1.2) magyar profilja közmű-kimaradásokra. A teljes műszaki leírás: [`kozmu-ertesites.md`](kozmu-ertesites.md); mintafájlok: [`minta/`](minta/).

## Alapelvek

1. **Terület, nem személy.** A szolgáltató a kimaradás területét teszi közzé; a cím nem hagyja el a lakos telefonját.
2. **A település a közös kulcs** (KSH településazonosító), utcaszinten a Központi Címregiszter azonosítói.
3. **Kódok utaznak, nem szöveg**, így bármely nyelvre lefordítható, és elfér egy SMS-ben.
4. **Minden üzenet aláírt**, és a kulcs csak a kiadó saját szolgáltatására és területére érvényes.
5. **Egy forrás, több kimenet:** JSON alkalmazásoknak, RSS/Atom honlapoknak, tömör forma SMS-hez és QR-kódhoz.

## Adatmezők

| Mező | Tartalom | Példa |
| --- | --- | --- |
| `service` | szolgáltatás | `E` áram, `V` ivóvíz, `G` gáz, `T` távhő, `S` szennyvíz |
| `kind` | típus | `Z` üzemzavar, `T` tervezett, `K` korlátozás, `M` minőségi figyelmeztetés |
| `state` | állapot | `B` bejelentve, `F` folyamatban, `H` helyreállt, `X` visszavonva |
| `cause` | ok | `c1` hálózati hiba, `c2` karbantartás, `c3` csőtörés, `c4` időjárás, `c5` külső kár, `c6` kapacitáshiány, `c9` vizsgálat alatt |
| `area` | érintett terület | településkódok, opcionálisan utcalista vagy sokszög |
| `onset`, `expectedRestore` | időpontok | kezdet, várható helyreállítás |
| `households` | érintett felhasználók száma | 1240 |
| `replacement` | pótlás | lajtos kocsi, szükségkút, aggregátor helye |
| `sig` | digitális aláírás | Ed25519 |

A tömör forma egy sor; aláírással együtt kb. 125 karakter, tehát egy SMS-be belefér:

```
K1|E|Z|F|c4|<KSH-kód>|<kezdet>|<várható vég>|eon_bp|<aláírás>
```

## Nemzetközi példák

| Ország / rendszer | Mit csinál | Mit veszünk át |
| --- | --- | --- |
| **Egyesült Királyság – ENA NEO API** | Az elosztók ágazati szövetsége (ENA) közös API-specifikációt adott ki a kimaradásokra; a UK Power Networks közel valós idejű, tervezett és nem tervezett kimaradásokat ad közre nyílt adatként, API-n | Egy ágazati specifikáció, minden elosztó ugyanazt adja |
| **Egyesült Királyság – 105** | 2016 óta egyetlen ingyenes, háromjegyű szám minden áramelosztóhoz; az elosztók finanszírozzák. Az előzmény: a felmérés szerint az emberek 72%-a nem tudta, kit hívjon áramszünetnél | Egységes belépési pont a lakosnak |
| **CAP (OASIS, ITU-T X.1303)** | Nemzetközi riasztási szabvány; az USA (IPAWS), Kanada (CAP-CP), Ausztrália (CAP-AU-STD) és más országok saját profilt készítettek belőle | Adatmodell, saját magyar profil |
| **MeteoAlarm (Európa)** | 36 európai meteorológiai szolgálat közös figyelmeztető rendszere, CAP-hírcsatornákkal | CAP + hírcsatorna (RSS/Atom) együtt |
| **EU-Alert (EECC 110. cikk)** | Minden uniós tagállamnak 2022 júniusáig kellett lakossági riasztórendszert működtetnie mobiltelefonokra | Súlyos kimaradásnál beköthető a riasztórendszerbe |
| **USA – kereskedelmi aggregátorok** | Magáncégek több száz amerikai, kanadai és brit szolgáltató adatait egységesítik egy API-ba, 10 percenkénti frissítéssel | Bizonyíték az igényre; szabvány nélkül a piac fizetős közvetítőkkel tölti ki a hiányt |

A tanulság: ahol nincs közös szabvány, ott magáncégek gyűjtik össze az adatot, fizetős szolgáltatásként. Ahol van (Egyesült Királyság), ott az elosztók maguk adják nyíltan, egy formában. Magyarországon négy áramelosztó van, így a megegyezés gyorsan elérhető.

## Források

**Hazai helyzet**

- [MVM: Tervezett áramszünetek listája (Démász)](https://www.mvmnext.hu/aram/pages/online/aramszunet.jsf)
- [MVM Émász: Tervezett áramszünetek és e-mailes értesítés](https://mvmemaszhalozat.hu/ugyfeleinknek/hasznos-informaciok/tervezett-aramszunetek)
- [Szeged a mindenem: Változik az értesítés módja az MVM Démász területén](https://www.szegedamindenem.hu/belfold/valtozik-a-tervezett-aramszunetekrol-szolo-ertesites-modja-az-mvm-demasz-teruleten/)
- [OPUS ENERGETIKA Áramapp (App Store)](https://apps.apple.com/hu/app/opus-energetika-%C3%A1ramapp/id6477295912)
- [Index: Tervezett áramszünet – E.ON tájékoztatás](https://index.hu/bcs/2026/11/16/miert-van-tervezett-aramszunet-eon)
- [E.ON: Garantált szolgáltatások (15 napos értesítés)](https://eon.hu/content/dam/eon/eon-hungary/documents/hatarozatok-szabalyzatok-aram/garantalt-szolgaltatasok/2018_garant%C3%A1lt_szolg%C3%A1ltat%C3%A1sok.pdf)
- [Fővárosi Vízművek: Munkatérkép](https://www.vizmuvek.hu/hu/kezdolap/informaciok/munkaterkep-hol-dolgozunk)
- [DMRV: Hírek (RSS)](https://www.dmrvzrt.hu/hu/hirek)
- [tervezettaramszunet.hu (független aggregátor)](https://tervezettaramszunet.hu/)
- [Magyar Közlöny 2026/46: a Kormány tagjainak feladat- és hatásköre](https://magyarkozlony.bsdnet.hu/kozlony/7)

**Nemzetközi példák**

- [UK Power Networks: National Energy Outage API](https://ukpowernetworks.opendatasoft.com/explore/assets/ukpn-national-energy-outage/)
- [Western Power: 105 is now live](https://www.westernpower.co.uk/news-and-events/latest-news/105-is-now-live)
- [Networks: National 105 power cut number launched](https://networks.online/power/national-105-power-cut-number-launched)
- [Wikipedia: Common Alerting Protocol](https://en.wikipedia.org/wiki/Common_Alerting_Protocol)
- [WMO: CAP és cell broadcast, MeteoAlarm](https://wmo.int/media/magazine-article/leveraging-common-alerting-protocol-and-cell-broadcast-technology-advancing-early-warnings-all)
- [Interoperable Europe: EECC 110. cikk](https://interoperable-europe.ec.europa.eu/node/704086)
- [PowerOutage.us: aggregált kimaradási API](https://poweroutage.us/use-our-data)
