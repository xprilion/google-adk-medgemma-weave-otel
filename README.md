# Doctor Agent

A medical assistant agent that can search for medical information, provide health advice, analyze symptoms, and offer medical guidance using internet search capabilities via Google Programmable Search API.

## Features

- **Medical Information Search**: Search for the latest medical information and guidelines
- **Drug Information**: Get information about medications, side effects, and dosages
- **Symptom Analysis**: Analyze symptoms and provide potential causes
- **Emergency Advice**: Get emergency medical advice for urgent situations
- **Health Tips**: Access general health tips for various categories
- **Medical Guidelines**: Retrieve treatment guidelines for specific conditions

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Google Programmable Search API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Custom Search API
4. Create credentials (API Key)
5. Go to [Google Programmable Search Engine](https://programmablesearchengine.google.com/)
6. Create a new search engine
7. Configure it to search the entire web

### 3. Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
GOOGLE_SEARCH_API_KEY=your_google_search_api_key_here
GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id_here
```

### 4. Run the Application

```bash
python main.py
```

The API will be available at `http://localhost:8080`

## API Endpoints

The agent provides various medical tools:

- `search_medical_info(query)`: General medical information search
- `get_medical_guidelines(condition)`: Get treatment guidelines
- `get_drug_information(drug_name)`: Drug information and side effects
- `get_symptom_analysis(symptoms)`: Analyze symptoms and causes
- `get_emergency_advice(emergency)`: Emergency medical advice
- `get_health_tips(category)`: General health tips

## Important Disclaimer

This agent is designed to provide general medical information and should not be used as a substitute for professional medical advice. Always consult with qualified healthcare professionals for serious medical concerns, diagnosis, and treatment.

## Usage Examples

- "What are the symptoms of diabetes?"
- "Tell me about the side effects of aspirin"
- "What are the treatment guidelines for hypertension?"
- "I have chest pain, what should I do?"
- "Give me nutrition tips for heart health"
