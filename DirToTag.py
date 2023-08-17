import os

def generate_tag(file_path, tag_path):
    parts = os.path.normpath(file_path).split(os.path.sep)
    index = parts.index(tag_path)
    tag_parts = parts[index:-1]  # Exclude filename and last folder
    tag = "#" + "/".join(tag_parts)
    return tag.replace(" ", "_").replace("-", "_")  # Replace spaces and special characters

def tag_already_exists(file_path, tag):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines[:3]:
        line_tags = line.strip().split()
        if tag in line_tags:
            return True

    return False

def process_markdown_file(file_path, tag, counters):
    if tag_already_exists(file_path, tag):
        counters['skipped'] += 1
        return

    try:
        with open(file_path, 'r') as file:
            content = file.read()

        if not content.lstrip().startswith("#"):
            new_content = f"{tag}\n\n{content}"
        elif content.lstrip().startswith("##") or content.lstrip().startswith("# "):
            new_content = f"{tag}\n\n{content}"
        else:
            new_content = f"{tag} {content}"

        with open(file_path, 'w') as file:
            file.write(new_content)

        counters['added'] += 1
    except FileNotFoundError as e:
        print(f"Error: {e}")

def main():
    file_path = input("Enter the file path: ").strip()  # Remove leading/trailing spaces
    tag_path = os.path.basename(file_path)
    counters = {'added': 0, 'skipped': 0}

    for root, dirs, files in os.walk(file_path):
        for file_name in files:
            if file_name.endswith(".md"):
                file_path = os.path.join(root, file_name)
                tag = generate_tag(file_path, tag_path)
                process_markdown_file(file_path, tag, counters)

    print(f"Tag added: {counters['added']}")
    print(f"Tag exists, skipped: {counters['skipped']}")

if __name__ == "__main__":
    main()
