import mammoth
import sys

docx_file = sys.argv[1]
md_file = sys.argv[2]

custom_styles = "\n\n => \n&nbsp;\n "

with open(docx_file, "rb") as docx_file:
    result = mammoth.convert_to_markdown(docx_file, style_map=custom_styles,
                                     ignore_empty_paragraphs=False)
    text = result.value

    with open("test.md", "w") as text_file:
        text_file.write(text)


pre = False
lines = []
with open(md_file, "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        if pre and lines[i-1] == '\n' and line == '\n':
            lines[i] = ('&nbsp;\n')
            pre = False
            continue

        if line == '\n':
            pre = True

with open("test.md", "w") as file:
    for line in lines:
        file.write(line)
