import sys
from fs_operation import input_directory, input_file_name_pattern
from this_operation import simulate_replace, replace_file_names

# 日本のWindows は "cp932" なので、Unicodeに変換
sys.stdout.reconfigure(encoding='utf-8')


# ディレクトリーを選んでください
while True:
    files = input_directory()

    print("""
Are you sure this is the right directory (y/n)?""")

    answer = input()

    if answer == "y":
        break
    else:
        print("Canceld")


# 正規表現のパターンを入力してください
while True:
    pattern = input_file_name_pattern(files)

    print("""
Was there a match (y/n)?""")

    answer = input()

    if answer == "y":
        break
    else:
        print("Canceld")

# 挿入する型を入力してください
print(r"""
Enter the insertion parameter type.
Example: file-modified-day""")

typeStr = input()

print(f"""
Parameter type
--------------
{typeStr}""")

# 文字列フォーマットを入力してください
print("""
Enter the string format.
Example: {0}{2}{1}""")

formatStr = input()

print(f"""
Format string
-------------
{formatStr}""")

# 置換のシミュレーション
simulate_replace(files, pattern, typeStr, formatStr)

print("""
Do you want to run it (y/n)?""")

answer = input()

if answer == "y":
    pass
else:
    print("Canceld")
    exit()


# 置換実行
replace_file_names(files, pattern, typeStr, formatStr)
