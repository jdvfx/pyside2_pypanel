
# create Python Panel inside Houdini20.5

requirements:

- linux
- pyside2-uic
- designer-qt5
- houdini20.5

// in this example, the panel is named: "my_pythonpanel"

1) create a directory in your project files:
eg: /home/houdini_tools/my_pythonpanel

2) create a "packages" directory and a .json inside
this updates $HOUDINI_PATH and add our houdini_tools directory

mkdir ~/houdini20.5/packages/my_pythonpanel.json
{
    "env": [
        {
            "HOUDINI_PATH": {
                "value": "$HOME/houdini_tools",
                "method": "append"
            }
        }
    ],
    "process_order" : 3
}



