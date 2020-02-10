# Tender Hack.Msk project

> Serious project developed by a serious team 
>
> [![](https://img.shields.io/badge/backend-Stepan%20Denisov-lightblue)](https://vk.com/sd.denisoff 'VK profile')
> [![](https://img.shields.io/badge/frontend-Matvey%20Kottsov-orange)](https://vk.com/kottsovcom 'VK profile')
> [![](https://img.shields.io/badge/UX%2FUI-Leonid%20Kravtsov-green)](https://vk.com/kravtsovjr 'VK profile')
> [![](https://img.shields.io/badge/PM%26BA-Pavel%20Krylov-lightgrey)](https://vk.com/pkryloff 'VK profile')

## Technology stack

#### Backend
- Python3
- Flask + addons
- MVC pattern

#### Frontend
- HTML5 + CSS3
- Jinja2

## Launch instruction

1. Clone the repository and change the directory
    ```
    git clone <link>
    cd <project_directory>
    ```
    
2. Create a virtual environment and activate it
    ```
    virtualenv --python=python3 venv
    source venv/bin/activate
    ```

3. Install dependencies
    ```
    pip3 install -r requirements.txt
    ```

4. Create tables in the database
    ```
    python3 migrate.py
    ```

5. Launch web application
    ```
    python3 runner.py
    ```

Developed by [PPnP](https://team.ppnp.me 'Team website') team
