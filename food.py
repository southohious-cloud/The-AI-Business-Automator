class Food:
    base_hearts = 1

    def __init__(self, ingredients=None, hearts=None):
        if ingredients is None:
            ingredients = []

        self.ingredients = ingredients

        if hearts is not None:
            # Explicit hearts override calculation
            self.hearts = hearts
        else:
            self.hearts = Food.calculate_hearts(ingredients)

    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts

    @classmethod
    def from_nothing(cls, hearts):
        return cls(ingredients=[], hearts=hearts)


def main():
    mushroom_skewer = Food(ingredients=["Mushroom", "Hearty Mushroom"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts!")

    mushroom_skewer = Food.from_nothing(hearts=2)
    print(f"Food from nothing heals {mushroom_skewer.hearts} hearts!")


main()
