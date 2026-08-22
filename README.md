# BY GUALTIERI GIANNI

# 🛠️ Terminal Utility Toolkit


A lightweight terminal-based Python toolset that includes:
![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge)
![UI](https://img.shields.io/badge/Rich--UI-green?style=for-the-badge)
![CLI Tool](https://img.shields.io/badge/CLI--Tool-orange?style=for-the-badge)


- 🔍 A multithreaded port scanner with a sleek terminal UI
- 🖥️ A system information summary using `psutil`
- 🎨 A graphical menu powered by `Rich`


## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- pip

### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### 📁 Clone the repository

```bash
git clone https://github.com/yourusername/terminal-utility-toolkit.git
cd terminal-utility-toolkit
```

---

## ▶️ Run the tool

```bash
python main.py
```

---

## 🛠️ Command-Line Options

| Flag     | Description                         |
|----------|-------------------------------------|
| `--pt`   | Launch the port scanner             |
| `--si`   | Show system information summary     |
| `--rm`   | print the README                    |
| *(no flag)* | Launch the main graphical menu   |

### 🔍 Example

```bash
python main.py --pt
```

---

## 💻 Features

- **Port Scanner**:  
  - Scans ports 1–1024 using multithreading  
  - Displays open ports in a colorful table  
  - Progress bar during scan  

- **System Info**:  
  - Displays RAM, CPU, OS details  
  - Rich layout and styling  

- **Graphical Menu**:  
  - Clean terminal UI using Rich  

---

## 🧰 Technologies Used

| Library  | Purpose                                      |
|----------|----------------------------------------------|
| `rich`   | Terminal formatting, tables, progress bars   |
| `socket` | Network communication for port scanner       |
| `psutil` | System info: CPU, RAM, OS                    |
| `threading` | Fast concurrent port scanning            |

---

## 📁 File Structure

```text
terminal-utility-toolkit/
│
├── main.py                  # Entry point with CLI arguments
├── port_scanner.py          # Port scanner module
├── sysinfo.py               # System info summary module
├── graphic_display.py       # Terminal menu UI
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🙌 Contributing

Pull requests are welcome! Feel free to fork the project and submit improvements.

---

## 📜 License

MIT License
