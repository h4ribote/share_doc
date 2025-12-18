決定された**「市場連動型発行制度（Market-Backed Emission）」**に基づき、3つの主要なフェーズ（新規発行、資金調達、償還）における資金フローをMermaidで可視化しました。

---

### 1. 新規市場開拓と通貨発行（The Minting Phase）

これは**NC（自国通貨）が世界に生まれる唯一の瞬間**です。「政府が汗をかいて稼いだ外貨」と引き換えに、銀行がプール用のNCを発行します。

```mermaid
sequenceDiagram
    autonumber
    actor Gov as 政府 (財務省)
    participant Game as 新規ゲーム (L1)
    participant Bank as 中央銀行 (System)
    participant Pool as 流動性プール (AMM)

    Note over Gov, Pool: 【条件】新しいゲーム市場への接続時のみ実行可能

    Gov->>Game: 1. ゲームプレイ / ファーミング
    Game-->>Gov: 2. 原資獲得 (100万 Gil)
    Gov->>Gov: 3. Peg化 (100万 Peg)

    Gov->>Bank: 4. プール開設申請 (100万 Peg用意済み)

    Note over Bank: NCの発行
    opt ここが唯一の発行ポイント
        Bank->>Bank: 5. 100万 NC を新規発行 (Mint)
    end

    Bank->>Gov: 6. 100万 NC を引き渡し
    
    Gov->>Pool: 7. ペア投入 (100万 Peg : 100万 NC)
    Note over Pool: 市場形成完了 (xy=k スタート)

```

---

### 2. 国債発行による資金調達（The Funding Phase）

政府はNCを刷れないため、投資家から**「Peg（外貨）」**を借ります。中央銀行はこのプロセスに関与しません（規律の維持）。

```mermaid
sequenceDiagram
    autonumber
    actor Inv as 投資家
    actor Gov as 政府 (財務省)
    participant AC as 運用口座
    
    Note over Inv, AC: 【目的】運用資金の確保 (NC発行なし)

    Gov->>Inv: 1. 国債発行 (Peg建て / 年利付)
    
    alt 投資家がNCしか持っていない場合
        Inv->>Inv: プールでNCをPegに交換
    end

    Inv->>Gov: 2. 国債購入 (Peg支払い)
    Gov-->>Inv: 3. 国債券面 (Bond) 引き渡し

    Gov->>AC: 4. 調達したPegを入金
    Note right of AC: レバレッジ取引開始

```

---

### 3. 償還とエコシステムの循環（The Redemption Cycle）

運用益を使って借金を返し、その資金がまたプールに戻ってくることで、NCの価値（需要）が高まる仕組みです。

```mermaid
sequenceDiagram
    autonumber
    participant AC as 運用口座
    actor Gov as 政府 (財務省)
    actor Inv as 投資家
    participant Pool as 流動性プール (AMM)

    Note over AC, Pool: 【結末】利益確定と資金の還流

    AC->>Gov: 1. 運用益 + 元本 (Peg) 出金
    Gov->>Inv: 2. 満期償還 (Peg + 利子)
    Inv-->>Gov: 3. 国債券面を返却 (償却)

    Note over Inv, Pool: 投資家の選択 (エコシステムへの還流)
    opt NCの将来性に期待する場合
        Inv->>Pool: 4. 償還されたPegを投入 (Buy)
        Pool-->>Inv: 5. NC を受け取る
        Note right of Pool: プール内のPegが増え<br>NCが減る = NC価格上昇
    end

```

### この図解のポイント

1. **中央銀行の出番が少ない:** 図1（新規発行）にしか登場しません。これにより「政府が勝手に刷っていない」ことが視覚的にわかります。
2. **プールの役割:** 図3の最後にあるように、償還された資金が再びプールに戻ることで、**「国債運用が成功するほど、NCの価値（対Pegレート）が上がる」**という健全なサイクルが表現されています。
