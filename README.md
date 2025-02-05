# 🚕 Evho - Ecosistema de Movilidad (MVP)

![Estado](https://img.shields.io/badge/Estado-Desarrollo_Activo-brightgreen) 
![Licencia](https://img.shields.io/badge/Licencia-MIT-blue)

Plataforma de movilidad urbana que conecta pasajeros con conductores en tiempo real.

## 🌟 Características Clave (MVP)

- **Registro/Login** de usuarios y conductores
- **Solicitud de viajes** con geolocalización en tiempo real
- **Asignación automática** de conductor más cercano
- **Simulación de pagos** integrada
- **Sistema de calificaciones**
- Panel administrativo básico

## 🛠 Tecnologías Utilizadas

| Área           | Tecnologías                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------|
| **Backend**    | [FastAPI](https://fastapi.tiangolo.com/), [MongoDB](https://www.mongodb.com/)                   |
| **Mobile**     | Swift (iOS), Kotlin (Android)                                                                   |
| **Web**        | [Reflex](https://reflex.dev/)                                                                   |
| **Infra**      | [Docker](https://www.docker.com/), [MongoDB Atlas](https://www.mongodb.com/atlas)               |
| **Herramientas**| [Postman](https://www.postman.com/), [Figma](https://www.figma.com/)                            |

## 📁 Estructura del Proyecto
evho/
├── backend/ # API principal
│ ├── routers/ # Endpoints de la API
│ ├── models/ # Modelos de datos
│ ├── services/ # Lógica de negocio
│ └── ...
├── mobile/ # Aplicaciones móviles
│ ├── ios/ # Versión iOS (Swift)
│ └── android/ # Versión Android (Kotlin)
├── web/ # Panel administrativo
│ ├── src/ # Código fuente Reflex/React
│ └── ...
├── docker-compose.yml # Configuración de servicios
└── .env.example # Variables de entorno


## 🚀 Primeros Pasos

### Prerequisitos
- Docker 20.10+
- Python 3.9+
- Node.js 16+ (para frontend web)
- Cuentas en [Stripe](https://stripe.com/) y [Google Maps Platform](https://mapsplatform.google.com/)

### Instalación

1. Clonar repositorio:
```bash
git clone https://github.com/tuusuario/evho.git
cd evho

📄 Licencia
Distribuido bajo licencia MIT. Ver LICENSE para más detalles.

🚨 Nota: Este proyecto está en activo desarrollo. ¡Reporta issues y sugerencias en nuestro tracker!

