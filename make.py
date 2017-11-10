import subprocess
from pathlib import Path

p = Path(__file__).parent
print(f"Running make.py on {str(p)}")
tex_files = p.glob("*.tex")
for tex_file in tex_files:
    print(f"Found {str(tex_file)} - compiling it!")
    aux_file = p / f"{tex_file.stem}.aux"
    commands = [["pdflatex.exe", str(tex_file)],
                ["bibtex.exe", str(aux_file)],
                ["pdflatex.exe", str(tex_file)],
                ["pdflatex.exe", str(tex_file)]]
    for command in commands:
        subprocess.run(command)
