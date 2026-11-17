# Mintafájlok – KÖZMŰ-KIMARADÁS K1

**DEMÓ: minden adat kitalált.** A fájlok azt mutatják meg, mit kellene egy szolgáltatónak közzétennie a `docs/kozmu-ertesites.md` szerinti szabvány alapján.

| Fájl | Kinek szól |
|---|---|
| `kozmu/eon_bp/budapest.json` | alkalmazásoknak: a teljes, strukturált forma (egy település, több esemény) |
| `kozmu/eon_bp/budapest.rss` | honlapoknak, RSS-olvasóknak: ugyanaz emberi nyelven |
| `kozmu/fv/budapest.json` | egy vízmű ugyanebben a formában |
| `tomor.txt` | SMS, QR-kód, Bluetooth: egysoros, tömör forma |
| `kozmu/index.json` | a szolgáltatók jegyzéke: ki, milyen szolgáltatásért, mely településekért felel |

A `sig` mezők helyőrzők (`DEMO…`): éles rendszerben Ed25519 aláírás áll ott, amelyet a telefon az állami tanúsítványlánc alapján ellenőriz.
