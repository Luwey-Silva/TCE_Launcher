import webview

window = webview.create_window('TCE Launcher', 'new project-html/home.html',
                               width=1025, height=700, resizable=False, confirm_close=True)
webview.start()
