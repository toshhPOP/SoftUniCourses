article = input()
content = input()
title = "<h1></h1>"
content_tag = "<article></article>"
comments = "<div></div>"
title = [a for a in title]
content_tag = [a for a in content_tag]
comments = [a for a in comments]
print(f"{''.join(title[:len(title)//2])}\n    {article}\n{''.join(title[len(title)//2:])} ")
print(f"{''.join(content_tag[:len(content_tag)//2])}\n    {content}\n{''.join(content_tag[len(content_tag)//2:])}")
while True:
    command = input()
    if command == "end of comments":
        break
    print(f"{''.join(comments[:len(comments)//2])}\n    {command}\n{''.join(comments[len(comments)//2:])}")