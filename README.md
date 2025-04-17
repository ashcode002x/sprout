# 🌱 Sprout

A modern web-based meeting platform that enables real-time communication and collaboration.

## ✨ Features

- **Real-time Communication**: Connect with participants seamlessly
- **Meeting Management**: Create, schedule, and manage meetings
- **Customizable Permissions**: Control participant access and capabilities
- **Multiple Meeting Types**: Support for different meeting formats
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Technology Stack

- **Backend**: Django (Python)
- **Real-time Communication**: Flask with Socket.IO
- **Database**: PostgreSQL
- **Containerization**: Docker & Docker Compose
- **Frontend**: HTML, CSS, JavaScript with jQuery

## 📋 Prerequisites

- Docker and Docker Compose
- Git

## 🚀 Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ashcode002x/sprout.git
   cd sprout
   ```

2. Create your `.env` file (or use the existing one for development):
   ```bash
   cp .env.example .env
   ```

3. Build and start the containers:
   ```bash
   docker-compose up -d
   ```

4. Access the application:
   - Django app: [http://localhost:8000](http://localhost:8000)
   - Socket.IO server: [http://localhost:5000](http://localhost:5000)

## 🔧 Configuration

### Environment Variables

The project uses the following environment variables:

**Database Configuration**
- `POSTGRES_DB`: Database name
- `POSTGRES_USER`: Database user
- `POSTGRES_PASSWORD`: Database password

**Django Configuration**
- `DJANGO_SECRET_KEY`: Secret key for Django
- `DEBUG`: Enable/disable debug mode
- `ALLOWED_HOSTS`: Allowed hosts for Django
- `DJANGO_SETTINGS_MODULE`: Django settings module path
- `DB_ENGINE`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`: Database connection settings
- `MEDIA_ROOT`, `STATIC_ROOT`: Paths for media and static files

**Flask/Socket.IO Configuration**
- `FLASK_DEBUG`: Enable/disable Flask debug mode
- `FLASK_SECRET_KEY`: Secret key for Flask
- `SOCKET_CORS_ALLOWED_ORIGINS`: CORS configuration for Socket.IO

## 📁 Project Structure

```
sprout/
├── backend/              # Django application
│   ├── static/           # Static assets
│   ├── templates/        # HTML templates
│   └── ...
├── flask-sock-connection/ # Flask Socket.IO server
├── .env                  # Environment variables
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile.django     # Dockerfile for Django
└── Dockerfile.flask      # Dockerfile for Flask
```

## 🖥️ Usage

### Creating a Meeting

1. Navigate to the home page
2. Fill out the meeting creation form:
   - Name
   - Description
   - Start/End time
   - Meeting type
   - Participant permissions
3. Click "Create Meeting"

### Joining a Meeting

1. Use the provided meeting ID to join
2. Access meeting details page to see all information
3. Click "Join Meeting" to enter the virtual meeting space

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔒 Security

Note: The included `.env` file contains development credentials. For production:
- Change all passwords and secret keys
- Disable debug mode
- Configure proper CORS settings
- Restrict allowed hosts

---

Made with ❤️ by the Sprout Team
