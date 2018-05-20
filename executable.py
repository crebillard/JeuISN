import sys
from cx_Freeze import setup, Executable
  
executables = [
        Executable("principale.py"),
        Executable("fonctions_jeu.py"),
        Executable("jeu1.py"),
        Executable("jeu2.py"),
        Executable("menu.py"),
        Executable("menupause.py"),
        Executable("menuperdu.py"),
        Executable("menuson.py"),
        Executable("notice.py"),      
        Executable("score1.py")
]
 
buildOptions = dict(
compressed = True,
include_files=["Abra.png","Dracaufeu.png","fond1.jpg","fond2.jpg","fond3.jpg","perso.png","perso1.png","Pokeball.png","Raichu.png","Tortank.png","vague 1.jpg","vague 2.jpg","vague 3.jpg","vie.jpg","bruit pas.wav","coin.wav","jeu.wav","vague.wav","arcade.ttf","Bungee-Regular.ttf","score1.txt","score2.txt","notice.txt"],
includes=["pygame"],
excludes=[],
packages=[],
path = sys.path + ["modules"]
)
         
  
setup(
    name = "Pocket Monster Runner",
    version = "1.0",
    description = "executable",
    options = dict(build_exe = buildOptions),
    executables = executables
)
