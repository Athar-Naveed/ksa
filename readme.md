## Keep Screen Active (KSA)

Whenever we are training our AI models, we have to wait for a long while keeping our screen active so, that we won't get disconnected to our runtime/kernel. Through this automation project we could do this without any hassle, just the run __exe__ or __deb__ file to start the project.

### Clone Info
To clone the project and run at your side, follow these steps:
1. Clone the repo.
2. In your terminal, create a venv, using:

```bash  
uv venv 
```

3. Activate the venv, using:
```bash
.venv\Scripts\activate # windows
```
and 
```bash
source .venv/bin/activate # linux
```
4. Install the dependencies, using:
```python
uv pip install -r requirements.txt
```
5. At the end run this command in the terminal:
```python
py main.py
```
