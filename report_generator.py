import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

# 🔧 Stałe
INPUT_FILE = "../../../Downloads/alerts.csv"
CSV_OUTPUT = "raport_alerty_dzienny.csv"
XLSX_OUTPUT = "raport_alerty_dzienny.xlsx"
TXT_OUTPUT = "raport_alerty_dzienny.txt"
PLOT_OUTPUT = "alerty_wykres.png"

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Plik {INPUT_FILE} nie istnieje.")
        return

    print("📥 Wczytywanie danych...")
    df = pd.read_csv(INPUT_FILE)

    # Konwersja czasu UNIX (ms) na datetime
    df['timestamp'] = pd.to_datetime(df['time'] / 1000, unit='s')

    # Filtrowanie z ostatnich 24 godzin
    now = datetime.now()
    df_24h = df[df['timestamp'] >= now - timedelta(hours=24)]

    print(f"🔍 Liczba alertów z ostatnich 24h: {len(df_24h)}")

    if df_24h.empty:
        print("⚠️ Brak danych z ostatnich 24h. Kończenie programu.")
        return

    # Zapisywanie do plików
    df_24h.to_csv(CSV_OUTPUT, index=False)
    df_24h.to_excel(XLSX_OUTPUT, index=False)
    with open(TXT_OUTPUT, "w", encoding="utf-8") as f:
        f.write(df_24h.to_string(index=False))

    print("💾 Zapisano pliki:")
    print(f" - {CSV_OUTPUT}")
    print(f" - {XLSX_OUTPUT}")
    print(f" - {TXT_OUTPUT}")

    # Wykres liczby alertów wg poziomu ryzyka
    print("📊 Tworzenie wykresu...")
    risk_counts = df_24h['risk_level'].value_counts()
    plt.figure(figsize=(8, 6))
    risk_counts.plot(kind='bar')
    plt.title("Liczba alertów wg poziomu ryzyka (ostatnie 24h)")
    plt.xlabel("Poziom ryzyka")
    plt.ylabel("Liczba alertów")
    plt.tight_layout()
    plt.savefig(PLOT_OUTPUT)
    plt.close()
    print(f"✅ Zapisano wykres: {PLOT_OUTPUT}")

if __name__ == "__main__":
    main()
