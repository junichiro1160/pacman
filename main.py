from game import Game
import os
import argparse
from config import common_args
from config import Parameters
from utils import dump_params
from utils import setup_params
from utils import set_logging
import logging


def main() -> None:

    # コマンドライン引数の設定
    parser = argparse.ArgumentParser()
    parser = common_args(parser)  # コマンドライン引数引数を読み込み
    # parser.add_argument("--main")
    # # 実行スクリプト固有のコマンドライン引数があればここに記入する．
    args = parser.parse_args()
    params = Parameters(**setup_params(vars(args), args.parameters))
    # args，run_date，git_revisionなどを追加した辞書を取得

    # 結果出力用ファイルの作成
    result_dir = f'result/{params.run_date}'  # 結果出力ディレクトリ
    os.mkdir(result_dir)  # 実行日時を名前とするディレクトリを作成
    dump_params(params, f'{result_dir}')  # パラメータを出力

    # ログ設定
    logger = logging.getLogger(__name__)
    set_logging(result_dir)  # ログを標準出力とファイルに出力するよう設定

    # 使用例
    logger.info('parameters: ')
    logger.info(params)
    # logger.info(params.param1)  # params変数は各パラメータにドットアクセスが可能．
    # logger.info(params.args['arg1'])  # コマンドライン引数はargs['']でアクセス．

    # ゲームの実行
    Game(params)


if __name__ == "__main__":
    main()
