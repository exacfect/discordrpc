Set objShell = CreateObject("Wscript.Shell")
objShell.Run "cmd /c start """" discord.exe", 0, True
WScript.Sleep 10000
objShell.Run "cmd /c python app.pyw", 0, True