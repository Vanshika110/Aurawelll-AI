# Aurawell-AI — Intelligent Fitness & Wellness Integration Platform

> AI-powered health advisory system integrating LLM chatbot services with 
> cloud-managed infrastructure via Vultr's managed services.

---

## System Integration Overview

Aurawell-AI is not just a fitness app — it is a **system integration project** 
that connects an AI chatbot layer, a cloud-managed database, a Laravel backend, 
and a responsive frontend into a single production-deployable platform.
```
User Interface (Laravel Breeze)
        ↓
Laravel Backend (API Layer)
        ↓
AI Chatbot Service (LLM Integration)
        ↓
Vultr Managed Database (Cloud Infrastructure)
        ↓
Personalized Health Response → User
```

---

## What This Project Integrates

| Layer | Technology | Role |
|---|---|---|
| Frontend | Laravel Breeze · Blade | Chat UI, user input handling |
| Backend | Laravel (PHP) | API routing, business logic |
| AI Service | LLM Chatbot API | Natural language health advice |
| Database | Vultr Managed MySQL | Cloud-hosted persistent storage |
| Infrastructure | Vultr Cloud Compute | Managed server deployment |

---

## Key Features

- 🤖 **AI Chatbot Integration** — LLM connected to Laravel backend via service abstraction layer
- ☁️ **Cloud Infrastructure** — Deployed on Vultr managed services (compute + database)
- 🔐 **Auth System** — Laravel Breeze authentication with session management
- 📊 **Personalized Responses** — Context-aware fitness and wellness advice
- 🔄 **Decoupled Architecture** — AI provider swappable without changing frontend

---

## Tech Stack

![PHP](https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white)
![Laravel](https://img.shields.io/badge/Laravel-FF2D20?style=flat-square&logo=laravel&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Vultr](https://img.shields.io/badge/Vultr_Cloud-007BFC?style=flat-square&logo=vultr&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

---

## Setup & Deployment

### Local Development
```bash
git clone https://github.com/Vanshika110/aurawell-ai-integration
cd aurawell-ai-integration
composer install
cp .env.example .env
php artisan key:generate
php artisan migrate
php artisan serve
```

### Vultr Cloud Deployment

Full step-by-step guide for provisioning Vultr managed server and 
database, configuring environment, and deploying this application:

📹 **[Vultr Setup & Deployment Guide](https://drive.google.com/file/d/1o97HYNE-GQxjyoaYLoCwmAs64p8OF7my/view?usp=drivesdk)**

Covers:
- Vultr Managed Database provisioning
- Cloud Compute instance setup
- Environment variable configuration
- Laravel deployment on Vultr server

---

## Architecture — Integration Flow
```
[User] 
  → Laravel Breeze Auth 
  → Chat UI (Blade Frontend)
  → Laravel Controller (Request Handler)
  → AI Service Layer (LLM API Call)
  → Response Normalization
  → Vultr MySQL (Conversation Storage)
  → Formatted Response → [User]
```

---

## Project Significance

This project demonstrates core **System Integrator** competencies:

- **Cloud-service integration** — connecting managed infrastructure (Vultr) to application layer
- **AI API integration** — embedding LLM capabilities into a traditional MVC framework
- **Multi-layer system design** — frontend, backend, AI service, and database working as one
- **Production deployment** — not just local dev, deployed to real cloud infrastructure

---

## Repository

> **Note:** Repository name updated from `Aurawelll-AI` to `aurawell-ai-integration` 
> for clarity and professional consistency.

---

*Built as part of a system integration portfolio targeting AI + Cloud + Data domains.*
```
