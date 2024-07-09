## About
 - FTPでファイルサーバーからファイルを取ってくる
 - 取ってきたファイルをInpaintする

## Run
 - ファイル取得 <br>
 docker compose run ftp_downloader sync_files
 - ファイル変換・Inpainting処理 <br>
 docker compose run ftp_downloader inpainting

## Links