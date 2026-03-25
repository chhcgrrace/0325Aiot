# 📡 0325Aiot - 全方位 AIoT 智能數據視覺化系統

![Dashboard Screenshot](動態板板.jpg)

> **這是一個專為 AIoT 設計的完整解決方案，模擬從硬體掛載、數據採集到雲端即時顯示的全過程。**

---

## 🚀 雲端動態演示 (Live Demo)
如果您不想在本地執行，可以直接點擊下方連結查看雲端版本（包含模擬數據）：

👉 **[點此進入 Streamlit 雲端儀表板](https://0325aiot-hkrg4zclkswrtkvmdp3zg3.streamlit.app/)** 

---

## 🛠️ 專案用途與功能亮點

本專案模擬了一個典型的智慧物聯網監測場景，具備以下核心能力：

- **ESP32 數據模擬**：精確模擬 DHT11 溫濕度計每 2 秒產生的真實動態數據。
- **後端中繼系統**：使用 Flask 建立的高效能 API，負責接收數據並自動加上「亞洲/台北」時區標籤。
- **持久化儲存**：利用 SQLite3 資料庫穩定存儲所有歷史採集記錄。
- **即時視覺化**：透過 Streamlit 打造的高質感儀表板，提供：
    - 🌡️ **即時溫濕度 KPI 卡片**
    - 📈 **動態歷史變化趨勢圖**
    - 📋 **詳細歷史日誌數據表格**
    - ☁️ **雲端 Mock 模式**：即使在 GitHub/Streamlit Cloud 也能無縫展示動態效果。

---

## 📂 系統架構簡述

1.  **`esp32_generator.py`**：虛擬硬體設端，透過 HTTP POST 推送 JSON 數據。
2.  **`app.py`**：輕量級 Flask Web Server，扮演數據資料中心的橋樑。
3.  **`dashboard.py`**：基於 Python 的動態網頁前端，提供 UI 視覺呈現。
4.  **`aiotdb.db`**：SQLite 持久層資料庫，存儲所有感測器記錄。

---

## ⚙️ 如何在本地端啟動 (Local Quick Start)

### 1️⃣ 前置準備
確保您的環境已安裝 Python 3.9+，然後執行：

```powershell
# 建立虛擬環境
python -m venv venv

# 啟動環境 (Windows)
.\venv\Scripts\activate

# 安裝所需套件
pip install -r requirements.txt
```

### 2️⃣ 啟動伺服器群 (建議開啟三個終端機)

**Terminal A：啟動後端資料中心**
```powershell
python app.py
```

**Terminal B：模擬硬體數據上傳**
```powershell
python esp32_generator.py
```

**Terminal C：啟動視覺化網頁**
```powershell
streamlit run dashboard.py
```

---

## 📋 開發日誌 (Success Stories)
- ✅ 成功解決 Streamlit Cloud 上的 Python 3.14 編譯相容性問題 (切換至 3.12)。
- ✅ 完美實現數據在雲端環境下的 Mock 模式偵測。
- ✅ 完整實作 Taiwan TimeZone 資料寫入邏輯。

---
*Powered by Antigravity AI @ Google DeepMind.*
