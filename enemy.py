from item import Item


class Enemy(Item):
    """エネミークラス
    Itemを継承して作成したエネミークラス.
    ランダムに動きたい方向を計算する関数。（数字ごとに動く方向を当てはめて乱数で数字を与える。）と
    マップから移動して良いと許可が出たら座標を更新するメソッド
    を追加.

    Attributes:
        self.icon(str) : 表示されるアイテムのアイコン
        self.now_x(int) : 現在のx座標
        self.now_y(int) : 現在のy座標
        self.next_x(int) : 次の時刻でのx座標
        self.next_y(int) : 次の時刻でのy座標
        self.status(bool) : アイテムの状態（Trueなら存在する、Falseなら存在しない消滅した）
    """

    def __init__(self, x, y) -> None:
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
