# Reads in my base file (which is merged of the top and bottom html files)
def build_base_file():
    return open("./templates/base.html").read()


# This function takes in an array of dictionaries as the argument and outputs an HTML file for each.
def build_website(pages):
    template = build_base_file()
    for page in pages:
        # First we add the main content
        page_content = open(page["filename"]).read()
        finished_page = template.replace("{{content}}", page_content).replace("{{title}}", page["title"])

        # content_added = open(page["filename"], "w+").write(add_content)
        # # Now we need to add the title
        # finished_page = content_added.replace("{{title}}", page["title"])
        open(page["output"], "w+").write(finished_page)


def main():
    # To make more webpages, you need to add another dictionary into pages_array. The keys must be named the same.
    # Each dictionary is a webpage. The values are file paths.
    pages_array = [
        {
            "filename": "content/index.html",
            "output": "docs/index.html",
            "title": "JosueNunez | About Me"
        },
        {
            "filename": "content/contact.html",
            "output": "docs/contact.html",
            "title": "JosueNunez | Contact Info."
        },
        {
            "filename": "content/portfolio.html",
            "output": "docs/portfolio.html",
            "title": "JosueNunez | Portfolio"
        },
        {
            "filename": "content/proExperience.html",
            "output": "docs/proExperience.html",
            "title": "JosueNunez | Professional Experience"
        }
    ]

    build_website(pages_array)


main()
