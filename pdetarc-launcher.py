# https://github.com/bero-sim/pdetarc-docker-app/blob/main/pdetarc-launcher.py
import subprocess
import os
import sys

def main():
    print("==== PDETARC DOCKER DROPLET START ====")

    # 引数（ドラッグ＆ドロップされたファイル）の取得
    if len(sys.argv) < 2:
        print("[ERROR] No input provided")
        input("\nPress Enter to exit...")
        sys.exit(1)

    input_path = os.path.abspath(sys.argv[1])
    directory = os.path.dirname(input_path)
    filename = os.path.basename(input_path)

    print(f"Input: {input_path}")
    print(f"Dir  : {directory}")
    print(f"Name : {filename}")
    print("Running Docker...")

    # Dockerコマンドの構築
    # -v "ディレクトリ":/work
    docker_command = [
        "docker", "run", "--rm",
        "-v", f"{directory}:/work",
        "-w", "/work",
        "pdetarc",
        filename
    ]

    try:
        # コマンドの実行
        result = subprocess.run(docker_command, shell=True)
        print(f"\n==== RETURN CODE: {result.returncode} ====")
    except Exception as e:
        print(f"\n[ERROR] Failed to run Docker: {e}")

    print("==== PDETARC DOCKER DROPLET END ====")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
