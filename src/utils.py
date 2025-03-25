"""
Utility functions for working with text data and files.
"""
import os

def save_article(content, root_dir, article_id):
    """
    Save an article's content to a text file in the specified directory.

    This function ensures that the target directory exists, then creates a text file 
    with a structured filename based on the provided article ID. The content is 
    saved in UTF-8 encoding to support a wide range of characters.

    Args:
        content (str): The text content of the article to be saved.
        root_dir (str): The directory where the article should be stored.
        article_id (int): A unique identifier for the article, used to generate the filename.

    Returns:
        str: The full path of the saved article file.

    Behavior:
        - If the `root_dir` does not exist, it is created automatically.
        - The filename follows the format `article_00001.txt`, ensuring numerical sorting.
        - The file is written in UTF-8 encoding to support international characters.

    Example:
        >>> save_path = save_article("This is an article.", "articles", 1)
        >>> print(f"Article saved at: {save_path}")

    Raises:
        OSError: If there is an issue creating the directory or writing to the file.
    """
    os.makedirs(root_dir, exist_ok=True)
    article_filename = f'article_{article_id:05d}.txt'
    article_savepath = os.path.join(root_dir, article_filename)

    with open(article_savepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return article_savepath
