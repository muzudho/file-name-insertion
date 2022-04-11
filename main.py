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
Example: ^(example-)(?:.*)(-banana.png)$""")

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

# 挿入する型
print(r"""
Enter the insertion parameter type.
Example: file-modified-day""")

parameterType = input()

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
        for j in range(0, groupCount):

            value = result.group(j+1)
            typeStr = typeTable[f"{j+1}"]

            if typeStr == "file-creation-year":
                tick = os.path.getctime(file)
                expected = datetime.fromtimestamp(tick).strftime('%Y')
                # print(f"file={file} value={value} year={expected}")
                if value != expected:
                    isUnmatched = True

            elif typeStr == "file-creation-month":
                tick = os.path.getctime(file)
                expected = datetime.fromtimestamp(tick).strftime('%m')
                # print(f"file={file} value={value} month={expected}")
                if value != expected:
                    isUnmatched = True

            elif typeStr == "file-creation-day":
                tick = os.path.getctime(file)
                expected = datetime.fromtimestamp(tick).strftime('%d')
                # print(f"file={file} value={value} day={expected}")
                if value != expected:
                    isUnmatched = True

            elif typeStr == "file-modified-year":
                tick = os.path.getmtime(file)
                expected = datetime.fromtimestamp(tick).strftime('%Y')
                if value != expected:
                    isUnmatched = True

            elif typeStr == "file-modified-month":
                tick = os.path.getmtime(file)
                expected = datetime.fromtimestamp(tick).strftime('%m')
                if value != expected:
                    isUnmatched = True

            elif typeStr == "file-modified-day":
                tick = os.path.getmtime(file)
                expected = datetime.fromtimestamp(tick).strftime('%d')
                if value != expected:
                    isUnmatched = True

            elif typeStr == "digit":
                expected = "#digit#"
                if not value.isdigit():
                    isUnmatched = True

            else:
                expected = "#type-failed#"

            buf += f" \\{j+1}=[{value}][{expected}]"

        if isUnmatched:
            print(buf)
            countOfSimulation += 1
    else:
        # Unmatched
        print(f"({i+1}) {basename}")
        countOfSimulation += 1

print(f"Count of simulation = {countOfSimulation}")
