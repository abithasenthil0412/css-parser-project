import json
from pathlib import Path
import tinycss2

def parse_css(file_path):
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    css_text = path.read_text(encoding="utf-8")

    rules = tinycss2.parse_stylesheet(
        css_text,
        skip_comments=True,
        skip_whitespace=True
    )

    results = []

    for rule in rules:
        if rule.type != "qualified-rule":
            continue

        selector = tinycss2.serialize(rule.prelude).strip()
        declarations = tinycss2.parse_declaration_list(
            rule.content,
            skip_comments=True,
            skip_whitespace=True
        )

        properties = {}

        for item in declarations:
            if item.type == "declaration":
                properties[item.name] = (
                    tinycss2.serialize(item.value).strip()
                )

        results.append({
            "selector": selector,
            "properties": properties
        })

    return results


if __name__ == "__main__":
    try:
        output = parse_css("sample.css")
        print(json.dumps(output, indent=4))
    except (OSError, ValueError) as error:
        print(f"Error: {error}")