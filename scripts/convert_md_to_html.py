#!/usr/bin/env python3
"""
Simple markdown to HTML converter for our small docs.
Converts headings, unordered lists and paragraphs.
"""
import sys
import re
from pathlib import Path


def md_to_html(text):
    html_lines = []
    lines = text.splitlines()
    in_list = False
    for line in lines:
        line = line.rstrip()
        if not line:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append('<p></p>')
            continue

        h1 = re.match(r'^# (.*)', line)
        h2 = re.match(r'^## (.*)', line)
        h3 = re.match(r'^### (.*)', line)
        li = re.match(r'^- (.*)', line)
        if h1:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(f'<h1>{h1.group(1).strip()}</h1>')
        elif h2:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(f'<h2>{h2.group(1).strip()}</h2>')
        elif h3:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(f'<h3>{h3.group(1).strip()}</h3>')
        elif li:
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            html_lines.append(f'  <li>{li.group(1).strip()}</li>')
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            # wrap as paragraph
            html_lines.append(f'<p>{line}</p>')

    if in_list:
        html_lines.append('</ul>')

    return '\n'.join(html_lines)


def write_html(md_path: Path, html_path: Path):
    md = md_path.read_text(encoding='utf-8')
    body = md_to_html(md)
    title = md.splitlines()[0].lstrip('# ').strip() if md else 'Document'
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    body {{ font-family: -apple-system,BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; max-width: 900px; margin: 40px auto; line-height: 1.6; color: #222; padding: 0 16px; }}
    h1 {{ font-size: 28px; margin-top: 24px; }}
    h2 {{ font-size: 22px; margin-top: 18px; }}
    h3 {{ font-size: 18px; margin-top: 12px; }}
    p {{ margin: 8px 0; }}
    ul {{ margin: 8px 0 8px 24px; }}
  </style>
</head>
<body>
{body}
</body>
</html>'''
    html_path.write_text(html, encoding='utf-8')


def main():
    # the docs live in the parent of this scripts folder (i.e. docs/)
    base = Path(__file__).parent.parent
    files = ['privacy-policy.md', 'terms-of-service.md']
    for f in files:
        mdp = base / f
        if mdp.exists():
            htmlp = base / f.replace('.md', '.html')
            print(f'Converting {mdp} -> {htmlp}')
            write_html(mdp, htmlp)
        else:
            print(f'Missing: {mdp}', file=sys.stderr)


if __name__ == '__main__':
    main()

