import os


def save_article(content, root_dir, article_id):
    """Lưu nội dung bài viết vào file."""
    os.makedirs(root_dir, exist_ok=True)
    article_filename = f'article_{article_id:05d}.txt'
    article_savepath = os.path.join(root_dir, article_filename)

    with open(article_savepath, 'w', encoding='utf-8') as f:
        f.write(content)
