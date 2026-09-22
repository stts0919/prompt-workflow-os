# Term Glossary — `en-GB` (English — United Kingdom)

> Source-of-truth file for the `en-GB` term glossary. Lives under
> `shared/locales/en-GB/` per the architecture in
> [`../README.md`](../README.md).

Context-sensitive guidance, not blind replacement. Use to pick the UK
form when the audience is British. User preference, brand names,
industry vocabulary always override defaults.

10 categories, ~50 entries. Smaller than `zh-TW` / `zh-CN` because the
glossary focuses on UK / US spelling flips and UK-specific idioms.

## How to use this glossary

1. Detect the audience. If the user named United Kingdom or used UK
   conventions, use this glossary.
2. Apply the substitution only to unprotected prose (see writing rules D).

## Limits

- This glossary does **not** translate brand names.
- This glossary does **not** translate workflow IDs or code identifiers.
- This glossary is a starting point, not exhaustive.

---

## 1. Spelling — UK vs US

Default UK spellings.

| UK (default) | US | Notes |
| --- | --- | --- |
| organisation | organization | -ise / -yse: realise, analyse |
| colour | color | -our: behaviour, favour, honour |
| centre | center | -re: theatre, fibre, litre |
| metre | meter | -re |
| modelled | modeled | double consonant for verbs ending in stressed -l |
| travelled | traveled | same pattern |
| cancelled | canceled | same pattern |
| defence | defense | -ce |
| licence (n.) / license (v.) | license | UK requires noun / verb distinction |
| grey | gray | -ey vs -ay |
| mum | mom | |
| biscuit (food) | cookie | UK biscuit = US cookie |
| flat | apartment | |
| lift | elevator | |
| petrol | gasoline | |
| lorry | truck | |
| chips | fries | |
| football | soccer | UK football = soccer |
| autumn | fall | |
| got | gotten | past participle |
| dialogue | dialog | -gue |
| catalogue | catalog | -ue |
| programme (n.) | program | -mme for noun sense |
| sceptic | skeptic | -sc- |
| pyjamas | pajamas | |
| manoeuvre | maneuver | -oeu- |
| moustache | mustache | |

## 2. Date / number / currency

| UK (default) | US / International | Notes |
| --- | --- | --- |
| DD/MM/YYYY | MM/DD/YYYY | UK: 22/09/2026 = 22 Sep |
| YYYY-MM-DD | same | ISO; use in technical docs |
| £100 (no space) | $100 | UK currency symbol |
| £1,000.50 | $1,000.50 | comma thousand, period decimal |
| 1.5 | 1.5 | period decimal |
| 020 7946 0958 | (555) 123-4567 | UK phone formats |
| SW1A 1AA | 12345 | UK postcode |

## 3. Common abbreviations

| UK (default) | US / International | Notes |
| --- | --- | --- |
| Mr | Mr. | UK often no period |
| Mrs | Mrs. | UK often no period |
| Ms | Ms. | UK often no period |
| Dr | Dr. | UK often no period |
| Prof | Prof. | UK often no period |
| St (Street) | St. | UK often no period |
| Ave | Ave. | UK often no period |
| Co | Co. | UK often no period |
| Ltd | Ltd. | UK often no period |
| PLC | Inc. | UK public limited company |
| LLP | LLC | UK limited liability partnership |

## 4. Idioms — UK

Use only in casual / conversational contexts.

| UK idiom | Meaning |
| --- | --- |
| whilst | while (formal) |
| amongst | among (formal) |
| fortnight | two weeks |
| at the end of the day | ultimately |
| brilliant | great (positive) |
| bespoke | custom-made |
| knack | skill at doing something |
| dodgy | suspicious / unreliable |
| gutted | very disappointed |
| chuffed | very pleased |

## 5. Business / workplace

| UK (default) | US / International | Notes |
| --- | --- | --- |
| annual leave | PTO / vacation | UK paid leave |
| workplace pension | 401(k) | UK retirement plan |
| share scheme | RSU | UK equity compensation |
| OOO | OOO | out of office |
| FY26 / FY 2026-27 | FY2026 | UK fiscal year |
| CV | resume | UK |
| P45 | W-2 | UK leaving document |
| NI number | SSN | UK national insurance |

## 6. Government and political

| UK (default) | Notes |
| --- | --- |
| PM | Prime Minister |
| HM | Her Majesty's (HM Government, HM Treasury) |
| Chancellor | Chancellor of the Exchequer (finance minister) |
| NHS | National Health Service |
| Parliament | legislative body |
| House of Commons / House of Lords | chambers |
| Whitehall | UK government (informal) |
| Downing Street | PM's office (informal) |
| Brexit | UK leaving the EU |

## 7. Education

| UK (default) | US | Notes |
| --- | --- | --- |
| GCSE | — | UK secondary school exam |
| A-level | — | UK pre-university exam |
| university | university | UK = both 2-year and 4-year |
| degree | degree | UK 3-year undergrad standard |
| Master's | Master's | UK postgraduate |
| PhD / DPhil | PhD | UK PhD; Oxford uses DPhil historically |
| UCAS | Common App | UK university application |

## 8. Time and date expressions

| UK (default) | US / International |
| --- | --- |
| 22/09/2026 (22 Sep) | 09/22/2026 (Sep 22) |
| 14:30 | 2:30 PM |
| autumn | Fall |
| Bank Holiday | federal holiday |
| half term | spring / fall break |

## 9. Casual register

| Casual | Formal |
| --- | --- |
| gonna | going to |
| wanna | want to |
| kinda | somewhat |
| yeah | yes |
| cheers | thank you |
| mate | friend |
| innit | isn't it |
| bloomin' | (euphemism, mild emphasis) |
| bloody | (mild expletive) |

(Casual register used in B2C / Twitter / casual email; formal in
legal / academic / official communications.)

## 10. Common cross-Atlantic differences (compact)

| Concept | UK | US |
| --- | --- | --- |
| parking lot | car park | parking lot |
| sidewalk | pavement | sidewalk |
| elevator | lift | elevator |
| apartment | flat | apartment |
| gasoline | petrol | gasoline |
| truck | lorry | truck |
| fries | chips | fries |
| cookie (food) | biscuit | cookie |
| soccer | football | soccer |
| fall (season) | autumn | fall |
| cookie (web) | cookie | cookie |

---

## How to extend

When adding a term:

1. Verify the UK form by consulting at least one UK-published
   reference (Oxford English Dictionary, The Economist Style Guide,
   UK government style guides).
2. Add the US form for cross-reference.
3. Keep brand names in their official form.
4. Update both `shared/locales/en-GB/TERM_GLOSSARY.md` and the
   canonical map.