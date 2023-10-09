# django-playbook

Este es un script básico de ansible para instalar automáticamente un ambiente de desarrollo remoto para django.
Se asume una máquina con Ubuntu 22.04.

Se incluye:
- nvim como editor
- PostgreSQL

Por hacer:
- Se clona un repositorio con un proyecto de django en GitHub.
- Se crea un ambiente virtual e instalan los requerimientos.

Por lo pronto se asume la ejecución con el servidor para desarrollo de django.

# Uso dentro de codespaces

0. Abre este repo en un codespace
1. Sube el archivo de llave al directorio `ssh-keys`. Hax click derecho en folder ssh-keys en el explorer y aparece la opción Upload...
2. Cambia los permisos del archivo: `chmod 400 ssh-keys/mi-llave.pem`
3. Instala ansible `pip install ansible`
4. Agrega tu host y llave al archivo hosts.yml
5. Ejecuta el playbook deseado, por ejemplo: `ansible-playbook playbooks/postgres.yml -i hosts.yml`



