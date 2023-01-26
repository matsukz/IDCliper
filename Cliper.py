import tkinter, tkinter.messagebox
from tkinter import ttk
import tkinter .font as f
from tkinter import filedialog

import os
import subprocess
import json

root = tkinter.Tk()
root.title("Cliper")
root.geometry("300x400+1000+50")
root.resizable(0,0)
root.attributes("-topmost", True)

Json_Path = ""
Executable = False
ImpJson = ""

JsonText = tkinter.Label(
    root,
    text="設定ファイルの場所",
    font=(
        "",
        "10",
        "bold"
    )
)
JsonText.place(x=10, y=10)

JsonPath_TextBox = tkinter.Entry(
    root,
    font=(
        "",
        12
    )
)
JsonPath_TextBox.place(
    x=30,
    y=40,
    width=180,
    height=30
)

Check_Ready = tkinter.Label(
    root,
    text="状態：設定ファイルの待機中",
    font=(
        "",
        "10",
        "bold"
    )
)
Check_Ready.place(x=30, y=150)

def Select_Json_path():
    global Executable
    Executable = False
    Check_Ready["text"] = "状態：設定ファイルの待機中"

    Inst_Json_Path = (filedialog.askopenfilename(
        title= "設定ファイルを開く",
        filetypes=[("JSON File",".json")],
        initialdir= "./"
    ))

    if not Inst_Json_Path == "":
        if not JsonPath_TextBox.get() == "":
            JsonPath_TextBox.delete("0","end")
        else:
            pass
    else:
        pass

    JsonPath_TextBox.insert("0",
    Inst_Json_Path.replace("/","\\")
)
Select_Json_button = tkinter.Button(
    text="１選択",
    command=Select_Json_path,
    width=6,
    height=1
)
Select_Json_button.place(x=220,y=43)

def JsonCheck():
    global Executable
    Executable = False
    global Json_Path
    global ImpJson
    Json_Path = JsonPath_TextBox.get()

    if not Json_Path == "":

        try:
            ImpJson = json.load(
                open(
                    Json_Path,
                    "r",
                    encoding="utf-8"
                )
            )
        except FileNotFoundError:
            tkinter.messagebox.showerror(
                "エラー",
                "ファイルパスに誤りがあります"
            )
            return
        try:
            if ImpJson["Check"]["CheckSum"] == "True":
                Executable = True
                Check_Ready["text"] = "状態：準備完了"
            else:
                tkinter.messagebox.showerror(
                    "エラー",
                    "この設定ファイルは使用できません \n 解決方法：正規の設定ファイルをGitHubから入手する。"
                )
                Check_Ready["text"] = "状態：設定ファイルの待機中"
        except KeyError:
            tkinter.messagebox.showerror(
                "エラー",
                "この設定ファイルは使用できません　\n 解決方法：正規の設定ファイルをGitHubから入手する。"
            )
            Check_Ready["text"] = "状態：設定ファイルの待機中"
            
    else:
        tkinter.messagebox.showerror(
            "エラー",
            "設定ファイルの場所を選択してください"
        )

Check_Json_button = tkinter.Button(
    text="２設定読み込み",
    command=JsonCheck,
    width=23,
    height=2
)
Check_Json_button.place(x=30,y=90)

def ExeIDCopy():
    print(Executable)
    if Executable == True:
        try:
            subprocess.run(
                "set /p cmdtmp=\"" + ImpJson["Main"]["StudentID"] + "\"< nul | clip",
                shell=True
            )
        except KeyError:
            tkinter.messagebox.showerror(
                "エラー",
                "設定ファイルが破損しています"
            )
    else:
        tkinter.messagebox.showerror(
            "エラー",
            "実行許可がありません \n 解決方法：設定ファイルをロードする。"
        )

ExeIDCopy_Button = tkinter.Button(
    text="コピー：学籍番号",
    command=ExeIDCopy,
    width=25,
    height=3
)
ExeIDCopy_Button.place(x=30,y=180)

def ExePWCopy():
    print(Executable)
    if Executable == True:
        try:
            subprocess.run(
                "set /p cmdtmp=\"" + ImpJson["Main"]["PassWord"] + "\"< nul | clip",
                shell=True
            )
        except KeyError:
            tkinter.messagebox.showerror(
                "エラー",
                "設定ファイルが破損しています"
            )
    else:
        tkinter.messagebox.showerror(
            "エラー",
            "実行許可がありません \n 解決方法：設定ファイルをロードする。"
        )

ExePWCopy_Button = tkinter.Button(
    text="コピー：パスワード",
    command=ExePWCopy,
    width=25,
    height=3
)
ExePWCopy_Button.place(x=30,y=250)

def ExeMACopy():
    print(Executable)
    if Executable == True:
        try:
            subprocess.run(
                "set /p cmdtmp=\"" + ImpJson["Main"]["MailAddress"] + "\"< nul | clip",
                shell=True
            )
        except KeyError:
            tkinter.messagebox.showerror(
                "エラー",
                "設定ファイルが破損しています \n 解決方法：設定ファイルをロードする。"
            )
    else:
        tkinter.messagebox.showerror(
            "エラー",
            "実行許可がありません"
        )

ExeMACopy_Button = tkinter.Button(
    text="コピー：メールアドレス",
    command=ExeMACopy,
    width=25,
    height=3
)
ExeMACopy_Button.place(x=30,y=320)

root.mainloop()
