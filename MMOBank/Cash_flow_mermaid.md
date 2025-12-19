### 1. 新規市場開拓と通貨発行（The Minting Phase）

これは**NC（自国通貨）が世界に生まれる唯一の瞬間**です。政府が獲得したL1通貨（原資）を中央銀行の金庫に預け入れ、その裏付けとして発行されたPegと、銀行が新規発行したNCをセットにして市場を作ります。

```mermaid
sequenceDiagram
    autonumber
    actor Gov as 政府 (財務省)
    participant Game as 新規ゲーム (L1)
    participant Bank as 中央銀行 (Custodian)
    participant Pool as 流動性プール (AMM)

    Note over Gov, Pool: 【条件】新しいゲーム市場への接続時のみ実行可能

    Gov->>Game: 1. ゲームプレイ / ファーミング
    Game-->>Gov: 2. 原資獲得 (100万 IGC)

    Note over Gov, Bank: 資産の分別管理 (Custody)
    Gov->>Bank: 3. 原資(IGC)を預入 (Deposit)
    Bank-->>Gov: 4. Pegを発行 (100万 Peg)

    Gov->>Bank: 5. プール開設申請 (対となるNCの発行依頼)

    Note over Bank: NCの発行
    opt ここが唯一の発行ポイント
        Bank->>Bank: 6. 100万 NC を新規発行 (Mint)
    end

    Bank->>Gov: 7. 100万 NC を引き渡し
    
    Gov->>Pool: 8. ペア投入 (100万 Peg : 100万 NC)
    Note over Pool: 市場形成完了 (xy=k スタート)

```

---

### 2. 国債発行による資金調達（The Funding Phase）

政府は**「NC建て」**で借金をします。投資家はNCを用意する必要があり、政府は借りたNCを運用資金（Peg）に換えます。

```mermaid
sequenceDiagram
    autonumber
    actor Inv as 投資家
    actor Gov as 政府 (財務省)
    participant Pool as 流動性プール (AMM)
    participant AC as 運用口座
    
    Note over Inv, AC: 【目的】NCの借入と、運用資金(Peg)化

    Gov->>Inv: 1. 国債発行 (NC建て / 年利付)
    
    opt 投資家がPegしか持っていない場合
        Inv->>Pool: 2. 手持ちPegを売却 (Buy NC)
        Pool-->>Inv: NCを受け取る
        Note right of Pool: NC価格上昇 (需要発生)
    end

    Inv->>Gov: 3. 国債購入 (NC支払い)
    Gov-->>Inv: 4. 国債券面 (Bond) 引き渡し

    Note over Gov, Pool: 政府による資金変換
    Gov->>Pool: 5. 調達したNCを売却 (Sell NC)
    Pool-->>Gov: Pegを受け取る
    
    Gov->>AC: 6. 調達したPegを入金

```

---

### 3. 償還とエコシステムの循環（The Redemption Cycle）

運用益（Peg）を使って、市場から**NCを買い戻し（Buyback）**、投資家に返済します。この「買い戻し」がNCの価値を支えます。

```mermaid
sequenceDiagram
    autonumber
    participant AC as 運用口座
    actor Gov as 政府 (財務省)
    participant Pool as 流動性プール (AMM)
    actor Inv as 投資家

    Note over AC, Pool: 【結末】利益確定とNCの買い戻し

    AC->>Gov: 1. 運用益 + 元本 (Peg) 出金
    
    Note over Gov, Pool: 返済原資の調達 (強力な買い圧)
    Gov->>Pool: 2. Pegを投入 (Buy NC)
    Pool-->>Gov: 3. NC を受け取る
    Note right of Pool: 政府の利益分だけ<br>NCの純粋な買い圧となる

    Gov->>Inv: 4. 満期償還 (NC + 利子)
    Inv-->>Gov: 5. 国債券面を返却 (償却)

    Note over Inv: 投資家の選択
    opt そのままNCを保有 (再投資など)
        Inv->>Inv: NC保有継続 = 売り圧なし
    end

```
