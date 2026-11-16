# Közmű-kimaradási értesítés – javasolt szabvány

Tervezet, 2026. november. Célja, hogy az áram-, víz-, gáz- és távhőszolgáltatók **egyféle, géppel olvasható, aláírt** formában közöljék a kimaradásokat, és a lakos telefonja a **saját helyeire** szűrve, **a saját nyelvén** mutassa meg, miért nincs áram vagy víz.

## 1. Alapelvek

1. **A cím nem hagyja el a telefont.** A szolgáltató a kimaradás *területét* teszi közzé, a telefon helyben dönti el, hogy a mentett helyek érintettek-e.
2. **A település a közös kulcs.** A víziközmű-törvény az ellátási területet településekben határozza meg, az áramhálózati elosztók is településenként dolgoznak. Azonosító: a KSH településazonosító törzsszám. Utcaszintű pontosításhoz a Központi Címregiszter (KCR) azonosítói.
3. **Kódok utaznak, nem szöveg.** Szolgáltatás, típus, ok: rögzített kódlista. A szöveget a telefon állítja össze bármelyik nyelven, ezért elfér SMS-ben és QR-kódban is.
4. **Minden üzenet aláírt, és a szolgáltató csak a saját területére és szolgáltatására írhat.** Ezt a telefon ellenőrzi az állami tanúsítványlánc alapján (lásd az architektúra Whiteboardot).
5. **CAP 1.2-kompatibilis.** A teljes forma a nemzetközi Common Alerting Protocol profilja, így katasztrófavédelmi rendszerekbe is beköthető.

## 2. Kódlisták

| Mező | Kódok |
|---|---|
| Szolgáltatás | `E` áram · `V` ivóvíz · `G` gáz · `T` távhő · `S` szennyvíz |
| Típus | `Z` üzemzavar · `T` tervezett munka · `K` korlátozás (pl. vízkorlátozás) · `M` minőségi figyelmeztetés (pl. vízforralás) |
| Állapot | `B` bejelentve · `F` folyamatban · `H` helyreállt · `X` visszavonva |
| Ok | `c1` hálózati hiba · `c2` karbantartás · `c3` csőtörés · `c4` időjárás · `c5` harmadik fél okozta kár · `c6` kapacitáshiány · `c9` vizsgálat alatt |

## 3. Teljes forma (alkalmazásoknak, weboldalaknak)

JSON, a CAP 1.2 mezőinek megfelelő nevekkel. A szolgáltató statikus fájlként teszi közzé (lásd 5. pont).

```json
{
  "v": "K1",
  "id": "eon_bp-2026-11-16-0042",
  "issuer": "eon_bp",
  "sent": "2026-11-16T10:40:00+01:00",
  "status": "Actual",
  "msgType": "Update",
  "service": "E",
  "kind": "Z",
  "state": "F",
  "cause": "c4",
  "onset": "2026-11-16T10:12:00+01:00",
  "expectedRestore": "2026-11-16T13:30:00+01:00",
  "area": {
    "settlements": ["<KSH-kód>"],
    "streets": ["KCR:…", "KCR:…"],
    "polygon": null
  },
  "households": 1240,
  "replacement": { "kind": "aggregátor", "where": "…" },
  "infoUrl": "https://…",
  "faultPhone": "…",
  "note": { "hu": "Szabad szöveg, opcionális" },
  "sig": "ed25519:…"
}
```

- Az `area` legalább egy települést tartalmaz. Az utcalista és a sokszög opcionális; ha van, a telefon pontosabban szűr.
- Frissítésnél ugyanaz az `id`, új `sent` és `state`. A helyreállítás külön üzenet (`state: "H"`), így a telefon le tudja zárni a kimaradást.
- `note`: szabad szöveg, csak kiegészítés. A lényeg mindig a kódokban van.
- A `replacement` vízhiánynál a lajtos kocsi vagy szükségkút helye, áramszünetnél az aggregátor.

## 4. Tömör forma (SMS, QR, Bluetooth, gyenge hálózat)

Egy sor, `|` jellel tagolva, a végén aláírással:

```
K1|E|Z|F|c4|<KSH-kód>|<kezdet>|<várható vég>|eon_bp|<aláírás>
```

- Az időpontok percben, 36-os számrendszerben (5 karakter).
- Az aláírás 64 bájtos Ed25519, base64-ben 86 karakter.
- Aláírás nélkül kb. 40 bájt, aláírással kb. 130 karakter, tehát **egy SMS-be belefér**.
- Utcalista nem fér bele, ezért a tömör forma településszintű. Utcaszintű pontosítás a teljes formában jön, ha van net.

## 5. Terjesztés

| Csatorna | Ki küldi | Mit tud a lakosról | Megjegyzés |
|---|---|---|---|
| **Statikus fájl** | szolgáltató | semmit | `…/kozmu/{szolgáltató}/{település}.json`. A telefon csak a saját helyei településeit kéri le, ETag-gel (változatlannál pár száz bájt). |
| **Push** | országos továbbító | semmit | Témára iratkozás: `kozmu.{település}.{szolgáltatás}`. Személyes adat nélkül. |
| **SMS** | országos továbbító | telefonszám + települések | Csak ha a lakos kéri (kettős megerősítés). Cím nincs. |
| **E-mail** | országos továbbító | e-mail-cím + települések | Mint az SMS. |
| **Továbbadás** | lakos | semmit | QR vagy Bluetooth a tömör formával, aláírás miatt hamisíthatatlan. |

