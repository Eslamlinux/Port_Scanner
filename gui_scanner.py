import tkinter as tk
from tkinter import messagebox
import subprocess
import threading

def run_scanner():
    target_ip = entry_ip.get()
    target_port = entry_port.get()

    if not target_ip or not target_port:
        messagebox.showwarning("Error", "Please Enter the ip and port")
        return

    # تغيير النص ليظهر أن الفحص جاري
    btn_scan.config(state=tk.DISABLED, text="Scan Runing")
    lbl_result.config(text="please wait", fg="blue")

    # تشغيل الفحص في Thread منفصل لكي لا تتجمد الواجهة
    thread = threading.Thread(target=execute_cpp_logic, args=(target_ip, target_port))
    thread.start()

def run_about():
    messagebox.showinfo("About the Programmer", "Hello My Name Is Eslam Linux\nthis is free software Pentest Port Scanner v1.0 for scan ports is opened or closed")
    return
    # تشغيل الفحص في Thread منفصل لكي لا تتجمد الواجهة
    # thread = threading.Thread(target=execute_cpp_logic, args=(target_ip, target_port))
    # thread.start()


def execute_cpp_logic(ip, port):
    try:
        # استدعاء ملف الـ C++ المترجم (تأكد أن اسمه scanner)
        result = subprocess.run(['./scanner', ip, port], capture_output=True, text=True)
        status = result.stdout.strip()

        # تحديث الواجهة بالنتيجة
        if status == "OPEN":
            lbl_result.config(text=f"Port {port} Opened! ✅", fg="green")
        else:
            lbl_result.config(text=f"Port {port} Close ❌", fg="red")
            
    except Exception as e:
        lbl_result.config(text="Working Error", fg="orange")
    
    # إعادة الزر لحالته الطبيعية
    btn_scan.config(state=tk.NORMAL, text="Start Scan")

# --- إعدادات النافذة ---
root = tk.Tk()
root.title("Pentest Port Scanner v1.0")
root.geometry("400x280")

# تسميات وحقول الإدخال
tk.Label(root, text="Pentest Port Scanner v1.0",font=("Arial", 16)).pack(pady=5)
tk.Label(root, text="Target IP:", font=("Arial", 12)).pack(pady=5)
entry_ip = tk.Entry(root, font=("Arial", 12), justify='center')
entry_ip.insert(0, "127.0.0.1") # قيمة افتراضية
entry_ip.pack()

tk.Label(root, text="Port:", font=("Arial", 12)).pack(pady=5)
entry_port = tk.Entry(root, font=("Arial", 12), justify='center')
entry_port.insert(0, "80") # قيمة افتراضية
entry_port.pack()

# نتيجة الفحص
lbl_result = tk.Label(root, text="", font=("Arial", 13, "bold"))
lbl_result.pack(pady=15)

# زر التشغيل
btn_scan = tk.Button(root, text="Start Scan", command=run_scanner, 
                      bg="#2c3e50", fg="white", font=("Arial", 12), width=15)
btn_scan.pack()

btn_about = tk.Button(root, text="About the Programmer", command=run_about, 
                      bg="#2c3e50", fg="white", font=("Arial", 10), width=15)
btn_about.pack()

root.mainloop()