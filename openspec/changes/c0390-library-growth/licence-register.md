# Licence register of import candidates (task 8)

Entry 2026-11-04. Each verdict rests on the LICENSE file and README text read at the pinned commit (GitHub API
and raw files, read only); nothing was imported in M1. ACCEPT means POLICY.md and `licences.toml` accept the
licence as it stands; UNCLEAR sources stay out until the maintainer decides; REFUSE sources are never read for
items. Share-alike sources go into their own licence family folder (`*/cc-by-sa-4.0/<Namespace>/`), never
mixed with CC0 items.

| source | pinned HEAD | licence as read | share-alike | approx. items | verdict |
|---|---|---|---|---|---|
| LibrePCB-Libraries, 48 `*.lplib` repositories | per repository; LibrePCB_Base `dc037a238eb5efcc034dd9d62e5775d5c21e90e4` (D-0005 pins `662a148d…`) | CC0-1.0, identical LICENSE.txt in all 48 | no | 763 symbols, 1470 packages, 1402 components, 1866 devices | ACCEPT; 1346 STEP files excluded (vendor-derived 3D undecided) |
| sparkfun/SparkFun-Eagle-Libraries | `2354daeed58cd6bcfcb97f2669765dce8ef2aaf0` | CC-BY-SA-4.0 in README and per-`.lbr` descriptions, no LICENSE file | yes | 1961 packages, 1144 symbols | ACCEPT after excluding one Ultra Librarian and one SnapEDA derived device set and the retired CC-BY-SA-3.0 logo items |
| Seeed-Studio/OPL_Kicad_Library | `b0035c51eb0348bb3e165fdb2f2765fa3d1d17bd` | CC-BY-SA-4.0 | yes | ~416 symbols, ~193 footprints | ACCEPT; EasyEDA-format files, boards and 3D excluded |
| hlord2000/nordic-lib-kicad | `05a4dae2427fde6be0e190d6c9169eae1b3dae51` | CERN-OHL-P-2.0 | no | ~60 symbols, 29 footprints | ACCEPT; 29 STEP excluded |
| sparkfun/SparkFun-KiCad-Libraries | `ff1d7db03ac0d7e084147b5361e0cf5aeb1f6c40` | CC-BY-4.0 in README and PCM metadata only | no | ~2270 symbols, 628 footprints | UNCLEAR: mixes copies of KiCad stock parts; needs a per-item filter |
| Digi-Key/digikey-kicad-library | `d4bd68f42e6ccc474526811a853a03692e170b58` | CC-BY-SA-4.0 WITH KiCad-libraries-exception | yes | 1073 symbols, 464 footprints | UNCLEAR: needs the alias decision below |
| Digi-Key/digikey-partner-kicad-library | `b0bdcd1e0d2b817815c2bbf6fb656673b258bbe7` | same as Digi-Key | yes | small | UNCLEAR: same decision |
| espressif/kicad-libraries | `dd76561812ab300351234ba6e0ec1295641796f0` | same as Digi-Key | yes | 49 symbols, 54 footprints | UNCLEAR: same decision; vendor 3D excluded |
| horizon-eda/horizon-pool | `0696685973dee6c9d7202704d23510768e212744` | same as Digi-Key | yes | 316 symbols, 311 packages | UNCLEAR: same decision; its 3D models are KiCad's and are refused |
| Alarm-Siren/arduino-kicad-library | `1075811e04a7a0ec7645a3590f179655e027c650` | CC-BY-SA-4.0 plus a reworded, non-SPDX exception; NC images | yes | 61 symbols, 35 footprints | UNCLEAR |
| OLIMEX/KiCAD | `1cc7f5763b512e7db429c178da666bc409bb873f` | Apache-2.0 | no | 3399 footprints | UNCLEAR: its README says most items copy KiCad stock parts |
| adafruit/Adafruit-Eagle-Library | `4abf84c3856535c0ab6ae96ec4be784d7dcc6b3e` | none found | n/a | 643 packages | REFUSE (no licence); the CC0 `LibrePCB-Libraries/Adafruit.lplib` is the usable route |
| ContextualElectronics/CE_KiCadLib | `b8095f49be8a718afaaf7686f2ded06dcbceb069` | none found | n/a | small | REFUSE (no licence) |
| WurthElektronik/KiCad-Library | `215595ffc7c98649394598bc6bac81ddc421fcc6` | custom terms (PDF) | n/a | large | REFUSE (custom licence) |
| kicad-library-tools (kicad-footprint-generator) | `090252c1f2429ceb8bd8ef2aa466b6c135f6273a` | GPL-3.0-or-later code | n/a | generator | REFUSE as an item source: its output is KiCad's official footprint set |

Never read for items whatever their terms: KiCad's official libraries, SnapEDA, Ultra Librarian, SamacSys /
Component Search Engine, EasyEDA / LCSC / OSHWLab, vendor 3D models.

## Decision for the maintainer

Four candidates (Digi-Key, Digi-Key Partner, Espressif, Horizon) carry the exact SPDX exception, so their
expression is `CC-BY-SA-4.0 WITH KiCad-libraries-exception`. The exception only adds permission for designs
that use the parts; redistribution of the library itself stays plain CC-BY-SA-4.0. `licences.toml` handles
`WITH` expressions through `[aliases]`; adding `"CC-BY-SA-4.0 WITH KiCad-libraries-exception" = "CC-BY-SA-4.0"`
would make them ACCEPT. This change does not add the alias: it is a licence policy decision.
