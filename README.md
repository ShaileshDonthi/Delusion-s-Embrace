# Delusions Embrace

**Delusions Embrace** is an atmospheric, text-based psychological horror game. You play as a protagonist grappling with sanity.

Your choices matter. Hidden stats track your **Sanity**, **Doubt**, and **Attachment**, subtly altering the narrative text and the game's conclusion.


## Getting Started

Follow these instructions to get the game running on your local machine.

### Prerequisites

- Python 3.x installed on your system.

### Installation

1.  **Clone the repository** (or download the source code):
    ```bash
    git clone https://github.com/yourusername/delusions-embrace.git
    cd delusions-embrace
    ```

2.  **Create a virtual environment** (recommended to avoid dependency conflicts):
    ```bash
    python3 -m venv venv
    ```

3.  **Activate the virtual environment**:
    -   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    -   On Windows:
        ```bash
        venv\Scripts\activate
        ```

4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Playing the Game

#### Web Version (Recommended)
This version features the full atmospheric visual experience with CRT effects and seamless text flow.

1.  Run the Flask application:
    ```bash
    python3 app.py
    ```
2.  Open your web browser and navigate to:
    `http://127.0.0.1:8000`

#### Terminal Version
A pure text-based experience running directly in your command line.

1.  Run the main script:
    ```bash
    python3 main.py
    ```
