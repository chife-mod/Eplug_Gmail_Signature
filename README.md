# EPlug Email Signatures

HTML-подписи для Gmail — проект подписей для группы компаний Eplug / Energy Plus.
Каждая подпись — карточка на дашборде (`index.html`); внутри — превью версий и инструкция установки.

## Структура

| Файл | Описание |
|---|---|
| `index.html` | **Дашборд-лаунчер** — карточки всех подписей группы (темплейт project-dashboard). |
| `signature-1/` | Превью Signature 1 (Michael Elhav): текущая V3, история V1–V2, инструкция. |
| `signature-2/` | Превью Signature 2 (Moshe Lefkowitz, President · Energy Plus): оба варианта + open items. |
| `signature-2-v4.html` | **Signature 2 / Moshe Lefkowitz, актуальный (2026-07)** — макет из Figma `Email-Signatures-All` node `1:2282` (600×488): Energy Plus, настоящие бейджи наград, промо-карточка VUE. Пиксель-дифф с Figma — 98.3%. Ранние драфты (A/B с плейсхолдерами) удалены — есть в git-истории до `8c1baac`. |
| `signature-2-matthew.html` | **Signature 2 / Matthew Polaniecki (COO/CTO)** — то же семейство, адаптация: имя длиннее (колонка 222px + зазор 3px, правый блок на том же месте), титул в две строки, один телефон. Правый блок и VUE-карточка побитово совпадают со сборкой Moshe. |
| `scripts/build-assets.py` | Нарезка @2x-ассетов из мастер-экспорта Figma @4x. |
| `scripts/qa-diff.sh` + `.py` | Рендер в headless Chrome @2x и пиксель-дифф с эталоном Figma. |
| `qa/` | Эталон Figma и результаты диффа (карта расхождений, side-by-side). |
| `shared/` | Токены, компоненты и чипса-навигатор превью (из темплейта). |
| `signature-v3.html` | **Signature 1, актуальный (2026-07)** — светлый макет из Figma `4869:509`: имя/контакты слева, логотипы Eplug + Energy Plus справа за разделителем. |
| `signature-v2.html` | Signature 1, V2 — розово-зелёный макет с двумя лого-блоками. |
| `signature.html` | Signature 1, V1 — подпись-картинка, пиксель-перфект из Figma. |
| `signature-live.html` | Signature 1, V1 альтернативный — живой HTML с копируемым текстом. |
| `public/assets/images/` | PNG-ассеты из Figma (V1/V2 @2x, V3 @4x). |

Новая подпись = папка `signature-N/` + карточка на дашборде + raw-файлы `signature-N-*.html`.

## Установка в Gmail

1. Откройте `signature-v3.html` в Chrome
2. `Cmd+A` (выделить всё) → `Cmd+C` (копировать)
3. Gmail → ⚙️ → **See all settings** → **General** → **Signature**
4. `Cmd+V` (вставить)
5. **Save Changes**

## Пересборка и проверка

```bash
python3 scripts/build-assets.py                                            # ассеты из мастер-кадра Figma
./scripts/qa-diff.sh signature-2-v4.html qa/ref/figma-1-2282@2x.png 600 488  # пиксель-дифф
```

Методика и свод правил вёрстки писем — в шаблоне студии
`oz/mod-manager/templates/email-signature/` (`BEST-PRACTICES.md`).

## Хостинг изображений

Подпись использует GitHub Pages для хостинга картинок:
```
https://chife-mod.github.io/Eplug_Gmail_Signature/public/assets/images/...
```

> **Картинка обязана быть закоммичена, иначе у получателя будет битая иконка.**
> Локальное превью этого не покажет — файл лежит на диске, но на GH Pages его нет.
> Так в 2026-07 сломались иконки в драфтах Signature 2: файлы лежали локально, но не были закоммичены.
> Проверка:
> ```bash
> for f in public/assets/images/**/*.{png,jpg}; do
>   printf "%-40s remote=%s git=%s\n" "$f" \
>     "$(curl -s -o /dev/null -w '%{http_code}' "https://chife-mod.github.io/Eplug_Gmail_Signature/$f")" \
>     "$(git ls-files --error-unmatch "$f" >/dev/null 2>&1 && echo tracked || echo UNTRACKED)"
> done
> ```

Для активации GitHub Pages:
1. GitHub → Settings → Pages
2. Source: **Deploy from a branch**
3. Branch: `main` / `root`
4. Save

## Figma

- **V3**: [Eplug-Design](https://www.figma.com/design/GXUObJIRiX2EfkOujCyNIq/Eplug-Design?node-id=4869-509) — node `4869:509` (Michael Elhav)
- **V2**: Eplug-Design, node `4700:912`
- **V1**: [Eplug-Web](https://www.figma.com/design/NsarAMa9SQMVyRCQDvgqg3/Eplug-Web?node-id=296-197) — node `296:197`
