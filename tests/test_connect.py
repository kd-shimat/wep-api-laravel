#!/usr/bin/env python
# ユニットテスト用ライブラリ
import unittest
import os

# SQLAlchemyを使う、テーブル構成は自動で行う
from sqlalchemy.ext.automap import automap_base

# 環境変数 MYSQL_USERの値をDBUSER変数に代入
DBUSER = os.getenv('MYSQL_USER')
# 同様に MYSQL_PASSWORD->DBPASS、MYSQL_DATABASE->DBNAMEに設定する
DBPASS = os.getenv('MYSQL_PASSWORD')
DBNAME = os.getenv('MYSQL_DATABASE')
# DBHOSTはdとする(構成上固定です)
DBHOST = "db"

# 接続文字列を作成し、dburlとする
dburl = f"mysql+mysqlconnector://{DBUSER}:{DBPASS}@{DBHOST}/{DBNAME}"

#DB接続エンジンの作成
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestConnect(unittest.TestCase):
    def setUp(self):
        # create_engineを使ってDBに接続しておく、必要に応じてユーザー、パスワードを渡す
        self.engine = create_engine(dburl)
        # automap_base()を使ってテーブル構成を自動取得
        self.Base = automap_base()
        self.Base.prepare(autoload_with=self.engine)
        # セッションを取得
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self) -> None:
        self.session.close()
        self.engine.dispose()

    def test_connect(self):
        # 接続に成功していれば真
        self.assertTrue(self.engine)

if __name__ == '__main__':
    unittest.main()


