from math import floor
from random import randint

first_name = input('マッチ準備 ゲーム1先攻プレイヤーの名前を入力してください：')
second_name = input('マッチ準備 ゲーム1後攻プレイヤーの名前を入力してください：')
first_score = 0
second_score = 0
game = 1

while game <= 6 and first_score < 21 and second_score < 21:
    while True:
        first = randint(1, 99)
        second = randint(1, 99)
        sc = 1
        f1 = (first + second * sc) % 10
        fc = 1
        s1 = (second + f1 * fc) % 10
        s2 = (second + first * fc) % 10
        f2 = (first + s2 * sc) % 10
        if game % 2 == 1:
            if first > second:
                if first % 10 != 0 and second % 10 != 0:
                    if first % 10 != 6 or second % 10 != 6:
                        if (first + second) % 10 != 0:
                            if f1 != 0 and f2 != 0 and s1 != 0 and s2 != 0:
                                break
        else:
            if first < second:
                if first % 10 != 0 and second % 10 != 0:
                    if first % 10 != 6 or second % 10 != 6:
                        if (first + second) % 10 != 0:
                            if f1 != 0 and f2 != 0 and s1 != 0 and s2 != 0:
                                break
    first_act = first % 10
    second_act = second % 10
    first_command_input = 0
    second_command_input = 0
    first_command = 1
    second_command = 1
    turn = 1

    if game % 2 == 1:
        print(f'ゲーム{game} 準備 （先攻）{first_name}：{first} （後攻）{second_name}：{second}')
        while turn <= 50 and first_act != 0 and second_act != 0:
            if first_command == 0:
                second_command = 1
                print(f'ターン{turn} 自動 {second_name}は自動的に突き')
                first = (first + second_act * second_command) % 100
                first_act = first % 10
                print(f'ターン{turn} 結果 {first_name}：{first} {second_name}：{second}')
                turn += 1
                first_command = 1
                print(f'ターン{turn} 自動 {first_name}は自動的に突き')
                second = (second + first_act * first_command) % 100
                second_act = second % 10
                print(f'ターン{turn} 結果 {first_name}：{first} {second_name}：{second}')
            elif second_command == 0:
                first_command = 1
                print(f'ターン{turn} 自動 {first_name}は自動的に突き')
                second = (second + first_act * first_command) % 100
                second_act = second % 10
                print(f'ターン{turn} 結果 {first_name}：{first} {second_name}：{second}')
                turn += 1
                second_command = 1
                print(f'ターン{turn} 自動 {second_name}は自動的に突き')
                first = (first + second_act * second_command) % 100
                first_act = first % 10
                print(f'ターン{turn} 結果 {first_name}：{first} {second_name}：{second}')
            else:
                if turn % 2 == 1:
                    while True:
                        first_command_input = input(
                            f'ターン{turn} 行動 {first_name}のターンです（突き＝１、引き＝０）：')
                        if first_command_input == '0' or first_command_input == '1':
                            first_command = int(first_command_input)
                            break
                    second = (second + first_act * first_command) % 100
                    second_act = second % 10
                else:
                    while True:
                        second_command_input = input(
                            f'ターン{turn} 行動 {second_name}のターンです（突き＝１、引き＝０）：')
                        if second_command_input == '0' or second_command_input == '1':
                            second_command = int(second_command_input)
                            break
                    first = (first + second_act * second_command) % 100
                    first_act = first % 10
                print(f'ターン{turn} 結果 {first_name}：{first} {second_name}：{second}')
            turn += 1

    else:
        print(f'ゲーム{game} 準備 （先攻）{second_name}：{second}（後攻）{first_name}：{first}')
        while turn <= 50 and first_act != 0 and second_act != 0:
            if first_command == 0:
                second_command = 1
                print(f'ターン{turn} 自動 {second_name}は自動的に突き')
                first = (first + second_act * second_command) % 100
                first_act = first % 10
                print(f'ターン{turn} 結果 {second_name}：{second} {first_name}：{first}')
                turn += 1
                first_command = 1
                print(f'ターン{turn} 自動 {first_name}は自動的に突き')
                second = (second + first_act * first_command) % 100
                second_act = second % 10
                print(f'ターン{turn} 結果 {second_name}：{second} {first_name}：{first}')
            elif second_command == 0:
                first_command = 1
                print(f'ターン{turn} 自動 {first_name}は自動的に突き')
                second = (second + first_act * first_command) % 100
                second_act = second % 10
                print(f'ターン{turn} 結果 {second_name}：{second} {first_name}：{first}')
                turn += 1
                second_command = 1
                print(f'ターン{turn} 自動 {second_name}は自動的に突き')
                first = (first + second_act * second_command) % 100
                first_act = first % 10
                print(f'ターン{turn} 結果 {second_name}：{second} {first_name}：{first}')
            else:
                if turn % 2 == 0:
                    while True:
                        first_command_input = input(
                            f'ターン{turn} 行動 {first_name}のターンです（突き＝１、引き＝０）：')
                        if first_command_input == '0' or first_command_input == '1':
                            first_command = int(first_command_input)
                            break
                    second = (second + first_act * first_command) % 100
                    second_act = second % 10
                else:
                    while True:
                        second_command_input = input(
                            f'ターン{turn} 行動 {second_name}のターンです（突き＝１、引き＝０）：')
                        if second_command_input == '0' or second_command_input == '1':
                            second_command = int(second_command_input)
                            break
                    first = (first + second_act * second_command) % 100
                    first_act = first % 10
                print(f'ターン{turn} 結果 {second_name}：{second} {first_name}：{first}')
            turn += 1
    if second_act == 0:
        first_score += floor(first / 10) + 1
        print(
            f'ゲーム{game}は{first_name}の勝ちです　{first_name} {first_score}-{second_score} {second_name}'
        )
    elif first_act == 0:
        second_score += floor(second / 10) + 1
        print(
            f'ゲーム{game}は{second_name}の勝ちです　{first_name} {first_score}-{second_score} {second_name}'
        )
    elif turn > 50:
        if first > second:
            first_score += 1
            print(
                f'ゲーム{game}は{first_name}の優勢勝ちです　{first_name} {first_score}-{second_score} {second_name}'
            )
        elif first < second:
            second_score += 1
            print(
                f'ゲーム{game}は{second_name}の優勢勝ちです　{first_name} {first_score}-{second_score} {second_name}'
            )
        else:
            print(
                f'ゲーム{game}は引き分けです　{first_name} {first_score}-{second_score} {second_name}'
            )
    game += 1

if first_score >= 21:
    print(f'このマッチは{first_name}の勝ちです　{first_name} 21-{second_score} {second_name}')
elif second_score >= 21:
    print(f'このマッチは{second_name}の勝ちです　{first_name} {first_score}-21 {second_name}')
elif game > 6:
    if first_score > second_score:
        print(
            f'このマッチは{first_name}の勝ちです　{first_name} {first_score}-{second_score} {second_name}'
        )
    elif first_score < second_score:
        print(
            f'このマッチは{second_name}の勝ちです　{first_name} {first_score}-{second_score} {second_name}'
        )
    elif first_score == second_score:
        print(
            f'このマッチは引き分けです　{first_name} {first_score}-{second_score} {second_name}')
