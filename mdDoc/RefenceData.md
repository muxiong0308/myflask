- dash muli-pages 参考链接
https://github.com/plotly/dash/pull/70

- vscode 调试 flask 的配置文件
https://donjayamanne.github.io/pythonVSCodeDocs/docs/debugging_debugging-flask/
https://segmentfault.com/a/1190000008742844

- launch.json配置文件
vscode下可以打断点，但是不会reload
一旦启用reload，断点不会命中，原因未查。
```json
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "stopOnEntry": false,
            "env": {
                "FLASK_APP": "runDash.py",
                // "FLASK_ENV": "development",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload",
            ],
            "jinja": true
        }
    ]
}
```

