import os
import glob
import re
import sys
from datetime import datetime

# 日本のWindows は "cp932" なので、Unicodeに変換
sys.stdout.reconfigure(encoding='utf-8')

# ディレクトリーを選んでください
while True:
    print("""Which directory?
Example: .""")

    path = input()
    os.chdir(path)

    # フィル名を一覧します
    print(f"""Current directory: {os.getcwd()}

Files
-----""")

    files = glob.glob("./*")

    # とりあえず一覧します
    for file in files:
        basename = os.path.basename(file)
        print(basename)

    print("""
Are you sure this is the right directory (y/n)?""")

    answer = input()

    if answer == "y":
        break
    else:
        print("Canceld")

# 正規表現のパターンを入力してください
while True:
    print(r"""
Please enter a regular expression pattern. Left and Rignt groups. Insert to center.
Example: ^(example-)(?:.*)(-banana.txt)$""")

    patternText = input()
    pattern = re.compile(patternText)

    print(r"""
Numbering
---------""")

    # とりあえず一覧します
    for i, file in enumerate(files):
        basename = os.path.basename(file)
        result = pattern.match(basename)
        if result:
            # Matched
            # グループ数
            groupCount = len(result.groups())
            buf = f"({i+1}) {basename}"
            for j in range(0, groupCount):
                buf += f" \\{j+1}=[{result.group(j+1)}]"
            print(buf)
        else:
            # Unmatched
            print(f"( ) {basename}")

    print("""
Was there a match (y/n)?""")

    answer = input()

    if answer == "y":
        break
    else:
        print("Canceld")

# 挿入する型を入力してください
while True:

    print(r"""
Enter the insertion parameter type.
Example: file-modified-day""")

    typeStr = input()

    print(f"""
Parameter type
--------------
{typeStr}

Parameter value
---------------""")

    if typeStr == "file-creation-year":
        tick = os.path.getctime(file)
        center = datetime.fromtimestamp(tick).strftime('%Y')

    elif typeStr == "file-creation-month":
        tick = os.path.getctime(file)
        center = datetime.fromtimestamp(tick).strftime('%m')

    elif typeStr == "file-creation-day":
        tick = os.path.getctime(file)
        center = datetime.fromtimestamp(tick).strftime('%d')

    elif typeStr == "file-modified-year":
        tick = os.path.getmtime(file)
        center = datetime.fromtimestamp(tick).strftime('%Y')

    elif typeStr == "file-modified-month":
        tick = os.path.getmtime(file)
        center = datetime.fromtimestamp(tick).strftime('%m')

    elif typeStr == "file-modified-day":
        tick = os.path.getmtime(file)
        center = datetime.fromtimestamp(tick).strftime('%d')

    elif typeStr == "digit":
        center = "#digit#"

    else:
        center = "#type-failed#"

    print(f"{center}")

    print("""
Ok (y/n)?""")

    answer = input()

    if answer == "y":
        break
    else:
        print("Canceld")


# 置換のシミュレーション
print("""
Simulation
----------""")

countOfSimulation = 0

for i, file in enumerate(files):
    basename = os.path.basename(file)
    result = pattern.match(basename)
    if result:
        # Matched
        # グループ数は２
        groupCount = len(result.groups())
        buf = f"({i+1}) {basename}"
        isUnmatched = False

        left = result.group(1)
        right = result.group(2)

        print(f"({i+1})Rename {basename} --> {left}{center}{right}")
        countOfSimulation += 1

    else:
        # Unmatched
        pass

print(f"""
Count of simulation = {countOfSimulation}""")

print(f"WIP")
