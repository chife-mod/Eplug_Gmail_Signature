# EPlug Gmail Signature

HTML-подпись для Gmail, экспортированная из Figma.

## Файлы

| Файл | Описание |
|---|---|
| `signature.html` | **Рекомендуемый** — подпись-картинка, пиксель-перфект из Figma. Работает везде. |
| `signature-live.html` | Альтернативный — живой HTML с копируемым текстом. Сплошной фон (Gmail вырезает текстуру). |
| `index.html` | Превью обоих вариантов для локального просмотра. |
| `public/assets/images/` | PNG-ассеты, экспортированные из Figma @2x через Images API. |

## Установка в Gmail

1. Откройте `signature.html` в Chrome
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

- **Файл**: [Eplug-Web](https://www.figma.com/design/NsarAMa9SQMVyRCQDvgqg3/Eplug-Web?node-id=296-197)
- **Node**: `296:197` (Email Signature)
