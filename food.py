from item import Item


class Food(Item):
    """
    Foodクラス
    アイテムの位置とアイコンを管理するクラス

    Arreibutes:
        now_x (int): 現在のx座標
        now_y (int): 現在のy座標
        status (bool): アイテムの状態
        icon (str): 表示アイコン

    Examples:
        >>> food = Food(4, 5)
        >>> food.now_x
        4
        >>> food.now_y
        5
        >>> food.icon
        '🍜'
        >>> food.status
        True
    """

    pass

    def __init__(self, x, y) -> None:
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass
