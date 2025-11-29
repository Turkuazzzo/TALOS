import datetime

# Görev ekleme fonksiyonu

def add_task(tasks):
    name = input("Lütfen görev adını giriniz")
    priority = int(input("Öncelik (1=çok önemli, 5=düşük): "))
    date_str = input("Lütfen görev tarihini giriniz (GG-AA-YYYY)")
    day, month, year = map(int, date_str.split("-")) # **-**-**** tipinde girilmeli
    date = datetime.date(year, month, day) # girilen datayı date olarak ayarlar
    tasks.append({"name" : name, "priority" : priority, "date" : date})
    print("Görev eklendi\n")

# Görev önemine göre sıralama fonksiyonu

def sort_by_priority(tasks):
    for i in range(len(tasks)):
        min_idx = i
        for j in range(i+1, len(tasks)):
            if tasks[j]["priority"] < tasks[min_idx]["priority"]:
                min_idx = j
            tasks[i], tasks[min_idx] = tasks[min_idx], tasks[i]

# Verilen tarihteki görevi bulma fonksiyonu

def filter_by_date(tasks, target_date):
    filtered = []
    for t in tasks:
        if t["date"] == target_date:
            filtered.append(t)
    return filtered

# Tüm görevleri gösterme fonksiyonu

def display_tasks(task_list):
    if not task_list:
        print("Görev bulunamadı")
        return
    for t in task_list:
        print(f"- {t["name"]} | Öncelik: {t["priority"]} | Tarih: {t["date"]}")

# main ve çıkış fonksiyonu

def main():
    tasks = []

    while True:
        print("\=== Daily Sistemi ===")
        print("1) Görev ekle")
        print("2) Görevleri önceliğe göre sırala")
        print("3) Belirli bir tarihteki görevleri göster")
        print("4) Tüm görevleri göster")
        print("5) Çıkış")

        choice = input("Seçim : ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            sort_by_priority(tasks)
            print("Sıralandı!\n")
        elif choice == "3":
            date_str = input("Hangi tarih? (GG-AA-YYYY): ")
            day, month, year = map(int, date_str.split("-"))
            target = datetime.date(year, month, day)
            filtered = filter_by_date(tasks, target)
            display_tasks(filtered)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            print("Çıkılıyor... Hoşçakal!")
            break
        else:
            print("Hatalı seçim, tekrar dene!")

if __name__ == "__main__":
    main()