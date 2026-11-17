# Miért nincs áram? Miért nincs víz?

Civil kezdeményezés a szabványos közmű-kimaradási tájékoztatásért: **szakpolitikai javaslat**, **működő demó alkalmazás** és **petíció** egy oldalon.

## Tartalom

| Fájl | Mi ez |
|---|---|
| `index.html` | a kampányoldal: probléma, megoldás, előnyök, demó, javaslat, nemzetközi példák, petíció |
| `app/` | a demó alkalmazás (mintaadatokkal, 4 nyelven, offline is működik) |
| `docs/szakpolitikai-javaslat.md` | a teljes javaslat és szabványjavaslat |
| `docs/peticio-szolgaltatok.md` | a petíció szövege |
| `docs/kozmu-ertesites.md` | a műszaki szabványleírás |
| `docs/minta/` | mintafájlok: JSON, RSS, tömör SMS-forma (kitalált adatokkal) |
| `sw.js` | offline működés |

## A petíciós link beillesztése

Az `index.html` alján, a `<script>` elején:

```js
var PETITION_URL = "";
```

Írd az idézőjelek közé az aláírási felület linkjét (például a szabad.ahang.hu petíciódét). Mentés után az „Aláírom a petíciót” gomb aktív lesz.

## Közzététel GitHub Pages-en

Settings → Pages → Deploy from a branch → `main` (vagy amelyik ágon van) → `/ (root)`.

## Kapcsolódó

A demó alkalmazás a [Felkészülés vészhelyzetekre](https://github.com/madcsaba/felkeszules-kezikonyv) kézikönyv része.

*Nem hivatalos kormányzati vagy szolgáltatói oldal. A demóban minden kimaradás kitalált.*
