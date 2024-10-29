from item import Item
from player import Player
from enemy import Enemy
from food import Food
from block import Block


class Field:
    """Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです。
    プレイヤー、敵、アイテムの位置を更新し、Fieldを表示する機能を持ちます。
    位置を更新する際に衝突判定を行います。

    Attributes:
        players (list[Player]): プレイヤーのリスト
        enemies (list[Enemy]): 敵のリスト
        foods (list[Food]]): アイテムのリスト
        blocks (list[Block]): アイテムのリスト
        field (list[list[str]]): フィールドの情報
        f_size (int): フィールドのサイズ
    """

    #  Fieldを生成する関数
    def __init__(
            self,
            players: list[Player],
            enemies: list[Enemy],
            foods: list[Food],
            blocks: list[Block],
            f_size: int = 6) -> None:

        """
        Fieldクラスの初期化を行う関数
        Args:
            players (list[Player]): プレイヤーのリスト
            enemies (list[Enemy]): 敵のリスト
            foods (list[Food]): アイテムのリスト
            blocks (list[Block]): ブロックのリスト
            f_size (int): フィールドのサイズ
        """
        pass

    def update_field(self) -> list[list[str]]:
        """
        敵、プレイヤー、アイテムを配置を参照して、Fieldを更新する関数
        Returns
        list[list[str]]: 更新されたField

        Examples:
        >>> p = [Player(1,0)]
        >>> p[0].icon = "p1"
        >>> e1 = Enemy(2,0)
        >>> e1.icon = "e1"
        >>> e2 = Enemy(1,1)
        >>> e2.icon = "e2"
        >>> e = [e1,e2]
        >>> f = [Food(0,1)]
        >>> f[0].icon = "f1"
        >>> b1 = Block(0,2)
        >>> b1.icon = "b1"
        >>> b2 = Enemy(1,2)
        >>> b2.icon = "b2"
        >>> b = [b1,b2]
        >>> field = field(p,e,f,b,3)
        >>> field.update_field()[0]
        ['\\u3000','p1','e1']
        >>> field.update_field()[1]
        ['f1','e2','\\u3000']
        >>> field.update_field()[2]
        ['b1','b2','\\u3000']
        """
        pass

    # 衝突判定を行う関数
    def check_bump(self, target: Item, items: list[Item]) -> Item | None:

        """
        2つのアイテムの位置が重なっているか判定する関数

        Args:
            target (Item): アイテム1
            items (list[Item]): アイテムのリスト2

        Returns:
            Item | None: 重なっているアイテムがあればそのアイテム、なければNone

        Examples:
            >>> p = Item(0,0)
            >>> e = Item(1,1)
            >>> field = Field([p],[e],[],[])
            >>> p.next_x = 1
            >>> r = field.check_bump(p,[e])
            >>> r is None
            True
            >>> p.next_y = 1
            >>> r = field.check_bump(p,[e])
            >>> r is e
            True
        """
    pass

    # Fieldを表示する関数
    def display_field(self) -> None:

        """
        Fieldを表示する関数

        Examples:
            >>> p = [Player(1,0)]
            >>> p[0].icon = "p1"
            >>> e1 = Enemy(2,0)
            >>> e1.icon = "e1"
            >>> e2 = Enemy(1,1)
            >>> e2.icon = "e2"
            >>> e = [e1,e2]
            >>> f = [food(0,1)]
            >>> f[0].icon = "f1"
            >>> b1 = Block(0,2)
            >>> b1.icon = "b1"
            >>> b2 = Enemy(1,2)
            >>> b2.icon = "b2"
            >>> b = [b1,b2]
            >>> field = Field(p,e,f,b,3)
            >>> field.display_field()
            w: 上に移動
            a: 左に移動
            s: 下に移動
            d: 右に移動
            p1e1
            f1e2
            b1b2
            """
        pass
