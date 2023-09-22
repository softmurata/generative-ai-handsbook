# generative-ai-handsbook

## Summary

- investigation
    - なんでも試したやつを入れとくやつ
- notebooks
    - investigationの中からいいと思ったやつを移してまとめておくやつ
- spaces
    - notebooksで動かせなそうなものに関して、その動かし方のDocsを準備したもの
    - imagesにテストデータを格納、もしくはデータの準備方法をDocsに記載
- application
    - notebooksの中で面白いと思ったものを利用してアプリケーションの形に落とし込んだやつ

## Usage

1. generate template
```
python3 scripts/generate_template.py --project_type investigation --project_name test
```

2. resize results or docs image
```
python scripts/resize_image.py --image_path investigation/fooocus/results/moden_living_room_japan_inpainting_and_outpainting.png
```

### Rule
- google colabのリンクは必ず全体共有する設定を行う。
- installation, demo data preparation, inference, anotherのような小分けを必ず入れる
- 結果とかの表示は全て消す
- 必ずgoogle colabのリンクを貼ったらgit pull