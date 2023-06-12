import cx_Freeze

executables = [
    cx_Freeze.Executable(script='Apygame.py', icon = 'flappybird.ico')
]

cx_Freeze.setup(
    name = "FlappyBird",
    options = {
        "build.exe":(
            "packages": ["pygame"],
            "include_files": [
                "background.png"
                "flappybird.png"
            ]
        )
    } , executables =  executables
)

#python gerasetup.py build
#python gerasetup.py bdist_msi