Az SMS- és e-mail-feliratkozást **egy helyen**, az országos továbbítónál kell kezelni, nem szolgáltatónként. Így a lakos egyszer adja meg az elérhetőségét, akárhány helye és szolgáltatója van, és egy helyen tudja visszavonni.

A szolgáltatók meglévő, ingatlanhoz kötött értesítései (például az E.ON online ügyfélszolgálatán beállítható SMS és e-mail) megmaradnak. Ez a szabvány nem kiváltja őket, hanem egységes, nyelvfüggetlen csatornát ad melléjük.

## 5/a. RSS/Atom kimenet

A szolgáltatói JSON-ból a build gépi úton településenkénti RSS/Atom csatornát is előállít:

```
…/kozmu/{szolgáltató}/{település}.rss
```

- Egy tétel = egy esemény aktuális állapota; a `guid` az esemény `id`-je, frissítésnél a `pubDate` változik, a helyreállítás (`state: H`) külön tétellel zárja le.
- A cím és a leírás a kódokból előállított, ember által olvasható szöveg (alapból magyarul), a `link` a teljes JSON-ra mutat.
- Célja a kompatibilitás: RSS-olvasók, önkormányzati honlapok és hírportálok ezt veszik át, az app a strukturált, aláírt JSON-t használja. Az RSS-ben aláírás nincs, ezért hivatalos forrásként csak a szolgáltató saját domainjéről érvényes.
- Előkép a gyakorlatból: a DMRV hírcsatornája (dmrvzrt.hu/hu/rss/hirek) már ma RSS-ben közli a vízhiányokat, de szűretlenül, vegyes hírek között — a településenkénti bontás és a kódolt tartalom ezt teszi géppel feldolgozhatóvá.

## 5/b. A mai helyzet (2026. november, felmérés)

| Szolgáltató | Fő csatorna | Értesítés | Géppel olvasható |
|---|---|---|---|
| E.ON | térképes kereső (eon.hu) | online felület, digitális csatornák | nincs |
| MVM Démász | térkép (mvmhalozat.hu) | 2026 augusztusától postaládás szórólap, lépcsőházi hirdetmény | nincs |
| MVM Émász | térkép (mvmemaszhalozat.hu) | e-mail, e-mailben igényelve (vevőazonosító + mérésipont-azonosító kell) | nincs |
| Opus Titász | áramszünet-kereső (opustitasz.hu) | saját mobilapp push értesítéssel | nincs |
| Fővárosi Vízművek | munkatérkép (vizmuvek.hu) | honlap, 3 nappal előre; mobilapp | nincs |
| DMRV | hírek + RSS | – | részben (RSS, szűretlen) |

Mind a négy áramelosztó másképp értesít, és egyiknél sincs meghirdetett API vagy RSS; a független tervezettaramszunet.hu aggregátor csak a felületek lekérdezésével dolgozik, és maga is tájékoztató jellegűnek minősíti az adatait. Ez a szabvány ezt a hiányt tölti be.

## 6. Helyek a telefonon

- A lakos tetszőleges számú helyet ment (otthon, nyaraló, szülők lakása, úti cél), mindegyikhez egy települést és opcionálisan egy KCR-címazonosítót.
- Helyenként tárolja a szolgáltatókat (áram, víz, gáz, távhő). Az app a település alapján javasol, a lakos a számlája alapján ellenőrzi.
- Az „Itt vagyok most” hely határozza meg a Most képernyő riasztásait; a kimaradás-értesítések minden mentett helyre megjelennek.
- Utazáskor az app a GPS-t **csak helyben** használja a település megállapítására, és csak engedéllyel.

## 7. Adatvédelem (GDPR)

- Push és statikus fájl: személyes adat nem keletkezik.
- SMS/e-mail: adatkezelő az országos továbbító. Cél: kimaradás-értesítés. Tárolt adat: elérhetőség és településkódok. Jogalap: hozzájárulás, bármikor visszavonható, a törlés azonnali.
- Cím, KCR-azonosító és a szolgáltatói ügyfélszám soha nem kerül a továbbítóhoz.

## 8. Szolgáltatói bevezetés

1. A szolgáltató tanúsítványt kap a gyökérkulcs alól: `service` = saját szolgáltatása, `regions` = ellátott települések listája.
2. A meglévő üzemzavar-kezelő rendszeréből (amely ma a weboldali térképet táplálja) exportál a 3. pont szerinti JSON-ba.
3. Az aláírt fájlt a saját webhelyén teszi közzé, és a push-továbbítónak is elküldi.
4. Tesztüzem `status: "Exercise"` értékkel, amit a telefon nem jelenít meg riasztásként.

## 9. Nyitott kérdések

- Ki üzemelteti az országos továbbítót (katasztrófavédelem, MEKH vagy állami IT-szolgáltató)?
- Kötelező legyen-e a szolgáltatóknak (MEKH-előírás), vagy önkéntes?
- A KCR-azonosítók nyilvánosan letölthetők-e a telefonra településenként?
- A kisebb víziközmű-szolgáltatóknak kell-e közös, egyszerű feltöltő felület?
