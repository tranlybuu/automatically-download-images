import os

def setup_folder():
    """
        Hàm này để kiểm tra thư mục chứa dữ liệu đã tồn tại hay chưa. Nếu chưa tồn tại thì tạo thư mục DATA
        Biến PATH chính là đường dẫn thư mục. Bạn có thể thay đổi đường dẫn bằng cách copy đường dẫn đến thư mục và thay thế None
        Nếu PATH = None thì thư mục sẽ được mặc định chính là thư mục đang chứa code này
        ---
        This function to check the directory containing the data already exists or not. If it does not exist, create a DATA folder
        The PATH variable is the directory path. You can change the path by copying the path to the directory and replacing None
        If PATH = None, the directory will default to the directory containing this code
    """
    path = "None"
    
    if path == "None":
        path = os.getcwd()
    os.chdir(path)
    all_folders = os.listdir(path)
    if 'DATA' not in all_folders:
        os.mkdir('DATA')
        print(f"\n- Created DATA directory at {path}-\n")
    else:
        print(f"\n- DATA directory already exists at {path}-\n")
    return path

def create_keyword_folder(path, keyword):
    """
        Hàm này để tạo thư mục với tên thư mục chính là keyword.
        ---
        This function to create a folder with the main folder name as keyword.
    """
    path = path + "\\DATA"
    os.chdir(path)
    try:
        os.mkdir(keyword)
        return path
    except:
        return False
        