from PIL import Image
import os
import time

# 圧縮したい画像が保存されているフォルダパスを指定
file_path = "C:\\Users\\03kaz\\Program\\講義課題\\情報数学応用\\中間レポート\\img_befor"

# 圧縮後の画像を保存したいフォルダパスを指定
save_file_path = "C:\\Users\\03kaz\\Program\\講義課題\\情報数学応用\\中間レポート\\img_comp"

# 使用する保存フォーマットを選択（pngまたはjpg）
while True:
    save_format = input("保存するフォーマットを選択してください（png または jpg と入力）: ").lower()
    if save_format in ["png", "jpg"]:
        break
    print("入力が正しくありません。'png' または 'jpg' を選択してください。")

# 圧縮レベルの設定
if save_format == "png":
    compression_color_num = 90  # 色数は固定
    compress_levels = list(range(0, 10))  # PNGの圧縮レベルを0-9で設定

elif save_format == "jpg":
    compress_levels = list(range(0, 91, 10))  # JPGの圧縮率を0から90まで10刻みで設定

# 圧縮処理を各レベルで10回行う
for compress_level in compress_levels:
    for i in range(10):
        start = time.time()  # 処理開始時間の記録

        # 圧縮したい画像の各ファイル名をリストで取得
        filename_pic_list = os.listdir(file_path)

        # 画像ファイルごとに処理を実行
        for filename_pic in filename_pic_list:
            # 圧縮したい画像の読み込み
            img = Image.open(os.path.join(file_path, filename_pic))

            # ファイル名と拡張子名を分割
            file, ext = os.path.splitext(filename_pic)

            # 保存形式に応じた処理を実行
            if save_format == "png":
                # パレットモードで画像の色を制限
                img = img.convert("P", palette=Image.ADAPTIVE, colors=compression_color_num)
                # 圧縮レベルを指定して保存
                img.save(
                    os.path.join(save_file_path, f"{file}_comp_PNG_level{compress_level}_try{i+1}.png"),
                    format="PNG",
                    optimize=True,
                    compress_level=compress_level
                )

            elif save_format == "jpg":
                # jpgはRGBモードで保存
                img = img.convert("RGB")
                img.save(
                    os.path.join(save_file_path, f"{file}_comp_JPG_quality{compress_level}_try{i+1}.jpg"),
                    format="JPEG",
                    optimize=True,
                    quality=compress_level
                )

        end = time.time()  # 処理終了時間の記録
        print("\n圧縮処理が完了しました。")
        print(f"圧縮レベル {compress_level} - {i + 1} 回目処理時間：", end - start)

print("\nーー実験終了ーー")