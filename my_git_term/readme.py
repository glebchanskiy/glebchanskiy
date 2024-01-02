
def gen(): 
    dark_image_url="https://i.ibb.co/gdS6Fj0/output_dark.gif"
    light_image_url="https://i.ibb.co/gdS6Fj0/output_light.gif"
    readme_file_content = rf"""<div align="justify">
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="{dark_image_url}">
    <source media="(prefers-color-scheme: light)" srcset="{light_image_url}">
    <img alt="GIFOS" src="{dark_image_url}">
</picture>
</div>
"""
    with open("README.md", "w") as fp:
        fp.write(readme_file_content)
        print("INFO: README.md file generated")

if __name__ == "__main__":
    gen()
