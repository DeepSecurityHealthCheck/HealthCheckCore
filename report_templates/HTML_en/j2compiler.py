from jinja2 import Template, Environment, FileSystemLoader, PackageLoader
import os


def main():
    jinja_env = Environment(loader=FileSystemLoader('./'))

    file = "base.html.j2"

    template = jinja_env.get_template(file)
    rendered_html = template.render()

    out = open('compiled.html', 'w')
    out.write(rendered_html)
    out.close()

    print("Compiled!")
    os.system('php TO_PDF.php')

if __name__ == '__main__':
    main()
