from jinja2 import Environment, PackageLoader, select_autoescape
import yaml
import shutil


env = Environment(
    loader=PackageLoader("src"),
    autoescape=select_autoescape()
)

template = env.get_template("index.html")

with open("src/data.yaml") as f:
    data = yaml.load(f.read(), Loader=yaml.Loader)
  
print(data[0]['file_name'])
rendered = template.render(data=data)

with open("dist/index.html", "w") as w:
    w.write(rendered)

