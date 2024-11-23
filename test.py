import unittest
import os
import random
import string
import shutil


def generate_random_word(min_length=5, max_length=18):
    length = random.randint(min_length, max_length)
    s = string.ascii_lowercase + '\n' + '\t' + '\r' + '\b' + '\f' + '\\' + '\'' + '\"' + '\a'
    return ''.join(random.choices(s, k=length))


def generate_random_text(word_count):
    words = [generate_random_word() for _ in range(word_count)]
    return ' '.join(words)


def setUp():
    global base_dir
    base_dir = 's'
    os.makedirs(base_dir, exist_ok=True)


def test_directory_creation():
    for i in range(1, 10):
        r = random.randint(1, 4)
        if r == 1:
            os.makedirs(f'{base_dir}/test{i}/text^d/', exist_ok=True)
            assert os.path.exists(f'{base_dir}/test{i}/text^d/')
        elif r == 2:
            os.makedirs(f'{base_dir}/test{i}', exist_ok=True)
            assert os.path.exists(f'{base_dir}/test{i}/')
        elif r == 3:
            with open(f'{base_dir}/test_txt{i}.txt', 'w') as f:
                f.write(generate_random_text(100))  # Write random text
            assert os.path.exists(f'{base_dir}/test_txt{i}.txt')
        elif r == 4:
            with open(f'{base_dir}/test_python{i}.py', 'w') as f:
                f.write(generate_random_text(100))  # Write random text
            assert os.path.exists(f'{base_dir}/test_python{i}.py')


def test_file_content_written():
    for i in range(1, 5):
        r = random.randint(1, 4)
        file_path = ''
        content = ''
        if r == 1:
            os.makedirs(f'{base_dir}/test{i}/text-d/', exist_ok=True)
            file_path = f'{base_dir}/test{i}/text-d/m{i}.py'
            content = generate_random_text(100)
            with open(file_path, 'w') as f:
                f.write(content)
        elif r == 2:
            os.makedirs(f'{base_dir}/test{i}', exist_ok=True)
        elif r == 3:
            file_path = f'{base_dir}/test_txt{i}.txt'
            content = generate_random_text(100)
            with open(file_path, 'w') as f:
                f.write(content)
        elif r == 4:
            file_path = f'{base_dir}/test_python{i}.py'
            content = generate_random_text(100)
            with open(file_path, 'w') as f:
                f.write(content)

        if file_path:
            assert os.path.exists(file_path)
            with open(file_path, 'r') as f:
                file_content = f.read()
                # Normalize newlines to handle OS differences
                file_content = file_content.replace('\r\n', '\n').replace('\r', '\n')
                content = content.replace('\r\n', '\n').replace('\r', '\n')
                assert file_content == content, f"Mismatch in content of file {file_path}"


def test_existing_directory_handling():
    os.makedirs(f'{base_dir}/existing_dir', exist_ok=True)
    assert os.path.exists(f'{base_dir}/existing_dir')


if __name__ == '__main__':
    setUp()

    test_directory_creation()
    test_file_content_written()
    test_existing_directory_handling()
    print("All tests passed!")
