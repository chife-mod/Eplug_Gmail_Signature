# Деплой и хостинг подписей Eplug / Energy Plus

Код живёт на GitHub, публикуется на **Cloudflare Pages** (быстро, без очередей).
GitHub Pages оставлен как запасной, но ненадёжен по времени раскатки.

## Хостинг

| Что | Где | URL |
|---|---|---|
| **Основной (быстрый)** | Cloudflare Pages, проект `eplug-gmail-signature`, аккаунт `mod.inbox@gmail.com` | https://eplug-gmail-signature.pages.dev/ |
| Запасной | GitHub Pages (ветка `main`) | https://chife-mod.github.io/Eplug_Gmail_Signature/ |
| Мгновенный превью из `main` | githack (без ожидания сборки) | `https://raw.githack.com/chife-mod/Eplug_Gmail_Signature/main/<file>.html` |

**Почему Cloudflare основной:** 2026-08-06 сборка GitHub Pages застряла в очереди
GitHub Actions на 25+ минут (`status: building`), публичная ссылка не
обновлялась. Cloudflare раскатывает те же файлы за ~1 секунду.

## Как задеплоить на Cloudflare

`wrangler` уже залогинен (OAuth, `mod.inbox@gmail.com`). Деплоим **чистую
staging-папку** — без `.git`, `qa/`, мастеров `_src` (иначе тянется лишнее):

```bash
cd /Users/oleg/Dev/bl/gmail-signature
STG="$(mktemp -d)/cf-deploy"; mkdir -p "$STG"
cp *.html .nojekyll "$STG"/ 2>/dev/null
cp -R public "$STG"/public
find "$STG/public" -type d -name '_src' -prune -exec rm -rf {} +
wrangler pages deploy "$STG" \
  --project-name=eplug-gmail-signature --branch=main --commit-dirty=true
```

Cloudflare делает «чистые URL»: `/signature-320-freund.html` отдаёт 308-редирект
на extensionless-путь — оба варианта работают в браузере.

## Рабочий цикл при правках

1. Правка HTML → пиксель-дифф/рендер (см. `oz/mod-manager/templates/email-signature`).
2. `git add … && git commit && git push origin main` — код на GitHub.
3. Команда деплоя выше — публикация на Cloudflare (обновляется сразу).
4. Проверка живого URL (charcoal/ссылки на месте, картинки 200). Кэш edge на
   `pages.dev` может секунду отдавать старое — проверяй с `?v=<ts>` или по
   уникальному deploy-URL из вывода wrangler.

## Подтверждённые ссылки (2026-08-06)

- **VUE-баннер (нижняя картинка)** во всех промо-подписях ведёт на:
  `https://energyplusny.com/get-early-access-to-vue/`
- Контакт «website» в подписи — `https://energyplusny.com` (это другая ссылка,
  не путать с баннером).
