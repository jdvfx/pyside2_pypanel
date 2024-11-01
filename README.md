# Create a Python Panel inside Houdini20.5

requirements:

- Linux
- Pyside2-uic
- QT designer 5
- Houdini 20.5

## in this example, the panel is named: "my_pythonpanel"

1) create a directory in your project files, eg:<br>
```
mkdir -p $HOME/houdini_tools/python3.11libs/my_pythonpanel
mkdir -p $HOME/houdini_tools/python_panels
```

```
$HOME/houdini_tools/
    + python3.11libs
        + my_pythonpanel
    + python_panels
        + my_pythonpanel.pypanel
```

3) create a "packages" directory and a .json inside<br>
this updates $HOUDINI_PATH and add our houdini_tools directory<b>

```
mkdir -p ~/houdini20.5/packages/
touch ~/houdini20.5/packages/my_pythonpanel.json
```
```
{
    "env": [
        {
            "HOUDINI_PATH": {
                "value": "$HOME/$houdini_tools/my_pythonpanel/",
                "method": "append"
            }
        }
    ],
    "process_order" : 3
}
```
4) create interface with QTDesigner5

5) save to .ui and convert to .py<br>
```pyside2-uic my_ui_file.ui my_ui_file.py```




