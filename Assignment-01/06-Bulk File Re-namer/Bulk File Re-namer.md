# 🐍 Bulk File Re-namer - Python Project

## 📌 Problem Statement
Manually renaming a large number of files can be time-consuming and error-prone. This **Python project** provides a solution by automatically renaming all the files in a given folder with a consistent base name and sequence number.

---

## 🎯 Features
- Rename all files in a specified folder.
- Add a base name (e.g., `photo`, `file`, `doc`).
- Auto-number files (e.g., `photo_1.jpg`, `photo_2.jpg`, etc.).
- Supports all file types.
- Simple and safe to use.

---

## 🛠️ How It Works
1. The user provides a **folder path** containing files.
2. The user enters a **base name** (e.g., `holiday`, `image`, etc.).
3. The program renames each file to match the format: `baseName_index.extension`
4. Files are renamed in sorted order to maintain consistency.

---

## 🖥️ Code Implementation
```python
import os

def bulk_rename(folder_path, base_name):
    try:
        files = os.listdir(folder_path)
        files.sort()  # Sort files alphabetically

        for index, file_name in enumerate(files, start=1):
            file_path = os.path.join(folder_path, file_name)

            if os.path.isfile(file_path):
                file_ext = os.path.splitext(file_name)[1]  # get file extension
                new_name = f"{base_name}_{index}{file_ext}"
                new_path = os.path.join(folder_path, new_name)
                os.rename(file_path, new_path)

        print("✅ Files renamed successfully!")

    except FileNotFoundError:
        print("❌ The specified folder was not found.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    folder = input("📂 Enter folder path: ")
    name = input("📝 Enter base name for files: ")
    bulk_rename(folder, name)
```

---

## 🧪 Example Output
```
📂 Enter folder path: C:\\Users\\YourName\\Desktop\\MyImages
📝 Enter base name for files: image

Before:
  - DSC_001.jpg
  - DSC_002.jpg

After:
  - image_1.jpg
  - image_2.jpg
```

---

## 🔐 Important Notes
- This operation is **permanent**. Test on a backup folder before using on important files.
- All files in the folder will be renamed (excluding subfolders).

---

## 🔗 Google Colab Notebook
Run it online using Google Colab:
[👉 Open in Google Colab](https://colab.research.google.com/drive/1EbZ4n2bjdVP_dI95EYiakUk9Oe9hWM6z?usp=sharing)

---

🚀 **Organize your files with ease!**

