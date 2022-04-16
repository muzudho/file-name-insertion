import sys
from fs_operation import input_directory, input_is_right_directory, input_was_there_match, \
    list_name_matched_files
from this_operation import input_file_name_pattern, simulate_replace, replace_file_names, \
    input_type_str, input_string_format, \
    input_do_you_want_to_run_it

# 日本のWindows は "cp932" なので、Unicodeに変換
sys.stdout.reconfigure(encoding='utf-8')


# ディレクトリー選択
while True:
    # どのディレクトリーですか？
    files = input_directory()

    # このディレクトリーで合っていますか？
    is_right_directory = input_is_right_directory()

    if is_right_directory:
        break
    else:
        print("Canceld")


# 正規表現のパターンを入力してください
while True:
    # ファイル名パターンの入力
    pattern = input_file_name_pattern()

    # パターンに一致したファイル名の一覧
    list_name_matched_files(files, pattern)

    # マッチしましたか？
    is_match = input_was_there_match()

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
    is_yes = input_do_you_want_to_run_it()

    if is_yes:
        break
    else:
        print("Canceld")
        exit()


# 置換実行
replace_file_names(files, pattern, typeStr, formatStr)
