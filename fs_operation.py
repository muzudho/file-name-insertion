# File system operation

import os
import glob
import re
import sys
from datetime import datetime


def input_directory():
    """どのディレクトリーですか？"""
    print("""Which directory?
Example: .""")

    path = input()

    # カレントディレクトリを移動
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

    return files


def input_file_name_pattern(files):
    """ファイル名パターンの入力"""
    print(r"""
Please enter a regular expression pattern. Left and Rignt groups. Insert to center.
Example: ^(example-)(?:.*)(-banana.txt)$""")

    patternText = input()

    pattern = re.compile(patternText)

    print(r"""
Numbering
---------""")

    return pattern


def list_name_matched_files(files, pattern):
    """パターンに一致したファイル名の一覧"""
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
