from sys import getsizeof
import tkinter as tk
from tkinter import filedialog, StringVar, messagebox
import os
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

def open_file():
    path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("HTML Files", "*.html;*.htm"), ("All Files", "*.*")])
    if path:
        try:
            with open(path, "r", encoding="utf-8") as file:
                text.delete("1.0", tk.END)
                text.insert(tk.END, file.read())
                update_field()
        except Exception:
            tk.messagebox.showerror("Error", "Failed to open file")
        if os.path.exists(path):
            file_size = os.path.getsize(path)
            file_size_label.config(text=f"Size: {file_size} bytes")
        else:
            file_size_label.config(text="Size: 0 bytes")
        window.title(f"HTML Editor - {os.path.basename(path)}")

def save():
    path = filedialog.asksaveasfilename(
        defaultextension="html",
        filetypes=[("Text Files", "*.txt"), ("HTML files", "*.html;*.htm"), ("All files", "*.*")])
    if path:
        with open(path, 'w', encoding="utf-8") as file:
            file.write(text.get('1.0', tk.END))
        update_field()
        window.title(f"HTML Editor - {os.path.basename(path)}")

def clear():
    text.delete('1.0', tk.END)
    update_field()

def search():
    text.tag_remove('highlight', '1.0', tk.END)
    keyword_text = keyword.get()
    pos = text.search(keyword_text, '1.0', stopindex=tk.END, nocase=True)
    if pos:
        end_line, end_column = pos.split('.')
        end_line = int(end_line)
        end_column = int(end_column) + len(keyword_text)
        end = f"{end_line}.{end_column}"
        text.tag_add('highlight', pos, end)
        text.mark_set("insert", pos)
        text.see(pos)
        text.tag_config('highlight', background='yellow')
    else:
        messagebox.showwarning("Result", "Search term not found")

def update_field(event=None):
    content = text.get('1.0', tk.END)
    charCount = len(content.replace(" ", "").replace("\n", ""))
    wordCount = len(content.split())
    file_size_label.config(text=f"Size: {getsizeof(content)}")
    char_count_label.config(text=f"Characters: {charCount}")
    word_count_label.config(text=f"Words: {wordCount}")

class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []                      

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)                  

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                 

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()               
    
def matching_html(raw):
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

def is_matched_html(raw):
    S = ArrayStack()
    j = raw.find('<')               
    while j != -1:
        k = raw.find('>', j+1)        
        if k == -1:
            return False               
        tag = raw[j+1:k]              
        if not tag.startswith('/'):   
            result = tag.split()
            S.push(result[0])
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

def pop_all(self, temp = None):
    if self.is_empty() and temp is None:
        raise Empty('Stack is empty')
    if temp is None:
        temp = []
    if self.is_empty():
        return temp
    temp2 = temp + [self._data.pop()]
    return self.pop_all(temp2)

def get_top_word_frequencies(text_content, top_n=10):
    word_frequency = {}
    for word in text_content.split():
        word = word.lower()
        word = word.strip('.,!?()[]{}":;\n')
        if word:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
    sorted_word_frequency = sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)
    return sorted_word_frequency[:top_n]

if __name__ == '__main__':
    import webbrowser
    window = tk.Tk()
    window.title("HTML Editor")
    frame = tk.Frame(window)
    frame.pack(side=tk.LEFT, fill=tk.Y)
    open_button = tk.Button(frame, text="Open", command=open_file, bd=0, bg="lightblue", padx=10, pady=10)
    open_button.pack(pady=10, padx=5)
    save_button = tk.Button(frame, text="Save", command=save, bd=0, bg="lightgreen", padx=10, pady=10)
    save_button.pack(pady=10, padx=5)
    clear_button = tk.Button(frame, text="Clear", command=clear, bd=0, bg="pink", padx=10, pady=10)
    clear_button.pack(pady=10, padx=5)

    def validate_html():
        html_content = text.get('1.0', tk.END)
        if is_matched_html(html_content):
            messagebox.showinfo("HTML Validation", "All HTML tags are properly matched.")
        else:
            messagebox.showerror("HTML Validation", "HTML tags are not properly matched!")

    def preview_html():
        import tempfile
        html_content = text.get('1.0', tk.END)
        with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html', encoding='utf-8') as f:
            f.write(html_content)
            temp_path = f.name
        webbrowser.open(f'file://{temp_path}')

    validate_button = tk.Button(frame, text="Validate HTML", command=validate_html, bd=0, bg="orange", padx=10, pady=10)
    validate_button.pack(pady=10, padx=5)
    preview_button = tk.Button(frame, text="Preview HTML", command=preview_html, bd=0, bg="violet", padx=10, pady=10)
    preview_button.pack(pady=10, padx=5)

    # --- Top 10 Word Frequency GUI ---
    freq_label = tk.Label(frame, text="Top 10 Words", bg="gray90")
    freq_label.pack(pady=(20, 0), padx=5)
    freq_listbox = tk.Listbox(frame, width=22, height=12)
    freq_listbox.pack(pady=5, padx=5)

    def update_word_frequency():
        freq_listbox.delete(0, tk.END)
        content = text.get('1.0', tk.END)
        top_words = get_top_word_frequencies(content, 10)
        for word, count in top_words:
            freq_listbox.insert(tk.END, f"{word}: {count}")

    freq_button = tk.Button(frame, text="Update Word Frequency", command=update_word_frequency, bd=0, bg="lightyellow", padx=10, pady=5)
    freq_button.pack(pady=(0, 10), padx=5)

    keyword = StringVar()
    search_entry = tk.Entry(frame, textvariable=keyword)
    search_entry.pack(pady=5, padx=5, fill=tk.X)
    search_button = tk.Button(frame, text="Search", command=search, bd=0, bg="yellow", padx=10, pady=10)
    search_button.pack(pady=10, padx=5)
    text = tk.Text(window, wrap='word', bg="black", fg="white", insertbackground="white")
    text.pack(expand=1, fill='both', side=tk.TOP)
    text.bind("<KeyRelease>", update_field)
    status_frame = tk.Frame(window)
    status_frame.pack(side=tk.BOTTOM, fill=tk.X)
    word_count_label = tk.Label(status_frame, text="Words: 0")
    char_count_label = tk.Label(status_frame, text="Characters: 0")
    file_size_label = tk.Label(status_frame, text="Size: 0 bytes")
    for label in [word_count_label, char_count_label, file_size_label]:
        label.pack(side=tk.LEFT, padx=5)
    window.geometry("900x650")
    window.mainloop()

