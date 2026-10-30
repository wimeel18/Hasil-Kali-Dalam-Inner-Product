# Hasil Kali Dalam (Inner Product Space)

A simple desktop application developed using Python, Kivy, and KivyMD to introduce and demonstrate the concept of Inner Product Space in Linear Algebra.

## 📌 About the Project

**Hasil Kali Dalam** is an educational application designed to help users understand the concept of inner products in vector spaces and explore their fundamental properties through simple calculations.

The application provides an introductory explanation and an interactive calculation interface for checking the four axioms of an inner product.

## ✨ Features

- **Introduction to Inner Product Space** — Provides a brief explanation of the concept of inner product spaces.
- **Interactive Calculation** — Allows users to input vectors and a scalar for calculations.
- **Commutativity** — Checks the commutative property of the inner product.
- **Linearity** — Demonstrates the linearity property.
- **Homogeneity** — Checks scalar multiplication properties.
- **Positive Definiteness** — Evaluates the inner product of a vector with itself.
- **Simple User Interface** — Built with KivyMD for a straightforward desktop experience.

## 🛠️ Built With

- Python
- Kivy
- KivyMD

## 📂 Project Structure

```text
Hasil-Kali-Dalam/
│
├── main.py
│
├── kv/
│   ├── hkd.kv
│   ├── aksioma.kv
│   └── assets/
│       ├── fonts/
│       └── foto/
│
└── screens/
    ├── screens.py
    ├── hkd.py
    └── aksioma.py
```

## 🚀 Getting Started

### Prerequisites

Make sure Python is installed on your computer.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/wimeel18/Hasil-Kali-Dalam.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Hasil-Kali-Dalam
   ```

3. Install the required libraries:

   ```bash
   pip install kivy kivymd
   ```

### Run the Application

Execute the following command:

```bash
python main.py
```

## 📖 How to Use

1. Launch the application.
2. Read the introduction to Inner Product Space.
3. Click the **Hitung** button to access the calculation page.
4. Enter vectors `u`, `v`, and `w` using space-separated numbers.
5. Enter a scalar value `k`.
6. Click **Hitung Aksioma** to display the calculation results.

## 🎯 Learning Objectives

This project was developed as part of a learning activity in Linear Algebra, particularly to understand the mathematical properties of inner product spaces and apply basic Python programming concepts to build an interactive desktop application.

## 👩‍💻 Contributors

Developed as an academic project.

---

*Learning mathematics through programming.*
