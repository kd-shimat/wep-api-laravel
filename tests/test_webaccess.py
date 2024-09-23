#!/usr/bin/env python

# selenium使います
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# テスト用のライブラリ
import unittest


# テスト用のサーバー(Selenium grid)
REMOTE_URL = "http://selenium:4444/wd/hub"

class TestCase(unittest.TestCase):
    def setUp(self):
        # カレントディレクトリを取得して表示
        import os
        print(os.getcwd())
        # カレントディレクトリにあるpublicディレクトリのアクセス権を確認する
        print(os.system("ls -ld public"))

        # selenium gridのサーバーに接続
        self.driver = webdriver.Remote(REMOTE_URL, options=webdriver.ChromeOptions())
        # テスト用のファイルを作成
        with open("/app/public/testcase.html", "w") as f:
            f.write("<html><head><title>This is a pen</title></head><body></body></html>")
        with open("/app/public/testcase.php", "w") as f:
            f.write("<html><head><title><?php echo 'This is a pen';?></title></head><body></body></html>")

    def tearDown(self):
        # テストサーバー切断
        self.driver.quit()
        # public/testcase.htmlおよびpublic/testcase.phpを削除
        import os
        [os.remove(f"public/testcase.{ext}") for ext in ["html", "php"]]

    # ホストwebに接続し、タイトルを取得するテスト
    def test_access(self):
        self.driver.get("http://web/testcase.html")
        self.assertIn("This is a pen", self.driver.title)

    # ホストwebに接続し、タイトルを取得するテスト(PHP)
    def test_access_php(self):
        self.driver.get("http://web/testcase.php")
        self.assertIn("This is a pen", self.driver.title)


if __name__ == "__main__":
    unittest.main()
