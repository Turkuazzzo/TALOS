import random
import sys
from typing import Optional

class Character:

    def __init__(self, name: str, max_hp: int, attack_min: int, attack_max:int, heal_value = 0):
        self.name = name
        self.hp = max_hp
        self.max_hp = max_hp
        self.attack_min = attack_min
        self.attack_max = attack_max 
        self.heal_value = heal_value

    # Hayattaysa canı 0'dan büyüktür True

    def is_alive(self) -> bool:
        return self.hp > 0
    
    # Saldırı fonksiyonu karakterin min-max saldırı değeri arasında
    # target 'a vurmasını sağlayan fonksiyon

    def attack(self, target: "Character") -> int:
        damage = random.randint(self.attack_min, self.attack_max)
        target.take_damage(damage)

    # damage verme fonksiyonu
    
    def take_damage(self, amount: int) -> None:
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0 # Bug olmaması için hp sıfırlar

    # iyileştirme fonksiyonu

    def heal(self) -> int:
        if self.heal_value <= 0:
            return 0
        
        heal_amount = min(self.heal_value, self.max_hp - self.hp) # Eksik canı tamamlamak için gereken can doldurma
        self.hp += heal_amount
        return heal_amount

    # karakterin can barı

    def status_line(self) -> str:
        return f"{self.name}: {self.hp}/{self.max_hp}"
    
class Game:
    def __init__(self):
        self.player: Optional[Character] = None
        self.enemy: Optional[Character] = None  # Kod başlatıldığında hata vermemesi için isimleri boşta bekletir
        self.turn_count = 0
        self.player_options = 2

        # Oyun zorluğu ve isim seçme, karakter statları ve pot sayıları

    def setup(self) -> None:
        print("=== Mini RPG ===")
        player_name = input("Lütfen kahraman adı giriniz.: ").strip() or "Kahraman"
        # strip -> başında ve sonunda boşluk varsa siler input yoksa boş string döndürür
        difficulty = self._choose_difficulty() # zorluk tanımlanma fonksiyonu aktive eder
        if difficulty == "easy":
            self.player = Character(player_name, max_hp = 100, attack_min=6, attack_max=12, heal_value=12)
            self.player_potions = 3
            self.enemy = Character("Gölge Canavar", max_hp = 30, attack_min =4, attack_max=9)
        elif difficulty == "hard":
            self.player = Character(player_name, max_hp=34, attack_min=5, attack_max=11, heal_value=10)
            self.player_potions = 1
            self.enemy = Character("Kırmızı Kabus", max_hp=46, attack_min=7, attack_max=13)
        else:  # normal
            self.player = Character(player_name, max_hp=36, attack_min=5, attack_max=12, heal_value=11)
            self.enemy = Character("Orta Seviye Canavar", max_hp=38, attack_min=5, attack_max=11)
            self.player_potions = 2

    def _choose_difficulty(self) -> str:
        while True:
            choice = input("Lütfen zorluk seçiniz (easy / normal / hard)").strip().lower() # Doğru kelime yanlış yaızm için input bug düzeltimi
            if choice == "":
                return "Normal"
            if choice in {"easy", "normal", "hard"}:
                return choice
            print("Geçersiz seçim. Tekrar seçiniz")

    def start(self) -> None:
        self.setup()
        while self.player.is_alive() and self.enemy.is_alive(): # oyun başladığında karakterin ve bossun can durumlarını kontrol eder
            self.turn_count += 1 # raund sayacı
            print(f"--- Tur {self.turn_count} ---")
            self._print_status() # tur başında karakter ve boss can durumları
            self.player_turn() # karakterin sırasında yapılacaklar
            if not self.enemy.is_alive(): # eğer boss yaşamıyorsa sonlandır
                break
            self.enemy_turn() # bossun sırası
            print()
        self._end_game()

    def player_turn(self) -> None:
        action = self._choose_action()
        if action == "a": # (a)ttack
            damage = self.player.attack(self.enemy)
            print(f"{self.player.name} saldırdı ve {damage} hasar verdi: ")
        elif action == "h": # (h)eal
            healed = self.player.heal()
            if healed:
                print(f"{self.player.name} kendini iyileştirdi: +{healed} HP.")
            else:
                print("İyileştirme kullanılamıyor")
        elif action == "p":
            if self.player_potions > 0:
                potion_heal = min(20, self.player.max_hp - self.player.hp)
                self.player.hp += potion_heal
                self.player_potions -= 1
                print(f"{self.player.name} iksir içti: +{potion_heal} HP. kalan iksir: {self.player_potions}")
            else:
                print("İksirin yok!")
                # Boş hamle yerine tekrar seçim hakkı
                self.player_turn()
        elif action == "s":
            if random.random() < 0.45:
                print(f"{self.player.name} kaçtı - mücadele sona erdi.")
                sys.exit(0)
            else:
                print(f"{self.player.name} kaçmayı başaramadı!")
        else: 
            print("Geçersiz eylem, sıra kaybedildi")

    def _choose_action(self) -> str:
        print("Eylemler: (a)ttack  (h)eal  (p)otion  (s)urrender/kaç")
        choice = input("Seçiminiz: ").strip().lower()
        return choice[:1] if choice else "a" # karşı tarafa hak geçecek eylem yapmadan hangi eylemler yapılmalı
    
    def enemy_turn(self) -> None:
        # Ya saldırır ya da güçlü vuruş dener
        if self.enemy.hp < self.enemy.max_hp * 0.25 and random.random() < 0.2:
            damage = random.randint(self.enemy.attack_min + 3, self.enemy.attack_max)
            self.player.take_damage(damage)
            print(f"{self.enemy.name} vahşice saldırdı! {self.player.name} {damage} hasar aldı.")
        else:
            damage = self.enemy.attack(self.player)
            print(f"{self.enemy.name} saldırdı ve {damage} hasar verdi.")

    def _print_status(self) -> None:
        print(self.player.status_line() + " | " + self.enemy.status_line())

    def _end_game(self) -> None:
        print("\n=== OYUN SONU ===")
        if self.player.is_alive() and not self.enemy.is_alive():
            print(f"Tebrikler, {self.enemy.name} yenildi!")
        elif not self.player.is_alive():
            print(f"{self.player.name} mağlup oldu. Yeniden dene!")
        else:
            print("Mücadele beklenmedik bir biçimde sonlandı.")
        print(f"Toplam tur: {self.turn_count}")

    
if __name__ == "__main__":
    random.seed()
    Game().start() # Start fonksiyonunda ilk kontrol edilmesi gereken şeyler ile başlatır ardından player_turn ile koda devam eder