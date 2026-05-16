# Voa Health Design System & UI/UX

This document consolidates information about the visual layout, styles, and design patterns of the Voa Health application.

## 1. Visual Identity
- **Primary Color**: A vibrant purple/violet (Brand color).
- **Secondary Colors**: Grays for typography and borders, with emerald/green for success states.
- **Typography**: Likely using a modern sans-serif font (e.g., Inter or Roboto) integrated via Next.js Font.

## 2. Layout Structure
- **Sidebar Navigation**: Fixed left-side navigation with iconography for core modules (EHR, Patients, Chat, Settings).
- **Top Header**: Context-aware header showing page title (e.g., "Novo Atendimento") and user profile/credits.
- **Main Content Area**: Centered or left-aligned depending on the module, with a focus on clean, high-contrast text for clinical readability.

## 3. UI Components (Library: Ant Design)
- **Buttons**: Rounded corners, consistent padding. Usage of primary (purple) and ghost styles.
- **Modals/Drawers**: Used for patient creation, template selection, and "Pro" plan activations.
- **Form Inputs**: Standardized textboxes with placeholders and validation states.
- **Audio Recorder**: Custom component in the EHR section with visual audio waves and timer.

## 4. Design Patterns
- **Humble Object Pattern**: Clear separation between the rendering layer and the complex logic for audio processing/transcription.
- **Responsive Design**: Mobile-responsive sidebar (collapsible) and fluid grid layouts.
- **Empty States**: Well-designed illustrations and helper text (e.g., "Seus atendimentos de hoje irão aparecer aqui").

## 5. User Experience (UX) Highlights
- **Reduced Cognitive Load**: Information is grouped by clinical context (e.g., Patient Info -> Audio -> Document).
- **Proactive Feedback**: Real-time counters for "Atendimentos Gratuitos" and status alerts.
- **Omnipresent AI**: The "Charcot" assistant is easily accessible via the Chat module or directly within the EHR workflow.

## 6. CSS Details (Extracted)
- **Framework**: Tailwind CSS (extrapolated from layout classes and responsiveness).
- **Theming**: Supports Dark/Light mode via `theme-setter.js`.
