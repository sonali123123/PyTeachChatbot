# AI Teaching Assistant Platform

A robust platform that provides an AI-powered teaching assistant specializing in Python, Data Analysis, and Advanced Python topics.

## Features

- Interactive chat interface with context-aware responses
- Vector store-based document retrieval using FAISS or Qdrant
- Smart search capabilities with customizable embeddings
- Token management and quota system
- Admin token authentication
- Prompt logging and redaction capabilities

## Technical Components

### Core Functionality
- Chat handling with multiple LLM provider support
- Context-aware responses using vector similarity search
- Token counting and memory management
- Daily call quota monitoring

### Document Processing
- Automatic chunking of course materials
- Vector embeddings using HuggingFace Instruct Embeddings
- Support for multiple vector store backends (FAISS, Qdrant)
- Smart file organization with hierarchical heading structure

### Configuration
- Environment variable based configuration
- Customizable system prompts
- Flexible document chunking parameters
- API key management

### UI Elements
- Custom chat header and footer
- Pre-defined example questions
- Markdown support for rich text formatting

## Setup Requirements

1. Environment variables configuration
2. Course materials in the designated folder
3. Vector store setup (FAISS or Qdrant)
4. Required API keys for chosen LLM provider

## Usage

The system acts as an intelligent teaching assistant that:
- Provides clear explanations with practical examples
- Uses real-life analogies for better understanding
- Focuses on course-specific content
- Maintains an encouraging and educational tone

## File Structure

- `chat_caller.py`: Main chat interaction logic
- `chat_utils.py`: Utility functions for chat interface
- `read_to_vectorstore.py`: Document processing and vectorization
- `process_prompt_redaction_requests.py`: Privacy and data management
- `course_material/`: Course content and prompt templates

## Security Features

- Admin token authentication
- Daily usage limits
- Prompt logging and redaction capabilities
- Configurable access controls
