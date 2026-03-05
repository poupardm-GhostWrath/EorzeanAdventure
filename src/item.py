from enum import Enum

class Item_Type(Enum):
    SWORD = "Sword"
    BOW = "Bow"
    STAFF = "Staff"
    POTION = "Potion"
    FOOD = "Food"
    COIN = "Coin"

class Item_Rarity(Enum):
    POOR = "Poor"
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    UNIQUE = "Unique"

class Item():
    def __init__(self, name: str, type: Item_Type, quantity: int=1):
        self._name: str = name
        self._type: Item_Type = type
        self._quantity: int = quantity

    def __repr__(self):
        return f"Name: {self._name} Type: {self._type.value} Rarity: {self._rarity.value} Damage: {self._damage}"

    def get_name(self) -> str:
        return self._name
    
    def get_type(self) -> Item_Type:
        return self._type
    
    def get_quantity(self) -> int:
        return self._quantity

    def inc_quantity(self) -> None:
        self._quantity += 1

    def dec_quantity(self) -> int:
        self._quantity -= 1
        return self._quantity

class Weapon(Item):
    def __init__(self, name: str, type: Item_Type, rarity: Item_Rarity, damage: int):
        super().__init__(name, type)
        self._rarity: Item_Rarity = rarity
        self._damage: int = damage

    def get_rarity(self) -> Item_Rarity:
        return self._rarity

    def get_damage(self) -> int:
        return self._damage

class Consumable(Item):
    def __init__(self, name: str, type: Item_Type, quantity: int, recovery_amount: int):
        super().__init__(name, type, quantity)
        self._recoveryAmount = recovery_amount

    def get_recover_amount(self) -> int:
        return self._recoveryAmount