from enum import Enum

class Item_Type(Enum):
    SWORD = "sword"
    BOW = "bow"
    STAFF = "staff"
    POTION = "potion"
    COIN = "coin"

class Item_Rarity(Enum):
    POOR = "poor"
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    UNIQUE = "unique"

class Item():
    def __init__(self, name: str, type: Item_Type, rarity: Item_Rarity, damage: int):
        self._name: str = name
        self._type: Item_Type = type
        self._rarity: Item_Rarity = rarity
        self._damage: int = damage
        self._quantity: int = 1

    def __repr__(self):
        return f"Name: {self._name} Type: {self._type.value} Rarity: {self._rarity.value} Damage: {self._damage}"

    def get_name(self) -> str:
        return self._name
    
    def get_type(self) -> Item_Type:
        return self._type

    def get_rarity(self) -> Item_Rarity:
        return self._rarity

    def get_damage(self) -> int:
        return self._damage
    
    def get_quantity(self) -> int:
        return self._quantity

    def inc_quantity(self) -> None:
        self._quantity += 1

    def dec_quantity(self) -> int:
        self._quantity -= 1
        return self._quantity