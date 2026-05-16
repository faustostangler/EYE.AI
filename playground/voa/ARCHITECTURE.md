# Voa Health Architecture Overview

This document describes the technical architecture of the Voa Health platform, based on reverse engineering and technical analysis.

## 1. System Architecture
Voa Health follows a modern decoupled architecture with a clear separation between the frontend application and the backend API.

- **Frontend Application**: `app.voa.health`
- **Backend API**: `api.voa.health`
- **Analytics & Orchestration**: Integrated via PostHog and Liveblocks.

## 2. Frontend Stack
- **Framework**: [Next.js](https://nextjs.org/) (App Router).
- **Icons & UI Components**: [Ant Design (antd)](https://ant.design/) and [Lucide React](https://lucide.dev/).
- **Real-time Collaboration**: [Liveblocks](https://liveblocks.io/) for presence and shared document state.
- **Client-side State**: Likely a mix of React Context and internal state management for the audio recorder.
- **Authentication**: [NextAuth.js](https://next-auth.js.org/) supporting Google and Apple OAuth providers. JWT (JSON Web Token) is persisted on the client-side to maintain sessions across reloads.
- **Offline Resilience & Networking**: The app actively monitors network changes (`net::ERR_NETWORK_CHANGED`) to protect the audio streaming. Audio is captured via the `MediaDevices API` and chunked for immediate transmission.

## 3. Backend Stack
- **API Engine**: [Django REST Framework (DRF)](https://www.django-rest-framework.org/).
- **Database**: Likely PostgreSQL (standard for Django/SaaS).
- **Authentication**: JWT (JSON Web Tokens) used for API authorization (Bearer tokens). Scoped to access the `api.voa.health` subdomain where core EHR operations occur.
- **Deployment**: Vercel (Frontend) and likely AWS or Google Cloud (Backend).
- **Audio Streaming & Encoding**: Uses an open streaming channel (likely WebSockets or Server-Sent Events) to send audio chunks continuously. The browser captures audio using the **Opus codec within a WebM container** (`audio/webm;codecs=opus`), optimizing for high fidelity voice capture at low bandwidth.
- **Data Schema**: Clinical documents are structured using **Tiptap / ProseMirror**, meaning the backend saves structured JSON (AST) rather than raw HTML, enabling advanced collaboration and granular AI insertions.

## 4. Key API Endpoints (v1)
| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/v1/user/` | GET | Current doctor profile, specialties, and feature flags. |
| `/api/v1/patient/` | GET | List of patients with pagination and search. |
| `/api/v1/ehr/` | GET/POST | Electronic Health Records (Atendimentos). |
| `/api/v1/document-templates/`| GET | Clinical templates for document generation. |
| `/api/v1/liveblocks/` | POST | Authentication for real-time collaboration. |

## 5. Intelligence Layer (Charcot AI)
The platform uses an AI assistant named **Charcot** (named after the French neurologist) for clinical transcription and reasoning. 
- **Role**: Summarizes audio, generates clinical documents (SOAP, receipts, etc.), and provides clinical insights. Acts as an orchestrator transforming raw transcription into structured medical data.
- **Mechanism**: LLM Wrapper with domain-specific grounding. Model names and context keys are dynamically injected via Next.js JavaScript chunks.
- **Security**: System prompts and core instructions are protected securely in the backend, though some contextual triggers are visible in the frontend chunks.

## 6. Observability & Analytics
- **PostHog**: Onnipresent. Used for event tracking, session recording, and feature flag management.
- **Monitoring**: Custom `/monitoring` endpoints for tracking performance and errors.
- **Marketing/Tracking**: Integrations with Google Analytics and Google Ads (`G-EE03ES08S9`).

## 7. Security & Vulnerability Posture
- **IDOR Mitigation**: All core entities (Patients, EHRs) use non-predictable **UUID v4** (e.g., `3df2b16b-254e-4c0d-9669-379e7a8f4437`), protecting against sequential record enumeration.
- **Token Security**: PII is primarily masked and managed server-side. JWTs dictate permissions, and attempting to modify the UUID in the URL without the correct JWT scope results in an immediate boundary failure (403/404).
- **Frontend Code**: No critical API keys (like OpenAI or raw Stripe secret keys) were found hardcoded in `window.__NEXT_DATA__`. Security boundaries appear well-respected between client and server.
