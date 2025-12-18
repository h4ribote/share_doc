## 🎯 ターゲット (Target)

ターゲットを指定するためのオプションです。

| オプション | 説明 |
| :--- | :--- |
| `-u URL`, `--url=URL` | ターゲット URL (例: `http://www.site.com/vuln.php?id=1`) |
| `-d DIRECT` | データベースへの直接接続文字列 |
| `-l LOGFILE` | Burp や WebScarab のプロキシログファイルからターゲットを解析 |
| `-m BULKFILE` | テキストファイルに記載された複数のターゲットをスキャン |
| `-r REQUESTFILE` | ファイルから生の HTTP リクエストを読み込む |
| `-g GOOGLEDORK` | Google dork (検索クエリ) の結果をターゲットとして処理 |
| `-c CONFIGFILE` | 設定 INI ファイルからオプションを読み込む |

## 📡 リクエスト (Request)

ターゲットへの接続方法を指定するオプションです。

| オプション | 説明 |
| :--- | :--- |
| `-A AGENT`, `--user-agent=AGENT` | HTTP User-Agent ヘッダの値を指定 |
| `-H HEADER`, `--header=HEADER` | 追加の HTTP ヘッダを指定 (例: `"X-Forwarded-For: 127.0.0.1"`) |
| `--method=METHOD` | 指定した HTTP メソッド (例: `PUT`) の使用を強制 |
| `--data=DATA` | POST で送信するデータ文字列 (例: `"id=1"`) |
| `--param-del=PDEL` | パラメータ値を分割する文字 (例: `&`) |
| `--cookie=COOKIE` | HTTP Cookie ヘッダの値を指定 |
| `--random-agent` | ランダムな HTTP User-Agent ヘッダを使用 |
| `--proxy=PROXY` | プロキシ (例: `http://localhost:8080`) を使用して接続 |
| `--tor` | Tor 匿名ネットワークを使用 |
| `--delay=DELAY` | 各 HTTP リクエスト間の遅延 (秒) |
| `--timeout=TIMEOUT` | 接続タイムアウトまでの待機秒数 (デフォルト 30) |
| `--retries=RETRIES` | 接続タイムアウト時の再試行回数 (デフォルト 3) |
| `--force-ssl` | SSL/HTTPS の使用を強制 |
| `--hpp` | HTTP パラメータ汚染 (HPP) メソッドを使用 |
| `--eval=EVALCODE` | リクエスト直前に Python コードを評価 |

## ⚙️ 最適化 (Optimization)

パフォーマンスを最適化するためのオプションです。

| オプション | 説明 |
| :--- | :--- |
| `-o` | すべての最適化スイッチをオンにする |
| `--keep-alive` | 持続的な HTTP(s) 接続 (Keep-Alive) を使用 |
| `--null-connection` | HTTP レスポンスボディなしでページ長を取得する手法を使用 |
| `--threads=THREADS` | 同時 HTTP(s) リクエストの最大数 (デフォルト 1) |

## 💉 インジェクション (Injection)

テスト対象のパラメータやペイロードを指定するオプションです。

| オプション | 説明 |
| :--- | :--- |
| `-p TESTPARAMETER` | テストするパラメータを指定 (例: `"id"`) |
| `--skip=SKIP` | テストをスキップするパラメータを指定 (例: `"user-agent"`) |
| `--dbms=DBMS` | バックエンドの DBMS (例: `"mysql"`) を強制的に指定 |
| `--os=OS` | バックエンド DBMS の OS (例: `"windows"`) を強制的に指定 |
| `--prefix=PREFIX` | インジェクションペイロードのプレフィックス (接頭辞) を指定 |
| `--suffix=SUFFIX` | インジェクションペイロードのサフィックス (接尾辞) を指定 |
| `--tamper=TAMPER` | ペイロードを改ざん (難読化) するためのタンパースクリプトを使用 |

## 🔬 検出 (Detection)

検出フェーズをカスタマイズするオプションです。

| オプション | 説明 |
| :--- | :--- |
| `--level=LEVEL` | 実行するテストのレベル (1-5, デフォルト 1) |
| `--risk=RISK` | 実行するテストのリスク (1-3, デフォルト 1) |
| `--string=STRING` | クエリが True の場合にページ内に存在する文字列 |
| `--not-string=NOTSTR` | クエリが False の場合にページ内に存在する文字列 |
| `--regexp=REGEXP` | クエリが True の場合にページ内容と一致する正規表現 |
| `--code=CODE` | クエリが True の場合に返される HTTP ステータスコード |
| `--smart` | 肯定的なヒューリスティック (手がかり) がある場合のみ徹底的なテストを実行 |
| `--text-only` | ページのテキストコンテンツのみに基づいて比較 |

## 🧪 テクニック (Techniques)

使用する SQL インジェクションのテクニックを指定するオプションです。

