class MarkdownFormatter:

    def bold(self, text):
        return f"**{text}**"

    def italic(self, text):
        return f"*{text}*"

    def header(self, text, step):
        return f"{step * '#'} {text}"

    def bullet_list_item(self, text):
        return f"+ {text}"
