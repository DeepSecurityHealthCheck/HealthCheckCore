from jinja2 import Template, Environment, FileSystemLoader





def main():
	jinja_env = Environment(loader = FileSystemLoader(os.path.abspath('./report_templates/HTML')))
    file = "base.html"
    template = jinja_env.get_template(file)
    rendered_html = template.render()

    out = open('compiled.html', 'w')
    out.write(rendered_html)
    out.close()

    print("Compiled!")


if __name__ == '__main__':
    main()
