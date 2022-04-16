import os
import sys
from fs_operation import input_change_current_directory, list_current_directory_files, \
    input_is_right_directory, input_y, \
    list_name_matched_files
from this_operation import input_re_pattern, simulate_replace, replace_file_names, \
    input_type_str, input_string_format, input_y

# 日本のWindows は "cp932" なので、Unicodeに変換
sys.stdout.reconfigure(encoding='utf-8')


# ディレクトリー選択
while True:
    # どのディレクトリーですか？
    input_change_current_directory("""Which directory?
Example: .""")

    print(f"Current directory: {os.getcwd()}")

    # カレント ディレクトリーのファイルを一覧します
    files = list_current_directory_files()

    # このディレクトリーで合っていますか？
    is_right_directory = input_is_right_directory()

    if is_right_directory:
        break
    else:
        print("Canceld")


# 正規表現のパターンを入力してください
while True:
    # ファイル名パターンの入力
    pattern = input_re_pattern(r"""
Please enter a regular expression pattern. Left and Rignt groups. Insert to center.
Example: ^(example-)(?:.*)(-banana.txt)$""")

    # パターンに一致したファイル名の一覧
    list_name_matched_files(files, pattern)

    # マッチしましたか？
    is_match = input_y("""
Was there a match (y/n)?""")

    if is_match:
        break
    else:
        print("Canceld")

while True:
    # 挿入する型を入力してください
    typeStr = input_type_str()

    # 文字列フォーマットを入力してください
    formatStr = input_string_format()

    # 置換のシミュレーション
    simulate_replace(files, pattern, typeStr, formatStr)

    # 実行しますか？ (y/n)
    is_yes = input_y("""
Do you want to run it (y/n)?""")

    if is_yes:
        break
    else:
        print("Canceld")
        exit()


# 置換実行
replace_file_names(files, pattern, typeStr, formatStr)
