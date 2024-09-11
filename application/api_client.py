import requests
from typing import Any


class APIClient():
    """Cliente para interactuar con una API externa."""

    def __init__(self, baseUrl: str):
        """Inicializa el cliente con la URL base de la API."""
        self.base_url = baseUrl

    def get(self, endpoint: str) -> dict[str, Any] | list[Any]:
        """Hace una solicitud GET a la API."""
        url = f"{self.base_url}/{endpoint}"
        data = {}
        response = requests.get(url)
        response.raise_for_status()# Lanza un error si la respuesta no es 200,  Lanza un error si la respuesta no es 200,  Lanza un error si la respuesta no es 200
        return response.json()

    def post(self, endpoint: str, data: dict[str, Any]) -> dict[str, Any]:
        """Hace una solicitud POST a la API."""
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def get_users(self) -> dict[str, Any] | list[Any]:
        """Obtiene la lista de usuarios de la API."""
        return self.get("users")

    def create_post(self, user_id: int, title: str, body: str) -> dict:
        """Crea un nuevo post para un usuario."""
        data = {
            "userId": user_id,
            "title": title,
            "body": body
        }
        return self.post("posts", data)

    def get_posts(self) -> dict[str, Any] | list:
        """Obtiene todos los posts."""
        return self.get("posts")

    def get_posts_count(self) -> int:
        """Obtiene la cantidad de posts."""
        return len(self.get_posts())

    def get_post_by_id(self, post_id) -> dict | list[Any]:
        """Obtiene un post específico por su ID."""
        return self.get(f"posts/{post_id}")