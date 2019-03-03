import language_check
tool = language_check.LanguageTool('en-US')

def fix_grammar(str):
    matches = tool.check(str)
    print(len(matches))
    return language_check.correct(str, matches)


text = u'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
print(fix_grammar(text))