
import tkinter as tk
from tkinter import messagebox
import instaloader
from datetime import datetime
import os

current_datetime = datetime.now()

def download_post(url):
    global fn_entry 
    
    fn = fn_entry.get()
    L = instaloader.Instaloader(save_metadata=False)
    try:
        post_code = url.split("/")[-2] #url에서 post주소 추출
        post = instaloader.Post.from_shortcode(L.context, post_code)
        # 게시물 다운로드
        if fn == "":
            L.download_post(post, target=current_datetime)
            messagebox.showinfo("완료", "게시물을 다운로드했습니다.")
        else:
            L.download_post(post, target=fn)
            messagebox.showinfo("완료", "게시물을 다운로드했습니다.")
    except instaloader.exceptions.InstaloaderException as e: # gpt도움
        messagebox.showerror("오류", f"게시물을 다운로드하는 데 문제가 발생했습니다: {e}")

def download_post_from_entry():
    global url_entry, app
    post_url = url_entry.get()  # 게시물 URL을 입력으로 받음
    download_post(post_url)
    result = messagebox.askquestion("?","더 저장하기")

    if result == "yes":
        main
    else:
        app.destroy()


def main():
    global url_entry ,app ,fn_entry
    app = tk.Tk()
    app.title("인스타그램 사진/동영상 다운로더")
    #폴더명 입력
    foldername_label = tk.Label(app, text="폴더 명 : ")
    foldername_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    fn_entry = tk.Entry(app, width=50)
    fn_entry.grid(row=0, column=1, padx=5, pady=5)
    #url 입력
    url_label = tk.Label(app, text="인스타그램 게시물 URL:")
    url_label.grid(row=1, column=0, padx=2, pady=5, sticky="w")

    url_entry = tk.Entry(app, width=50)
    url_entry.grid(row=1, column=1, padx=5, pady=5)

    #txt파일 여부 
    cheak = tk.IntVar()
    cheak_txt = tk.Checkbutton(app, text="txt파일 여부", variable=cheak)
    cheak_txt.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")

    #다운로드 버튼
    download_button = tk.Button(app, text="다운로드", command=download_post_from_entry)
    download_button.grid(row=2, column=0, columnspan=2, pady=10)

    app.mainloop()

main()

#https://www.instagram.com/reel/C6xhVQUrAkW/?utm_source=ig_web_copy_link
