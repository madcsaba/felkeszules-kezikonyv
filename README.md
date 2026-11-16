# Felkészülés vészhelyzetekre – weboldal

Statikus, függőség nélküli weboldal (HTML + CSS + JS) a „Felkészülés vészhelyzetekre – családi és közösségi kézikönyv” szövegéből.

## Fájlok

- `index.html` – a teljes kézikönyv, fejezetenként (`#viz`, `#elelmiszer`, … horgonyokkal)
- `style.css` – megjelenés: világos/sötét téma, mobilnézet, nyomtatási (PDF) nézet
- `script.js` – tartalomjegyzék-kiemelés, mobilmenü, kipipálható listák (csak a böngészőben tárolva), 10 pontos teszt pontozása
- `.nojekyll` – a GitHub Pages ne futtassa a Jekyllt

## Közzététel GitHub Pages-en

A repó **Settings → Pages → Build and deployment** beállításai:

- Source: **Deploy from a branch**
- Branch: **main**, mappa: **/ (root)** → Save

Pár perc múlva elérhető: `https://madcsaba.github.io/felkeszules-kezikonyv/`

## Helyi megtekintés

```bash
python3 -m http.server -d . 8000
```

## Szerkesztés

A szöveg közvetlenül az `index.html`-ben van. A **15. fejezet** két dolgot tartalmazza:

- a magyarországi hivatalos források listáját (a „Hivatalos magyar források" blokk);
- a **„Közzététel előtt a hazai hatóságoktól pontosítandó"** kipipálható listát: minden
  pontnál meg van adva, **kitől és hol** kérdezhetsz. Egy pont akkor zárható, ha a válasz
  megvan – a kipipálás a böngészőben tárolódik.

A korábbi `<span class="verify">ellenőrizendő</span>` jelölés megszűnt: ahol lehetett,
hivatalos forrásból pontosítottunk, ahol nem, ott a hatóság megkeresése a megoldás.

## Forrás

Az eredeti fájlok a `madcsaba/kh` repó `claude/confident-cray-gd9rcq` ágának `docs/` mappájában készültek.
