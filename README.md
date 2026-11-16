# Felkészülés vészhelyzetekre – weboldal

Statikus, függőség nélküli weboldal (HTML + CSS + JS) a „Felkészülés vészhelyzetekre – családi és közösségi kézikönyv” szövegéből.

## Fájlok

- `index.html` – a teljes kézikönyv, fejezetenként (`#viz`, `#elelmiszer`, … horgonyokkal)
- `style.css` – megjelenés: világos/sötét téma, mobilnézet, nyomtatási (PDF) nézet
- `script.js` – tartalomjegyzék-kiemelés, mobilmenü, kipipálható listák (csak a böngészőben tárolva), 10 pontos teszt pontozása
- `app/` – mobilalkalmazás (PWA): 5 képernyő, 4 nyelv (hu, en, uk, de), telepíthető a kezdőképernyőre
- `sw.js` – service worker: az app és a kézikönyv internet nélkül is megnyílik
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

A szöveg közvetlenül az `index.html`-ben van. Az ellenőrizendő adatokat a `<span class="verify">ellenőrizendő</span>` jelöli – ezeket közzététel előtt érdemes hivatalos forrásból pontosítani.

## Forrás

Az eredeti fájlok a `madcsaba/kh` repó `claude/confident-cray-gd9rcq` ágának `docs/` mappájában készültek.

## Mobilalkalmazás (`app/`)

Elérhető: `https://madcsaba.github.io/felkeszules-kezikonyv/app/`

- **Most** – vészhelyzeti teendők nagy gombokkal, 112-es hívógomb, aktív riasztások
- **Felkészülés** – vízkalkulátor, kipipálható listák
- **Helyben** – terület választása, segélyhívók, helyi adatok
- **Tervem** – családi terv (csak a telefonon tárolódik)
- **Frissítések** – letöltött csomagok kiadóval és hatókörrel, rövid üzenet próbája

Telepítés: a böngésző menüjében *Hozzáadás a kezdőképernyőhöz*. Első megnyitás után internet nélkül is működik.

Az adatok három külön sávban vannak (tanácsok, helyi adatok, riasztások), mindegyiknek saját kiadója és hatóköre van. A helyi adatok egyelőre **mintaadatok**; a digitális aláírás ellenőrzése még nincs bekötve. Az ukrán és a német fordítás anyanyelvi lektorálásra vár.
