import os

def generate_post (txt_file_name):
    with open("raw_posts/" + txt_file_name) as f:
        lines = f.readlines()

        html_file_name = txt_file_name.split(".")[0] + ".html"

        title = lines[0]
        content = lines[1:]

        if os.path.exists("generated_posts/" + html_file_name):
            os.remove("generated_posts/" + html_file_name)

        with open("generated_posts/" + html_file_name, "w") as new_page:
            new_page.write("<a href=\"../index.html\">Back</a>")
            new_page.write("<h2>" + title + "</h2>")
            new_page.writelines(content)
        
    return [html_file_name, title, content]

def main ():
    if os.path.exists("index.html"):
        os.remove("index.html")

    posts = os.listdir("raw_posts")
    post_data = []

    for x in posts:
        post_data.append(generate_post(x))

    with open("index.html", "w") as home_page:
        home_page.write("<h1>Blog</h1></br>")
        home_page.write("<ul>")
        for post in post_data:
            home_page.write("<li><a href=\"generated_posts/" + post[0] + "\">" + post[1] + "</a></li>")
        home_page.write("</ul>")

main()
