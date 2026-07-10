# EPlug Gmail Signature

HTML-подпись для Gmail, экспортированная из Figma.

## Файлы

| Файл | Описание |
|---|---|
| `signature-v3.html` | **Актуальный (2026-07)** — светлый макет из Figma `4869:509`: имя/контакты слева, логотипы Eplug + Energy Plus справа за разделителем. |
| `signature-v2.html` | V2 — розово-зелёный макет с двумя лого-блоками. |
| `signature.html` | V1 — подпись-картинка, пиксель-перфект из Figma. |
| `signature-live.html` | V1 альтернативный — живой HTML с копируемым текстом. |
| `index.html` | Превью V1-вариантов для локального просмотра. |
| `public/assets/images/` | PNG-ассеты из Figma (V1/V2 @2x, V3 @4x). |

## Установка в Gmail

1. Откройте `signature-v3.html` в Chrome
2. `Cmd+A` (выделить всё) → `Cmd+C` (копировать)
3. Gmail → ⚙️ → **See all settings** → **General** → **Signature**
4. `Cmd+V` (вставить)
5. **Save Changes**

## Хостинг изображений

Подпись использует GitHub Pages для хостинга картинок:
```
https://chife-mod.github.io/Eplug_Gmail_Signature/public/assets/images/...
```

Для активации GitHub Pages:
1. GitHub → Settings → Pages
2. Source: **Deploy from a branch**
3. Branch: `main` / `root`
4. Save

## Figma

- **V3**: [Eplug-Design](https://www.figma.com/design/GXUObJIRiX2EfkOujCyNIq/Eplug-Design?node-id=4869-509) — node `4869:509` (Michael Elhav)
- **V2**: Eplug-Design, node `4700:912`
- **V1**: [Eplug-Web](https://www.figma.com/design/NsarAMa9SQMVyRCQDvgqg3/Eplug-Web?node-id=296-197) — node `296:197`
