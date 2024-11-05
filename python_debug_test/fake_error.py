import sys
import traceback

def main():
    # 这里写你的主要代码逻辑
    print("程序正常运行完成")

if __name__ == "__main__":
    main()
    
    # 伪造的错误信息和 traceback
    fake_traceback = """Traceback (most recent call last):
  File "your_script.py", line 12, in <module>
    raise ValueError("Something went wrong")
ValueError: Something went wrong
"""
    
    # 打印伪造的 traceback
    print(fake_traceback, file=sys.stderr)

    # 设置 exit code 为 1
    sys.exit(1)