| オプション | 説明 |
| :--- | :--- |
| `--technique=TECH` | 使用する SQL インジェクションテクニック (デフォルト: `BEUSTQ`) <br> `B`: Boolean-based blind (ブール値ベース) <br> `E`: Error-based (エラーベース) <br> `U`: Union query-based (UNION クエリベース) <br> `S`: Stacked queries (スタッククエリ) <br> `T`: Time-based blind (時間ベース) <br> `Q`: Inline queries (インラインクエリ) |
| `--time-sec=TIMESEC` | 時間ベースのテクニックで DBMS の応答を遅延させる秒数 (デフォルト 5) |
| `--union-cols=UCOLS` | UNION クエリでテストするカラム数の範囲 (例: `1-10`) |

## 🕵️ フィンガープリント (Fingerprint)

| オプション | 説明 |
| :--- | :--- |
| `-f`, `--fingerprint` | 広範な DBMS バージョンのフィンガープリントを実行 |

## 📊 列挙 (Enumeration)

データベースの情報を抜き出すためのオプションです。

| オプション | 説明 |
| :--- | :--- |
| `-a`, `--all` | すべての情報を取得 (バナー、ユーザー、DB、テーブルなど) |
| `-b`, `--banner` | DBMS のバナー (バージョン情報) を取得 |
| `--current-user` | DBMS の現在のユーザーを取得 |
| `--current-db` | 現在のデータベース名を取得 |
| `--hostname` | DBMS サーバーのホスト名を取得 |
| `--is-dba` | 現在のユーザーが DBA (管理者) かどうかを検出 |
| `--users` | DBMS ユーザーのリストを取得 |
| `--passwords` | DBMS ユーザーのパスワードハッシュを取得 |
| `--privileges` | DBMS ユーザーの権限を取得 |
| `--dbs` | データベースのリストを取得 |
| `--tables` | テーブルのリストを取得 |
| `--columns` | カラムのリストを取得 |
| `--schema` | DBMS の全スキーマ (DB、テーブル、カラム) を取得 |
| `--dump` | テーブルのエントリ (データ) をダンプ |
| `--dump-all` | すべてのデータベースの全テーブルのデータをダンプ |
| `--search` | カラム名、テーブル名、データベース名を検索 |
| `-D DB` | 列挙対象のデータベースを指定 |
| `-T TBL` | 列挙対象のテーブルを指定 |
| `-C COL` | 列挙対象のカラムを指定 |
| `-U USER` | 列挙対象のユーザーを指定 |
| `--sql-query=QUERY` | 任意の SQL クエリを実行 |
| `--sql-shell` | 対話型の SQL シェルを起動 |

## 📂 ファイルシステムと OS へのアクセス

データベースサーバーのファイルシステムや OS を操作するオプションです。

| オプション | 説明 |
| :--- | :--- |
| `--file-read=FILE` | サーバーのファイルシステムからファイルを読み取る |
| `--file-write=LFILE` | ローカルファイルをサーバーに書き込む |
| `--file-dest=RFILE` | サーバーに書き込む際の絶対パスを指定 |
| `--os-cmd=OSCMD` | 任意の OS コマンドを実行 |
| `--os-shell` | 対話型の OS シェルを起動 |
| `--os-pwn` | Meterpreter などのアウトオブバンド (OOB) シェルを取得 |
| `--priv-esc` | データベースプロセスユーザーの権限昇格を試みる |

## 🖥️ Windows レジストリアクセス

| オプション | 説明 |
| :--- | :--- |
| `--reg-read` | Windows レジストリキーの値を読み取る |
| `--reg-add` | Windows レジストリキーの値を書き込む |
| `--reg-del` | Windows レジストリキーの値を削除 |

## 🔧 一般 (General)

一般的な動作設定オプションです。

| オプション | 説明 |
| :--- | :--- |
| `-s SESSIONFILE` | セッションファイル (.sqlite) を指定して状態を保存・復元 |
| `-t TRAFFICFILE` | すべての HTTP トラフィックを指定ファイルに記録 |
| `--batch` | 対話モードを無効にし、すべての質問にデフォルトで回答 |
| `--answers=ANSWERS` | 質問に対する回答をあらかじめ指定 (例: `"quit=N"`) |
| `--crawl=DEPTH` | 指定した深度で Web サイトをクロール |
| `--forms` | ターゲット URL のフォームを解析してテスト |
| `--flush-session` | 現在のターゲットのセッションファイルを破棄 |
| `--update` | sqlmap を最新の Git バージョンに更新 |
| `--wizard` | 初心者向けのウィザードインターフェイスを起動 |
| `--beep` | SQL インジェクションが見つかったときにビープ音を鳴らす |
| `--disable-coloring` | コンソール出力の色付けを無効にする |
| `--smart` | 検出を高速化するため、動的なパラメータのみを対象にテスト |
| `--skip-waf` | WAF/IPS (Web アプリケーションファイアウォール) の検出をスキップ |
| `-z MNEMONICS` | オプションを短いニーモニック (省略形) で指定 (例: `"bat,ban,tec=U"`) |
