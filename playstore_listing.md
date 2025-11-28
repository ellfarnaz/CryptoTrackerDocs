# Play Store Listing Content — Crypto Tracker

Use this file to copy/paste ready-to-use Play Store listing fields (English & Indonesian). Replace placeholders (e.g., URLs) after you enable GitHub Pages for the repo.

---

## App Name
- EN: Crypto Tracker - Portfolio Manager
- ID: Crypto Tracker - Manajer Portofolio

## Short description (80 chars max)
- EN: Track crypto prices, manage portfolio & set alerts. Real-time market data.
- ID: Pantau harga crypto, kelola portofolio & set notifikasi. Data pasar real-time.

## Full description (up to 4000 chars)
- EN:
```
Crypto Tracker - Portfolio Manager

Track live cryptocurrency prices, manage your holdings, get price alerts, and export your transactions — all in one simple app.

Key features:
• Real-time market data from CoinGecko
• Portfolio management with buy/sell tracking and P/L calculation
• Watchlist & customizable price alerts (background notifications)
• Crypto converter and interactive charts
• Export transactions to Excel and share
• Dark/Light themes and localization (English & Indonesian)
• Small, fast, privacy-first: all sensitive user data is kept locally

Why choose Crypto Tracker?
• Clean Neo-Brutalist UI
• Efficient background notifications with WorkManager
• Offline-safe portfolio tracking
• No ads, no in-app purchases

Download now and start tracking! For feedback: farelnazhari.22@gmail.com
```

- ID:
```
Crypto Tracker - Manajer Portofolio

Pantau harga cryptocurrency secara real-time, kelola kepemilikan, atur notifikasi harga, dan ekspor transaksi — semuanya lewat aplikasi sederhana ini.

Fitur utama:
• Data pasar real-time (CoinGecko)
• Manajemen portofolio dengan pencatatan buy/sell dan perhitungan P/L
• Watchlist & notifikasi harga kustom (background)
• Konverter crypto dan grafik interaktif
• Ekspor transaksi ke Excel dan bagikan
• Dark/Light theme dan dukungan bahasa EN/ID
• Privasi terjaga: data pengguna disimpan lokal

Kenapa pilih Crypto Tracker?
• UI Neo-Brutalism yang bersih
• Notifikasi background efisien (WorkManager)
• Pelacakan portofolio offline
• Tidak ada iklan, tidak ada pembelian dalam aplikasi

Unduh sekarang dan mulai lacak aset kripto Anda! Masukan: farelnazhari.22@gmail.com
```

## Screenshots & captions (EN/ID)
- 1) Home / Market — "Live Prices & Charts" / "Harga Real-time & Grafik"
- 2) Portfolio — "Portfolio & P/L Overview" / "Ringkasan Portfolio & P/L"
- 3) Alerts — "Price Alerts & Notifications" / "Notifikasi Harga"
- 4) Watchlist — "Watchlist for favorite coins" / "Watchlist koin favorit"
- 5) Converter — "Converter — fast & accurate" / "Konverter cepat & akurat"
- 6) Export — "Export transactions to Excel" / "Ekspor transaksi ke Excel"
- 7) Settings — "Dark/Light & Localization" / "Tema & Lokalitas"

> Tip: Provide 6–8 images. Use 1080x1920 or 1080x2340, PNG. Include a small overlay caption and/or device frame.

## Feature graphic
- Size: 1024 x 500 px (PNG/JPEG)
- Text suggestion: "TRACK • MANAGE • ALERT"
- Design: Neo-Brutalist, bright accent colors, minimal composition. Include app icon.

## App icon
- 512x512 PNG — recommended file: `assets/play_store_512.png`
- Adaptive icon layers: foreground + background (if used) in assets.

## Tags & Category
- Category: Finance
- Tags (keywords): cryptocurrency, portfolio, investment, tracker

## Contact details
- Email: farelnazhari.22@gmail.com
- Website: https://github.com/ellfarnaz/crypto_tracker
- Phone: Optional (leave blank if you prefer)

## Release notes (Short)
- EN: v1.0.0 — Initial Release
	• Market data (CoinGecko), portfolio tracking, alerts & watchlist
	• Background notifications, Excel export, converter, dark/light theme
	• Bug fixes and performance optimizations

- ID: v1.0.0 — Rilis Awal
	• Data pasar (CoinGecko), manajemen portofolio, notifikasi & watchlist
	• Notifikasi background, ekspor Excel, konverter, tema gelap/terang
	• Perbaikan bug & optimisasi performa

## Content Rating & Data Safety guidance
- Category: Finance
- Ads: No
- In-app purchases: No
- User-generated content: No
- Data Collection: Minimal — transaction records saved locally; market data fetched from CoinGecko (non-personal)
- If you use crash reporting or analytics (Firebase, Sentry), declare it in Data Safety (vendor & purpose)

## Privacy policy & Terms of Service (Placeholders)
- Privacy Policy URL: https://ellfarnaz.github.io/crypto_tracker/privacy-policy.html
- Terms of Service URL: https://ellfarnaz.github.io/crypto_tracker/terms-of-service.html

## Build & Upload instructions (quick)
- Generate signed AAB:
```bash
flutter build appbundle --release
```
- Upload to Play Console (Internal test) → QA → Promote to Production

## Notes & Reminders
- Ensure `android/key.properties` and `android/app/build.gradle` signing configs are correct (do not commit passwords).
- Verify targetSdk (compile settings in Gradle) and API targets as required by Play Store.
- Test functionality: notifications, export/share, localization, dark/light mode, and general UI.

---

If you want, I can split this file into two localized files (`docs/ listing_en.md` and `docs/listing_id.md`), convert the policy files to HTML for GitHub Pages, and run a quick lint to ensure Markdown correctness. Tell me which of these you prefer.

