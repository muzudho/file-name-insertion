import os
import sys
from datetime import datetime


def input_type_str():
    # 挿入する型を入力してください
    print("""
    Enter the insertion parameter type.
    Example: file-modified-day""")

    typeStr = input()

    print(f"""
    Parameter type
    --------------
    {typeStr}""")

    return typeStr


def input_string_format():
    """文字列フォーマットを入力してください"""
    print("""
    Enter the string format.
    Example: {0}{2}{1}""")

    formatStr = input()

    print(f"""
    Format string
    -------------
    {formatStr}""")

    return formatStr


def get_center(typeStr, file):
    if typeStr == "file-creation-year":
        tick = os.path.getctime(file)
        return datetime.fromtimestamp(tick).strftime('%Y')

    elif typeStr == "file-creation-month":
        tick = os.path.getctime(file)
        return datetime.fromtimestamp(tick).strftime('%m')

    elif typeStr == "file-creation-day":
        tick = os.path.getctime(file)
        return datetime.fromtimestamp(tick).strftime('%d')

    elif typeStr == "file-modified-year":
        tick = os.path.getmtime(file)
        return datetime.fromtimestamp(tick).strftime('%Y')

    elif typeStr == "file-modified-month":
        tick = os.path.getmtime(file)
        return datetime.fromtimestamp(tick).strftime('%m')

    elif typeStr == "file-modified-day":
        tick = os.path.getmtime(file)
        return datetime.fromtimestamp(tick).strftime('%d')

    elif typeStr == "digit":
        return "#digit#"

    else:
        return "#type-failed#"


def simulate_replace(files, pattern, typeStr, formatStr):
    """置換のシミュレーション"""
    print("""
    Simulation
    ----------""")

    countOfSimulation = 0

    for i, file in enumerate(files):
        center = get_center(typeStr, file)
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
            replaced = formatStr.format(left, right, center)

            print(f"({i+1}) {basename} --> {replaced}")
            countOfSimulation += 1

        else:
            # Unmatched
            pass

    print(f"""
    Count of simulation = {countOfSimulation}""")


def replace_file_names(files, pattern, typeStr, formatStr):
    """置換実行"""
    print("""
    Result
    ------""")

    # 置換実行
    for i, file in enumerate(files):
        center = get_center(typeStr, file)
        basename = os.path.basename(file)
        result = pattern.match(basename)
        if result:
            # Matched

            left = result.group(1)
            right = result.group(2)
            replaced = formatStr.format(left, right, center)

            oldPath = os.path.join(os.getcwd(), basename)
            newPath = os.path.join(os.getcwd(), replaced)
            print(f"({i})Rename {oldPath} --> {newPath}")
            os.rename(oldPath, newPath)


def input_was_there_match():
    """マッチしましたか？"""
    print("""
Was there a match (y/n)?""")

    answer = input()

    return answer == "y"


def input_do_you_want_to_run_it():
    print("""
    Do you want to run it (y/n)?""")

    answer = input()

    return answer == "y"


def input_is_right_directory():
    """このディレクトリーで合っていますか？"""
    print("""
Are you sure this is the right directory (y/n)?""")

    answer = input()

    return answer == "y"
