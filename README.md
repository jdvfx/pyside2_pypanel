
# Create a Python Panel inside Houdini20.5

requirements:

- linux
- pyside2-uic
- designer-qt5
- houdini20.5

## in this example, the panel is named: "my_pythonpanel"

1) create a directory in your project files, eg:<br>
```mkdir -p /home/houdini_tools/my_pythonpanel ```

3) create a "packages" directory and a .json inside<br>
this updates $HOUDINI_PATH and add our houdini_tools directory<b>

```mkdir -p ~/houdini20.5/packages/my_pythonpanel.json```
```
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
```
4) create interface with QTDesigner5

5) save to .ui and convert to .py<br>
```pyside2-uic my_ui_file.ui my_ui_file.py```



