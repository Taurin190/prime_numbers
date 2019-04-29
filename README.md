# 素数を判定する問題
プログラム実行して、「入力した正数」が素数か判定するプログラム。

## 制約
- 言語の制約はなく、どの言語で実装してもよい
- 入力される値は正の数のみで1000までとする

## プラスアルファの条件
- 入力値が文字列、負の値、0の場合には、エラーを表示して再入力を求める
- 素数でない場合に何の数で割り切れるのか表示する

## 実行結果
### 正常系
- 1 : 正常値の最小値

        素数か判定したい1000までの正の整数を入力してください。
        1
        1は素数ではありません。
        1は1に素因数分解できます。

- 2 : 最初に処理を行う素数

        素数か判定したい1000までの正の整数を入力してください。
        2
        2は素数です。
        
- 4 : 最初の素数じゃない数

        素数か判定したい1000までの正の整数を入力してください。
        4
        4は素数ではありません。
        4は2,2に素因数分解できます。
- 997 : 1000以内の最大の素数

        素数か判定したい1000までの正の整数を入力してください。
        997
        997は素数です。
        
- 1000 : 正常値の最大の入力値

        素数か判定したい1000までの正の整数を入力してください。
        1000
        1000は素数ではありません。
        1000は2,2,2,5,5,5に素因数分解できます。
 
 
 ### 異常系
 - -1000 : 負の値
 - -1 : 負の値の境界値
 - 0 : 正数の境界値
 - 1001 : 最大値の境界値
 - aaa : 文字列

        素数か判定したい1000までの正の整数を入力してください。
        -1000
        有効な入力は1000までの正の整数です。
        
        素数か判定したい1000までの正の整数を入力してください。
        -1
        有効な入力は1000までの正の整数です。
        
        素数か判定したい1000までの正の整数を入力してください。
        0
        有効な入力は1000までの正の整数です。
        
        素数か判定したい1000までの正の整数を入力してください。
        1001
        有効な入力は1000までの正の整数です。
        
        素数か判定したい1000までの正の整数を入力してください。
        aaa
        有効な入力は1000までの正の整数です。