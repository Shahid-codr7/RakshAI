# RakshAI

RakshAI is a real-time AI-powered call vigilance system designed to detect **deepfake voices and fraudulent or harmful communication during live calls**.

The system integrates **acoustic intelligence** and **semantic analysis** into a unified pipeline that operates on **WebRTC-based voice communication streams**.

RakshAI continuously analyzes live calls to:

- Detect AI-generated deepfake voices
- Identify fraudulent or criminal intent in conversations
- Generate real-time risk signals during the call

The objective is to prevent **voice impersonation attacks, scam calls, and malicious communication**.

---

# Key Features

## Real-Time Call Monitoring
RakshAI processes **live WebRTC audio streams** and performs continuous analysis during an active call session.

## Deepfake Voice Detection
The acoustic engine analyzes audio characteristics to determine whether a voice is **real human speech or AI-generated synthetic audio**.

## Fraud & Harmful Intent Detection
The semantic engine transcribes spoken content and evaluates it to identify **fraud, threats, scams, or criminal intent**.

## Integrated Risk Scoring
Outputs from both engines are combined to produce a **risk assessment score for the ongoing call**.

---

# System Architecture

```
User Call (WebRTC)
        │
        ▼
 Real-Time Audio Stream
        │
        ▼
+---------------------------+
|      RakshAI Pipeline     |
+---------------------------+
        │
        ├── Acoustic Engine
        │      │
        │      └── Deepfake Voice Detection
        │
        └── Semantic Engine
               │
               └── Speech-to-Text + Intent Analysis
        │
        ▼
  Risk Classification
        │
        ▼
 Alert / Monitoring System
```

---

# Core Engines

## 1. Acoustic Engine (Voice Authenticity Detection)

The acoustic engine performs **real-time audio forensic analysis** to determine whether the voice in the call is genuine or artificially generated.

### Processing Pipeline

```
Live Audio Stream
       │
       ▼
Audio Preprocessing
       │
       ▼
Feature Extraction
(MFCC, Spectrogram, Pitch, Formants)
       │
       ▼
Deepfake Detection Model
       │
       ▼
Classification
Real Voice / AI Generated Voice
```

### Objectives

- Detect voice cloning attacks
- Identify synthetic speech generation
- Flag suspicious audio signatures

---

## 2. Semantic Engine (Intent & Fraud Detection)

The semantic engine analyzes the **content of the conversation**.

Speech from the call is transcribed and evaluated using NLP models to detect **harmful or fraudulent intent**.

### Processing Pipeline

```
Live Speech
     │
     ▼
Speech-to-Text
     │
     ▼
Text Normalization
     │
     ▼
Semantic Analysis Model
     │
     ▼
Intent Classification
```

# Example Use Cases

- Banking fraud detection during calls
- Deepfake voice scam prevention
- Secure customer verification

---

### Audio Processing
- Python
- wave2vec2
- Librosa
- PyAudio
- FFmpeg

### Machine Learning
- PyTorch
- TensorFlow
- Deepfake audio detection models

### NLP
- Transformer-based intent classification
- Contextual embeddings

### Backend
- FastAPI / Flask
- Streaming inference services

---

# Project Structure

```
RakshAI/
│
├── acoustic_engine/
│  
├── semantic_engine/
│  
└── README.md
```

---

# Future Improvements

- Real-time deepfake detection optimization
- Multi-language speech analysis
- Adaptive fraud detection models
- Integration with call center platforms
- Explainable AI for decision transparency

---

# Disclaimer

RakshAI is designed to **assist monitoring and fraud detection systems**.  
Final decisions should involve **human verification and oversight**.

---
